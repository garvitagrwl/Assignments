import pandas as pd


ds = {
    'fruits': ["Apple", "Orange", "Mango"],
    'passing': [3, 4, 2]
}
data = pd.DataFrame(ds, index=["day1", "day2", "day3"])
data.columns = ["col1", "col2"]
print("Original DataFrame:")
print(data)

# 1
print("\nIterating over DataFrame rows:")
for index, row in data.iterrows():
    print(f"{index}: {row['col1']}, {row['col2']}")

# 2
d = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [8, 7, 5, 2], 'c': [1, 2, 0, 1]}, index=["r1", "r2", "r3", "r4"])
print("\nOriginal DataFrame for condition selection:")
print(d)

dp = d[d["c"] != 0]
print("\nRows where column 'c' is not 0:")
print(dp)

# 3
reversed_df = data.iloc[::-1, :]
print("\nReversed DataFrame using iloc:")
print(reversed_df)

# 4
col_only = data.loc[:, 'col1']
print("\nSelected column 'col1':")
print(col_only)

# 5. Drop rows based on condition
# Handled above using condition d["c"] != 0

# 6
modified_data = data.copy()
modified_data.iloc[1:2, :] = ['Melon', 0]
print("\nDataFrame after modifying row at index 'day2':")
print(modified_data)

# 7
selected_rows = data.loc[["day1", "day3"]]
print("\nSelected rows 'day1' and 'day3':")
print(selected_rows)
