import pandas as pd


df = pd.DataFrame({
    'date': pd.date_range(start='2024-12-25', periods=10, freq='D'),
    'sales': [200, 250, 180, 300, 270, 320, 210, 230, 310, 290]
})

print("Original Data:")
print(df)


df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()


df['custom_date'] = pd.to_datetime(['2024-12-25', '2024-12-26', '2024-12-27',
                                    '2024-12-28', '2024-12-29', '2024-12-30',
                                    '2024-12-31', '2025-01-01', '2025-01-02', '2025-01-03'])



weekend_sales = df[df['weekday'].isin(['Saturday', 'Sunday'])]


# results
print("\nData with datetime extraction and operations:")
print(df.reset_index())

print("\nWeekend Sales (Saturday/Sunday):")
print(weekend_sales)


