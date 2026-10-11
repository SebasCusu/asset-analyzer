from datetime import datetime
import yfinance as yf
import streamlit as st
import sqlite3
import numpy as np
import time

# Configure the Streamlit page layout and appearance
st.set_page_config(
    page_title="Asset Analyzer",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Connect to the SQLite database
# check_same_thread=False allows the connection to be used across threads
conn = sqlite3.connect(
    "asset_analyzer_db",
    check_same_thread=False
)
cur = conn.cursor()

# Create the database table if it does not already exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS app_db (
        ticker TEXT NOT NULL,
        date TEXT NOT NULL,
        high REAL NOT NULL,
        low REAL NOT NULL,
        average REAL NOT NULL,
        volatility REAL NOT NULL
    )
""")
conn.commit()


# Backend functions

def download_data(ticker, start_date, end_date):
    """Download historical closing prices for a financial asset."""
    try:
        # Retrieve historical market data from Yahoo Finance
        data = yf.download(
            ticker,
            start=start_date,
            end=end_date
        )

        # Return None if no data is available
        if data.empty:
            return None

        # Extract valid closing prices and convert them into a flat array
        closing_prices = data["Close"].dropna().values.flatten()

        return closing_prices

    except Exception:
        # Return None if the download fails
        return None


def calculate_statistics(prices):
    """Calculate the main statistics for the asset prices."""

    # Round prices to two decimal places
    rounded_prices = np.round(prices, 2)

    # Calculate the maximum, minimum, average, and standard deviation
    maximum = float(np.max(rounded_prices))
    minimum = float(np.min(rounded_prices))
    average = float(np.mean(rounded_prices))
    volatility = float(np.std(rounded_prices))

    return maximum, minimum, average, volatility


def insert_data(ticker, date, maximum, minimum, average, volatility):
    """Save the calculated statistics in the SQLite database."""

    # Use parameterized SQL to safely insert the values
    cur.execute(
        """
        INSERT INTO app_db
            (ticker, date, high, low, average, volatility)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (ticker, date, maximum, minimum, average, volatility)
    )

    # Save the changes to the database
    conn.commit()


# Main Streamlit interface

def main():

    # Display the application title and subtitle
    st.title("📈 Asset Analyzer")

    st.markdown(
        "<p style='color: #8E8E93; font-size: 1.1rem; "
        "margin-top: -15px;'>Financial Terminal</p>",
        unsafe_allow_html=True
    )

    st.write("---")

    # Create a container for the asset configuration inputs
    with st.container(border=True):

        st.markdown("**⚙️ Asset Configuration**")

        # Ask the user for a stock or cryptocurrency ticker
        ticker = st.text_input(
            "Ticker Symbol",
            value="AAPL",
            placeholder="e.g., AAPL, BTC-USD"
        ).upper().strip()

        # Place the start and end date inputs side by side
        col_start_date, col_end_date = st.columns(2)

        with col_start_date:
            start_date = st.text_input(
                "Start Date",
                value="2026-01-01",
                placeholder="YYYY-MM-DD"
            )

        with col_end_date:
            end_date = st.text_input(
                "End Date",
                value="2026-10-01",
                placeholder="YYYY-MM-DD"
            )

        # Run the analysis when the button is clicked
        run_analysis = st.button(
            "Run Analysis",
            type="primary",
            use_container_width=True
        )

    # Execute the analysis only after the user clicks the button
    if run_analysis:

        # Record the current date for the database entry
        analysis_date = datetime.now().strftime("%Y-%m-%d")

        # Display a loading message while retrieving financial data
        with st.spinner("Connecting to financial servers..."):

            # Download the asset's historical closing prices
            prices = download_data(
                ticker,
                start_date,
                end_date
            )

            # Continue only if valid price data was returned
            if prices is not None and len(prices) > 0:

                # Calculate the asset's main statistical metrics
                maximum, minimum, average, volatility = (
                    calculate_statistics(prices)
                )

                # Save the analysis results in the SQLite database
                insert_data(
                    ticker,
                    analysis_date,
                    maximum,
                    minimum,
                    average,
                    volatility
                )

                # Notify the user that the results were saved
                st.toast(
                    f"Metrics for {ticker} saved successfully",
                    icon="⚡"
                )

                # Display the analysis results and price chart
                st.markdown("### 📊 Analysis Results")

                st.line_chart(prices)

                # Display the calculated metrics in four columns
                metric_1, metric_2, metric_3, metric_4 = st.columns(4)

                metric_1.metric(
                    label="Maximum",
                    value=f"${maximum:,.2f}"
                )

                metric_2.metric(
                    label="Minimum",
                    value=f"${minimum:,.2f}"
                )

                metric_3.metric(
                    label="Average",
                    value=f"${average:,.2f}"
                )

                metric_4.metric(
                    label="Volatility",
                    value=f"{volatility:.2f}"
                )

                # Display the previously saved analysis history
                st.write("")
                st.markdown("### 🗄️ Analysis History (`app_db`)")

                # Retrieve the most recent database entries first
                cur.execute(
                    "SELECT * FROM app_db ORDER BY rowid DESC"
                )
                database_records = cur.fetchall()

                # Show the database records in an interactive table
                st.dataframe(
                    database_records,
                    column_config={
                        "0": "Ticker",
                        "1": "Analysis Date",
                        "2": "Maximum",
                        "3": "Minimum",
                        "4": "Average",
                        "5": "Volatility"
                    },
                    use_container_width=True
                )

            else:
                # Inform the user if the download or analysis fails
                st.error(
                    f"❌ Unable to retrieve or process ticker: {ticker}. "
                    "Check the ticker symbol and date range."
                )


# Start the application when this file is executed directly
if __name__ == "__main__":
    main()