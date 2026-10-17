import yfinance as yf
import numpy as np
import sqlite3

conn = sqlite3.connect('my_db')
cur = conn.cursor()

# Initialize database table to store calculated asset metrics
cur.execute('''
    CREATE TABLE IF NOT EXISTS ticker_data (
        ticker TEXT,
        maximum REAL,
        minimum REAL,
        average REAL,
        volatility REAL
    )
''')
conn.commit()

class Asset:
    # Represents a financial asset and manages its data workflow
    def __init__(self, name):
        self.name = name
    
    def download_data(self, start_date: str, end_date: str):
        data = yf.download(self.name, start=start_date, end=end_date)
        if data.empty:
            return None
        
        else:
            # Extract closing prices and flatten into a 1D array
            closing_prices = data["Close"].to_numpy().flatten()
            return closing_prices
        
    def analyze_data(self, prices):
        # Compute key statistical metrics from the price series
        maximum = np.max(prices)
        minimum = np.min(prices)
        average = np.mean(prices)
        volatility = np.std(prices)
        return maximum, minimum, average, volatility
    
    def insert_data(self, maximum, minimum, average, volatility):
        # Save rounded metrics into the SQLite database
        cur.execute('''INSERT INTO ticker_data
                    (ticker, maximum, minimum, average, volatility) VALUES (?, ?, ?, ?, ?)''',
                    (self.name, round(maximum, 2), round(minimum, 2), round(average, 2), round(volatility, 2)))
        conn.commit()
        
    def view_data(self):
        # Query and display all records currently stored in the database
        content = cur.execute('SELECT * FROM ticker_data')
        if not content:
            print("No data available")
        else:
            records = content.fetchall()
            for record in records:
                print(record)
                

def main():
    asset1 = Asset("BTC-USD")
    prices = asset1.download_data("2025-1-1", "2026-1-1")
    if prices is not None:
        data = asset1.analyze_data(prices)
        maximum, minimum, average, volatility = data
        asset1.insert_data(maximum, minimum, average, volatility)
        print(asset1.view_data())

    else:
        print("There was an error")

if __name__ == "__main__":
    main()