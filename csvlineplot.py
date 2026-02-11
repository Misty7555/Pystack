import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Sales.csv")
plt.plot(
    data["Month"],
    data["Product_A"],
    linestyle='-',
    marker='o',
    label="Product A"
)
plt.plot(
    data["Month"],
    data["Product_B"],
    linestyle='--',
    marker='s',
    label="Product B"
)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales of Two Products")
plt.legend()
plt.show()
