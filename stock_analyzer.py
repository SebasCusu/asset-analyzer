import numpy as np
import yfinance as yf

def get_yf_data(ticker, start_date, end_date):
    """
    Downloads data for the specified financial asset using its Ticker, between the start and end dates.
    

    ticker (str): The Ticker of the financial asset.
    start_date (str): The start date in date format.
    end_date (str): The end date in date format.
        
    Returns:
        np.ndarray: The prices of the financial asset during the specified period, or None if the asset is not found.
    """
    ticker_data = yf.download(ticker, start=start_date, end=end_date)
    prices = ticker_data['Close'].values
    if not prices.any():
        return None
    else:
        return prices

def extract_data(prices):
    """
    returns the maximum, minimum, average, and volatility of the asset
    
    Args:
        prices (np.ndarray): The prices of the financial asset.
        
    Returns:
        Tuple: The maximum, minimum, average, and volatility of asset
    """
    max_price = np.max(prices)
    min_price = np.min(prices)
    avg_price = np.mean(prices)
    price_volatility = np.std(prices)
    return max_price, min_price, avg_price, price_volatility

def main():
    """
    Main function that allows the user to search for information about a specific financial asset.
    """
    ticker = input("Enter the Ticker you want to search for: ").strip().upper()
    start_date = input("Enter the Start Date: ")
    end_date = input("Enter the End Date: ")
    data = get_yf_data(ticker, start_date, end_date)

    max_price, min_price, avg_price, price_volatility = extract_data(data)
    
    if data is None:
        print("Financial Asset not found")
    else:
        print(f"Max Price: {max_price:.2f} USD")
        print(f"Min Price: {min_price:.2f} USD")
        print(f"Average Price: {round(avg_price,2):.2f} USD")
        print(f"Volatility: {price_volatility:.2f}%")

if __name__ == "__main__":
    main()