import pandas as pd

df = pd.read_csv('./data/dates.csv')

df['Date Paid'] = pd.to_datetime(df['Date Paid'], format='%m/%d/%Y')

rides_per_date = df.groupby('Date Paid').size().reset_index(name='Number of Rides')
rides_per_date.to_csv('processed_rides_data.csv', index=False)

print(rides_per_date)