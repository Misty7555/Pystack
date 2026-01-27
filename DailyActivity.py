import matplotlib.pyplot as plt
activities = ['Study', 'Sleep', 'Exercise', 'Leisure', 'Others']
hours = [6, 8, 1, 5, 4]
plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title('Daily Activities Distribution')
plt.legend()
plt.show()
