
Asset Analyzer

A high-performance quantitative financial analysis web application built to process market data, compute risk metrics, and maintain local data persistence.

Features

• Data Retrieval: Integrated with Yahoo Finance API to pull historical closing prices.
• Vectorized Engine: Utilizes NumPy for high-speed mathematical computations.
• Statistical Analytics: Computes maximum, minimum, average, and annualized volatility.
• Data Persistence: Structures storage and logs analytical history using SQLite3.
• Modern Interface: Powered by Streamlit with asynchronous progress trackers.

Tech Stack

• Python
• SQLite3
• NumPy
• yfinance API
• Streamlit

Core Modularity

1. download_data: Downloads and flattens market data frames into continuous raw arrays.
2. calculate_statistics: Executes matrix mathematical operations via NumPy vectorization.
3. insert_data: Maps and saves variables into the relational SQLite3 schema.

Installation and Execution

bash
git clone https://github.com
cd streamlit-asset-anlyzer
pip install -r requirements.txt
streamlit run app.py
