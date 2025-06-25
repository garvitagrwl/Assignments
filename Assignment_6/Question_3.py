import pandas as pd
df1 = pd.DataFrame({
    'Name': ['a', 'b'],
    'Subject': ['sub1', 'sub2'],
    'marks': [23, 45],
    'id': [1, 2]
})

df2 = pd.DataFrame({
    'Name': ['c', 'd'],
    'Subject': ['sub3', 'sub4'],
    'marks': [56, 78],
    'id': [3, 4]
})

df3 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Grade': ['A', 'B', 'A', 'C']
})

# Vertical concatenation of df1 and df2
combined_df = pd.concat([df1, df2], axis=0)
print("\n--- Vertically Concatenated DataFrame ---")
print(combined_df)

#  Mergeing
merged_result = combined_df.merge(df3, on='id', how='left')
print("\n--- Merged with Third DataFrame on 'id' ---")
print(merged_result)    
