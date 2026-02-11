import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("MelaSales.csv")

days = data["Day"]
sales = data["Week 1"]
colors = ["red", "yellow", "purple", "red", "yellow", "purple", "red"]
plt.bar(
    days,
    sales,
    color=colors,
    edgecolor="green",
    linewidth=2,
    linestyle="--"
)

plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Day-wise Sales Bar Plot")

plt.show()
