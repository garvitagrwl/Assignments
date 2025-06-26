import pandas as pd

# 1
a = [12, 10, 15]
s = pd.Series(a, index=['a', 'b', 'c'])
print("Series from List:")
print(s)

#2
score = {"day1": 39, "day2": 31, "day3": 9}
v = pd.Series(score, dtype=float)
print("\nSeries from Dictionary:")
print(v)

# 3
v = pd.Series(score, dtype=float, index=["day1", "day3"])
print("\nSeries with selected indices:")
print(v)


f = v.tolist()
print(f"\nConverted to list: {f} and data type: {type(f)}")
