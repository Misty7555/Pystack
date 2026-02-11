import pandas as pd
import matplotlib.pyplot as plt

country = pd.read_csv("Country.csv")
population = pd.read_csv("Population.csv")

plt.bar(
    country["Country"],
    population["Population"],
    width=0.6,
    color="skyblue"
)

for i, val in enumerate(population["Population"]):
    plt.text(i, val, str(val), ha="center", va="bottom")

plt.xlabel("Country")
plt.ylabel("Population (in millions)")
plt.title("Country-wise Population")

plt.show()