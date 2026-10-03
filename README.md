<div align="center">

# 🏡 Short-Term Rental Market Analysis Dashboard
*(Kısa Süreli Kiralama Pazar Analizi Aracı)*

**A data-driven web application designed to analyze local short-term rental markets (e.g., Airbnb), optimize pricing strategies, and uncover missed revenue opportunities for property hosts.**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Built to transform raw open-source data into actionable B2B sales strategies and financial insights.*

</div>

---

## 📖 About the Project

Property managers and local hosts often struggle to price their listings competitively, leading to significant missed revenue. This tool utilizes public data from **Inside Airbnb** to provide neighborhood-specific market insights, occupancy trends, and pricing optimizations. 

It is not just an analytical dashboard; it is a **business development tool** designed to generate leads and offer data-as-a-service (DaaS) to short-term rental management companies.

---

## ✨ Key Features

- 📊 **Dynamic Data Processing:** Seamlessly processes raw `.csv.gz` files directly—no manual extraction required.
- 🎯 **Advanced Filtering:** Granular control over room types and minimum listing counts to filter out outliers.
- 💰 **Revenue Estimation:** Benchmarks properties against local competitors to highlight potential missed revenue.
- 📅 **Seasonality Tracking:** Uses calendar availability metrics as a proxy to identify high and low demand seasons.

---

## 🗂️ Example Data: How to Test the App?

To test the live dashboard, you need to download raw data for a specific city. 

1. Go to the open-source data provider: **[Inside Airbnb - Get the Data](http://insideairbnb.com/get-the-data/)**
2. Scroll down and find any city you want to analyze (e.g., *Istanbul, London, Paris*).
3. Download **only** these two specific files for your chosen city:
   - 📄 `listings.csv.gz`
   - 📅 `calendar.csv.gz`
4. Go to the Live Demo link and upload these files directly. *(No need to extract them; the app processes `.gz` files automatically!)*

---

## 🚀 Live Demo

You can test the application live here:
**[👉 Click here to view the Live Dashboard](https://short-term-rental-market-analysis-tool-wpcqxinpqbxhcqxdiqxh4e.streamlit.app/)**

*(Upload your desired city's data from Inside Airbnb to see the dashboard in action.)*

---

## 💻 Quick Start & Installation

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/siyarkafurogullari/Short-Term-Rental-Market-Analysis-Tool.git
cd Short-Term-Rental-Market-Analysis-Tool
