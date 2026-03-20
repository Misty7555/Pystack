import pandas as pd
data_dict = {
    'Name': ['Amit', 'Riya', 'John'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 88]
}
df = pd.DataFrame(data_dict)
print("First two rows:")
print(df.head(2))
print("Last row:")
print(df.tail(1))