import pandas as pd


df = pd.DataFrame({
    'Name': ['a', 'b', 'c', 'd'],
    'Subject': ['sub1', 'sub2', 'sub3', 'sub4'],
    'marks': [23, 45, 56, 78],
    'Section': ['A', 'B', 'C', 'D'],
    'id': [1, 2, 3, 4]
}, index=[1, 2, 3, 4])

da = pd.DataFrame({
    'Name': ['e', 'f', 'g', 'h'],
    'Subject': ['sub1', 'sub2', 'sub3', 'sub4'],
    'marks': [32, 60, 68, 89],
    'Section': ['A', 'B', 'C', 'D'],
    'id': [1, 6, 3, 5]
}, index=[1, 2, 3, 4])

# a) Inner Merge on 'id'
inner_result = df.merge(da, on='id')
print("\n--- Inner Merge on 'id' ---")
print(inner_result)

# b Left Join on 'id'
left_result = df.merge(da, on='id', how='left')
print("\n--- Left Join on 'id' ---")
print(left_result)

# c) Right Join on 'id'
right_result = df.merge(da, on='id', how='right')
print("\n--- Right Join on 'id' ---")
print(right_result)

# d Merge on multiple keys
multi_key_result = df.merge(da, on=['id', 'Section'])
print("\n--- Merge on Multiple Keys ['id', 'Section'] ---")
print(multi_key_result)

#  Index based join using join()
join_result = df.join(da, rsuffix='_da', lsuffix='_df')
print("\n--- Index-Based Join using join() ---")
print(join_result)
