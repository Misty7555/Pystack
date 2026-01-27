import matplotlib.pyplot as plt
departments = ['Emergency', 'ICU', 'Pediatrics', 'Orthopedics', 'Medicine']
patients = [45, 20, 30, 25, 40]
plt.barh(departments, patients)
plt.xlabel('Number of Patients')
plt.ylabel('Departments')
plt.title('Hospital Admissions')
plt.show()