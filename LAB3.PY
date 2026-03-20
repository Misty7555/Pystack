import pandas as pd
data = pd.Series([10, 60, 30, 80, 45, 29, 50, 103, 49])
data[data > 50] = 50
print("Updated Series:")
print(data)
