import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
import matplotlib.pyplot as plt

# Quadratic equation
temperature = 20.0
pressure = 800.0
humidity = 79.0

# Quadratic equation coefficients
a = 0.01
b = -0.5
c = 25

# Calculate weather parameter (e.g., precipitation)
precipitation = a * temperature**2 + b * humidity + c
temperatures=range(0,101)
# Print result
print(f"Precipitation: {precipitation}")

# Plotting the precipitation values
plt.figure(figsize=(8, 6))
plt.bar(temperatures, precipitation_v, color='blue', alpha=0.7)
plt.title('Precipitation vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Precipitation')
plt.grid(True)
plt.show()


