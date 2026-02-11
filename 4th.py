import pandas as pd
import matplotlib.pyplot as plt

file1 = pd.read_csv("file1.csv")
file2 = pd.read_csv("file2.csv")

x1 = file1["x1"]
x2 = file1["x2"]
y1 = file2["y1"]
y2 = file2["y2"]

plt.plot(x1, y1, linestyle="--", label="Line 1")
plt.plot(x2, y2, linestyle="--", label="Line 2")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Dashed Line Plot")
plt.legend()

plt.show()
