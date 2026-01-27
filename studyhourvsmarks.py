import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [40, 50, 60, 68, 75, 85, 92]
plt.scatter(study_hours, marks)
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study Hours vs Marks')
plt.show()