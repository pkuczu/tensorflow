
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


df = pd.read_csv('./data/processed_rides_data.csv', parse_dates=['Date Paid'], index_col='Date Paid')

# Ensure that the Date Paid column is in datetime format and set it as the index

df.index = pd.to_datetime(df.index)

df['Day of Week'] = df['Date Paid'].dt.day_name()

# Calculate the average number of rides for each day of the week
average_rides_per_day = df.groupby('Day of Week')['Number of Rides'].mean().sort_values()

# Visualize the differences in the average number of rides
plt.bar(average_rides_per_day.index, average_rides_per_day)
plt.xlabel('Day of Week')
plt.ylabel('Average Number of Rides')
plt.title('Average Number of Rides by Day of Week')

# Perform time series decomposition
result = seasonal_decompose(df['Number of Rides'], model='additive')

# Plot the original time series, trend, seasonality, and residuals
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(df['Number of Rides'], label='Original')
plt.legend(loc='upper left')
plt.title('Original Time Series')

plt.subplot(4, 1, 2)
plt.plot(result.trend, label='Trend')
plt.legend(loc='upper left')
plt.title('Trend Component')

plt.subplot(4, 1, 3)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='upper left')
plt.title('Seasonal Component')

plt.subplot(4, 1, 4)
plt.plot(result.resid, label='Residuals')
plt.legend(loc='upper left')
plt.title('Residuals')

plt.tight_layout()
plt.show()