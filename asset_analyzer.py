
import yfinance as yf
import pandas as pd
import numpy as np
import sqlite3


# This class handles the database stuff
class Database:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def create_table(self):
        # Connect to the database
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        # Make the table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_fn (
                period TEXT,
                ticker TEXT,
                max_price REAL,
                min_price REAL,
                average_price REAL,
                volatility REAL
            )
        """)

        connection.commit()
        return connection, cursor


# This class downloads and analyzes asset prices
class AssetAnalyzer:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        # Get stock data from Yahoo Finance
        data = yf.download(
            self.ticker,
            start=self.start_date,
            end=self.end_date
        )

        # Check if we got any data
        if data.empty:
            print(f"{self.ticker} was not found")
            return None

        # Get only the closing prices
        closing_prices = data["Close"]
        return closing_prices

    def analyze_data(self, closing_prices):
        # Find the highest and lowest prices
        max_price = np.max(closing_prices)
        min_price = np.min(closing_prices)

        # Get the average price and volatility
        average_price = np.mean(closing_prices)
        volatility = np.std(closing_prices)

        return max_price, min_price, average_price, volatility

    def save_data(self, max_price, min_price, average_price, volatility):
        # Open the database and create the table
        database = Database("my_db", "datos_fn")
        connection, cursor = database.create_table()

        # Save the date range as one string
        period = f"{self.start_date} - {self.end_date}"

        # Add the results to the database
        cursor.execute("""
            INSERT INTO datos_fn (
                period, ticker, max_price, min_price,
                average_price, volatility
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            period,
            self.ticker,
            max_price,
            min_price,
            average_price,
            volatility
        ))

        connection.commit()

        # Show all the saved data
        cursor.execute("SELECT * FROM datos_fn")
        saved_data = cursor.fetchall()

        for row in saved_data:
            print(row)

        # Close the database connection
        cursor.close()
        connection.close()


def main():
    # Pick the stock and the dates
    ticker = "TSLA"
    start_date = "2025-01-01"
    end_date = "2026-01-01"

    # Create the analyzer and download the data
    asset = AssetAnalyzer(ticker, start_date, end_date)
    data = asset.download_data()

    # Analyze and save the data if we got some
    if data is not None:
        max_price, min_price, average_price, volatility = (
            asset.analyze_data(data)
        )

        asset.save_data(
            round(max_price, 2),
            round(min_price, 2),
            round(average_price, 2),
            round(volatility, 2)
        )
    else:
        print("No data to analyze")


# Run the program
if __name__ == "__main__":
    main()
