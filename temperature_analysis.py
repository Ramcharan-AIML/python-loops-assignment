# Task -1
# Requirements:

# Create a NumPy array called temps_celsius with these values
# Convert all temperatures to Fahrenheit using: F = C × 1.8 + 32
# Print both Celsius and Fahrenheit arrays
# Calculate the average temperature in Fahrenheit

import numpy as np

temps_celsius = np.array([22,25,28,24,26])

# F = C * 1.8 + 32

F = temps_celsius * 1.8 + 32

average_fah = np.mean(F)

print("Celsius :- ",temps_celsius)
print("Fahrenheit :- ",F)
print("Average Fahrenheit :- ",average_fah)
print("-" * 45)




