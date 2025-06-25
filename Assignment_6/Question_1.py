import pandas as pd

# Convert a list of date strings to datetime (timeseries)
date_series = ["2025-06-20", "2025-07-02", "2025-05-02", "2025-04-02"]
datetime_series = pd.to_datetime(date_series)
print("Converted Time Series:")
print(datetime_series)
