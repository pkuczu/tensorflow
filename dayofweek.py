import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


df = pd.read_csv('./data/processed_rides_data.csv')

print(df.dtypes)

# Check if the date column is present in the DataFrame
if 'Date Paid' in df.columns:
    # Convert the 'Date Paid' column to datetime
    df['Date Paid'] = pd.to_datetime(df['Date Paid'])

    # Add a new column 'Day of Week'
    df['Day of Week'] = df['Date Paid'].dt.day_name()

    # Calculate the average number of rides for each day of the week
    average_rides_per_day = df.groupby('Day of Week')['Number of Rides'].mean().sort_values()

    # Visualize the differences in the average number of rides
    plt.bar(average_rides_per_day.index, average_rides_per_day)
    plt.xlabel('Day of Week')
    plt.ylabel('Average Number of Rides')
    plt.title('Average Number of Rides by Day of Week')
    plt.show()
else:
    print("Error: 'Date Paid' column not found in the DataFrame.")