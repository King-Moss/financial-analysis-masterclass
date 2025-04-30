import pandas as pd
import yfinance as yf
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

# Select your stock tickers
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Define date range (last 5 years)
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=365*5)

# Download the stock data
df = yf.download(tickers, start=start_date, end=end_date)

# Use only the 'Close' prices
price_df = df['Close']

# Calculate daily log returns
log_returns = np.log(price_df / price_df.shift(1))

# Calculate cumulative log returns
cumulative_log_returns = log_returns.cumsum()

# Plot the cumulative returns
cumulative_log_returns.plot(title="Cumulative Returns Over 5 Years", figsize=(10, 6))
plt.xlabel("Date")
plt.ylabel("Cumulative Log Return")
plt.grid(True)
plt.tight_layout()

# Save and show the chart
plt.savefig("images/cumulative_returns.png")
plt.show()
