# Ride Requests Analysis

This repository contains data and scripts for analyzing ride requests per day. The dataset includes information about the date and the number of ride requests on each day.

## Data Format

The data is stored in a CSV file with the following format:

- `Date Paid`: Date of the ride request.
- `Number of Rides`: The number of ride requests on that particular day.

## Dependencies

- Python 3.x
- pandas
- matplotlib

Install the required dependencies using:

bash

pip install pandas matplotlib
Usage
Clone the repository:
bash
Copy code
cd ride-requests-analysis
Run the analysis script:
bash
Copy code
python analyze_rides.py
This script performs time series decomposition and analyzes patterns in the ride request data, considering factors such as trend, seasonality, and day of the week.

Results
The analysis results are visualized and provide insights into the patterns and trends in ride requests over time.
