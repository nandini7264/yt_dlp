# 🎥 YouTube Recommendation Scraper & Metadata Pipeline

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objective](#-project-objective)
- [System Architecture (Nested Data Flow)](#️-system-architecture-nested-data-flow)
- [Database Structure](#-database-structure)
- [Core Functional Components](#-core-functional-components)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Key Capabilities](#-key-capabilities)
- [Potential Extensions](#-potential-extensions)
- [Conclusion](#-conclusion)

---

## 📌 Project Overview

This project builds an automated YouTube data extraction pipeline that:

1. Crawls recommended video links using Selenium  
2. Expands the recommendation network recursively  
3. Extracts structured metadata using yt-dlp  
4. Stores all processed data into a SQLite database  

The system transforms unstructured web content into structured analytical data.

---

## 🎯 Project Objective

- Automate extraction of YouTube recommendation links
- Collect structured metadata (title, description, likes, views)
- Store results in a relational SQLite database
- Enable scalable video network analysis

---

## ⚙️ System Architecture (Nested Data Flow)

```
Seed Video URL
    │
    ▼
[ Selenium Recommendation Crawler ]
    │
    ├── Open video page
    ├── Extract recommended video links
    ├── Filter valid YouTube URLs
    └── Store unique links in SQLite
            │
            ▼
[ SQLite Database - links table ]
            │
            ▼
[ yt-dlp Metadata Extractor ]
    │
    ├── Fetch video URL
    ├── Extract title
    ├── Extract description
    ├── Extract like count
    ├── Extract view count
    └── Insert structured data
            │
            ▼
[ SQLite Database - data1 table ]
```

---

## 📂 Database Structure

### 1️⃣ links Table
Stores discovered YouTube video URLs.

| Column | Type |
|--------|------|
| link   | TEXT |

---

### 2️⃣ data1 Table
Stores structured metadata for each processed video.

| Column       | Type    |
|-------------|----------|
| url         | TEXT     |
| title       | TEXT     |
| description | TEXT     |
| likes       | INTEGER  |
| views       | INTEGER  |

---

## 🧠 Core Functional Components

### 🔹 Recommendation Crawler (Selenium)
- Opens YouTube video pages
- Extracts recommended video links
- Expands recommendation graph
- Inserts discovered URLs into SQLite

### 🔹 Metadata Extractor (yt-dlp)
- Processes stored URLs
- Extracts structured metadata
- Uses safe parameterized SQL insertion
- Handles missing fields gracefully

### 🔹 Data Storage (SQLite)
- Persistent storage of:
  - Raw discovered links
  - Structured video metadata
- Supports scalable pagination using LIMIT + OFFSET

---

## 🛠 Technologies Used

- Python
- Selenium WebDriver
- yt-dlp
- SQLite3
- ChromeDriver Manager

---

## 📁 Project Structure

```
youtube-recommendation-pipeline/
│
├── recommendation_crawler.py
├── metadata_extractor.py
└── README.md
```

---

## 🚀 Key Capabilities

- Automated YouTube recommendation crawling
- Recursive link expansion
- Structured metadata extraction
- Safe SQL insertion using parameterized queries
- Lightweight relational storage
- Modular pipeline architecture

---

## 📊 Potential Extensions

- Duplicate filtering with UNIQUE constraints
- Recommendation graph visualization
- Sentiment analysis on descriptions/comments
- Export to CSV or BI tools
- Network analysis of video relationships

---

## 📌 Conclusion

This project demonstrates:

- Web automation using Selenium
- API-level metadata extraction via yt-dlp
- Database schema design and structured storage
- Modular pipeline development
- End-to-end data engineering workflow

The system converts dynamic web recommendations into structured, queryable analytical data.
