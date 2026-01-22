# 🔍 YouTube Influencer Discovery Tool

A **keyword-driven influencer discovery application** built using **Streamlit** and the **YouTube Data API v3**.  
The tool enables discovery of **small to mid-sized YouTube creators across any niche**, with pagination, audience-size filtering, and exportable datasets.

---

## 🚀 Overview

This application allows users to:
- Search YouTube creators by **any keyword**
- Paginate through large result sets
- Filter creators by **subscriber count**
- Export structured data for **outreach, GTM, or analysis**

The project is designed to be **API-first**, **deployment-ready**, and **easily extensible**.

---

## ✨ Key Features

- Keyword-based creator discovery (channel metadata)
- Pagination support (50 results per page)
- Subscriber-range filtering
- CSV export for downstream workflows
- Secure API key handling
- Streamlit Cloud deployment support

---

## 🧱 Tech Stack

- **Python**
- **Streamlit**
- **YouTube Data API v3**
- **Pandas**

---

## 📁 Project Structure

youtube-influencer-discovery/
├── sat_scraper_app.py # Streamlit application
├── requirements.txt # Dependency definitions
└── README.md # Project documentation

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sat-scraper.git
cd sat-scraper
```
### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Steps to Generate an API Key

1. Visit https://console.developers.google.com/
2. Create a new project
3. Enable YouTube Data API v3
4. Go to APIs & Services → Credentials
5. Create an API key

### 5. Deployment (Streamlit Cloud)

1. Push the project to a public GitHub repository
2. Go to https://streamlit.io/cloud and sign in
3. Click New App
4. Select:
  4.1. Repository
  4.2. Branch (e.g., main)
  4.3. Entry file: sat_scraper_app.py
8. Add the API key under Settings → Secrets
9. Click Deploy
The application will be live at:
https://<username>-<repo-name>.streamlit.app


### Built by Satyarth
#### For questions or collaborations, reach out at jaiswal.satyarth070@gmail.com
