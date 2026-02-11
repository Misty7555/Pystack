import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("performance.csv")

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(data["Month"], data["Attendance"], marker='o')
plt.title("Attendance vs Month")
plt.xlabel("Month")
plt.ylabel("Attendance")

plt.subplot(2, 2, 2)
plt.bar(data["Month"], data["Marks"])
plt.title("Marks vs Month")
plt.xlabel("Month")
plt.ylabel("Marks")

plt.subplot(2, 2, 3)
plt.scatter(data["Month"], data["StudyHours"])
plt.title("Study Hours vs Month")
plt.xlabel("Month")
plt.ylabel("Study Hours")

plt.subplot(2, 2, 4)
plt.hist(data["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
