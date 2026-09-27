Financial Asset Data Analyzer

A Python program that downloads historical financial asset prices using Yahoo Finance
 and calculates basic statistics such as the maximum price, minimum price, average price, and volatility.

Features

Download historical financial data using yfinance.

Search for assets using their ticker symbol.

Specify a custom start and end date.

Calculate:

Maximum price

Minimum price

Average price

Price volatility

Display the results directly in the terminal.

Requirements

Python 3.8 or higher

NumPy

yfinance

Installation

Clone the repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository


Install the required dependencies:

pip install numpy yfinance

Usage

Run the program with:

python main.py


The program will ask for three inputs:

Enter the Ticker you want to search for: AAPL
Enter the Start Date: 2024-01-01
Enter the End Date: 2024-12-31


The program will then display the calculated statistics:

Max Price: 237.49 USD
Min Price: 164.08 USD
Average Price: 196.23 USD
Volatility: 15.42%

Functions
get_yf_data(ticker, start_date, end_date)

Downloads the historical closing prices of a financial asset from Yahoo Finance.

Parameters:

ticker (str): Asset ticker symbol, such as AAPL, MSFT, or TSLA.

start_date (str): Start date.

end_date (str): End date.

Returns:

np.ndarray: Array containing the closing prices.

None: If no prices are found.

extract_data(prices)

Calculates basic statistics from the downloaded prices.

Returns:

maximum price
minimum price
average price
standard deviation

main()

Handles user input, downloads the data, calculates the statistics, and displays the results.

Example Tickers

Some examples of ticker symbols you can use:

AAPL — Apple

MSFT — Microsoft

GOOGL — Alphabet

TSLA — Tesla

AMZN — Amazon

Technologies

Python

NumPy

yfinance

Yahoo Finance API

Disclaimer

This project is intended for educational purposes only. The information obtained from Yahoo Finance should not be considered financial advice.
