import pandas as pd

numbers = pd.Series(range(1, 11))
even_numbers = numbers[numbers % 2 == 0]

print("Even Numbers:")
print(even_numbers)
