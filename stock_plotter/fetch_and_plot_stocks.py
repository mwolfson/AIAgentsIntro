# filename: fetch_and_plot_stocks.py
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    # Fetch data from start of 2024 until today
    data = stock.history(start="2024-01-01", end="2024-08-23")
    return data['Close']

def calculate_ytd_gains(data):
    # Calculate gains as percentage from the first day of the year
    return 100 * (data / data.iloc[0] - 1)

# Fetching data
nvda_data = fetch_stock_data("NVDA")
tsla_data = fetch_stock_data("TSLA")

# Calculating YTD gains
nvda_gains = calculate_ytd_gains(nvda_data)
tsla_gains = calculate_ytd_gains(tsla_data)

# Create plot
plt.figure(figsize=(10, 5))
plt.plot(nvda_gains, label='NVDA YTD Gains %')
plt.plot(tsla_gains, label='TSLA YTD Gains %')
plt.title('NVDA and TSLA Stock Gains YTD 2024')
plt.xlabel('Date')
plt.ylabel('Gain %')
plt.legend()
plt.grid(True)

# Save to file
plt.savefig('ytd_stock_gains.png')
plt.show()