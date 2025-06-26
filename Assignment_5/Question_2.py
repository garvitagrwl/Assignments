import pandas as pd
# 1
ds = {
    'fruits': ["Apple", "Orange", "Mango"],
    'passing': [3, 4, 2]
}
data = pd.DataFrame(ds)
data.columns = ["col1", "col2"]
print("DataFrame from dictionary:")
print(data)

# 2
data_list = [["Apple", 3], ["Orange", 4], ["Mango", 2]]
df_list = pd.DataFrame(data_list, columns=["col1", "col2"])
print("\nDataFrame from list of lists:")
print(df_list)

# 3
data_tuples = [("Apple", 3), ("Orange", 4), ("Mango", 2)]
df_tuples = pd.DataFrame(data_tuples, columns=["col1", "col2"])
print("\nDataFrame from list of tuples:")
print(df_tuples)

# 4
data_dicts = [{"col1": "Apple", "col2": 3}, {"col1": "Orange", "col2": 4}, {"col1": "Mango", "col2": 2}]
df_dicts = pd.DataFrame(data_dicts)
print("\nDataFrame from list of dicts:")
print(df_dicts)
