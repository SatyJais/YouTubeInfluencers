import streamlit as st
from googleapiclient.discovery import build
import pandas as pd
import os
API_KEY = os.getenv("API_KEY")
# ---- CONFIG ----
# API_KEY = 'AIzaSyBdskqXi7npoqY9GZyOMSmHGOVQUyqCVP4'  # <-- Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=API_KEY)

# ---- FUNCTIONS ----
def search_channels(query):
    request = youtube.search().list(
        q=query,
        type='channel',
        part='snippet'
    )
    response = request.execute()
    return response['items']

def get_channel_stats(channel_id):
    request = youtube.channels().list(
        part='statistics,snippet',
        id=channel_id
    )
    response = request.execute()
    if response['items']:
        stats = response['items'][0]
        return {
            'Channel Name': stats['snippet']['title'],
            'Channel ID': channel_id,
            'Subscribers': int(stats['statistics'].get('subscriberCount', 0)),
            'Video Count': stats['statistics'].get('videoCount', 'N/A'),
            'Description': stats['snippet'].get('description', ''),
            'URL': f"https://www.youtube.com/channel/{channel_id}"
        }
    return {}

# ---- STREAMLIT UI ----
st.title("🎓 YouTube Influencer Finder")

search_query = st.text_input("Search Keyword", value="SAT prep")
max_subs = st.slider("Max Subscriber Count", min_value=1000, max_value=500000, value=250000, step=1000)
run_search = st.button("Search YouTube Influencers")

if run_search:
    with st.spinner("Searching..."):
        results = search_channels(search_query)
        influencer_data = []

        for item in results:
            channel_id = item['snippet']['channelId']
            stats = get_channel_stats(channel_id)
            if 100 <= stats.get('Subscribers', 0) <= max_subs:
                influencer_data.append(stats)

        if influencer_data:
            df = pd.DataFrame(influencer_data)
            st.success(f"Found {len(df)} influencers.")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "youtube_influencers.csv", "text/csv")
        else:
            st.warning("No influencers found in that range.")
