import pandas as pd


df = pd.read_csv('industry_sample.csv')

print("🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Info:")
print(df.info())

print("\n🔹 Description:")
print(df.describe())

print("\n🔹 Shape of the Data:")
print(df.shape)

print("\n🔹 Column Names:")
print(df.columns)
c_df = df.copy()
c_df['Employees'] = c_df['Employees'].fillna(c_df['Employees'].mean())
c_df['Revenue'] = c_df['Revenue'].fillna(c_df['Revenue'].mean())
c_df.dropna(subset=['Industry'], inplace=True)


print("\n🔹 Industry Count:")
print(c_df['Industry'].value_counts())


print("\n🔹 Grouped Industry Stats:")
print(c_df.groupby('Industry').agg({
    'Employees': 'mean',
    'Revenue': ['sum', 'mean']
}))


print("\n🔹 Top Industries by Revenue:")
print(c_df.sort_values(by='Revenue', ascending=False).head())
