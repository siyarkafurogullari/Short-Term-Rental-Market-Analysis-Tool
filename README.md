# Short-Term Rental Analysis Tool — Quick Start Guide

## Installation
```bash
pip install -r requirements.txt
streamlit run app.py
```
It opens automatically in your browser (typically at `http://localhost:8501`).

## Usage
1. Download Inside Airbnb data for your target city: http://insideairbnb.com/get-the-data/
   - `listings.csv.gz`
   - `calendar.csv.gz`
2. Upload these two files to the application (you can upload them directly in `.gz` format as the code extracts them automatically—try uploading directly without extracting to CSV, and extract via `gunzip` only if you encounter an issue).
3. Adjust the room type and minimum listing count filters from the sidebar.

## How to Turn This Tool into Sales
1. Select a city, run the dashboard, and take screenshots or record a short screen capture.
2. Send the following outreach message to local host Facebook groups or short-term rental management accounts on Instagram:

   > "I looked into the pricing and occupancy trends for hosts in [City] and put together a free, neighborhood-specific analysis. It highlights potential missed revenue opportunities—would you like me to send it over?"

3. Walk interested hosts through the demo and highlight the "missed revenue" figures.
4. Pricing structure:
   - One-time analysis report: $150–250 (for early clients)
   - Monthly pricing optimization subscription: $50–100/month (recurring revenue)

## Notes
- The `estimated_occupancy_l365d` and `estimated_revenue_l365d` fields come from Inside Airbnb's proprietary estimation model; they are not 100% exact, but they provide consistent benchmark comparisons.
- The "unavailable" rate in the calendar file includes both confirmed bookings and days manually blocked by the host—it serves as an approximate proxy for seasonality, so be sure to disclose this when presenting to clients.
