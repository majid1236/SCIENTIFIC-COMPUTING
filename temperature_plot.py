import matplotlib.pyplot as plt

temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

plt.plot(days, temperatures, marker='o', color='blue')
plt.title("Weekly Temperature Readings")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
