import matplotlib.pyplot as plt
exam_scores = [45, 50, 55, 60, 65, 70, 72, 75, 78, 80, 85, 90, 95]
plt.hist(exam_scores, bins=5)
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Exam Score Distribution')
plt.show()