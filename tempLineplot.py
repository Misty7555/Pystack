import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
city_a = [30, 32, 31, 33, 34, 35, 36]
city_b = [25, 26, 27, 28, 29, 30, 31]
plt.plot(days, city_a, label='City A')
plt.plot(days, city_b, label='City B')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Weekly Temperature Variation')
plt.legend()
plt.grid()
plt.show()