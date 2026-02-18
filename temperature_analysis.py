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



# Task - 2
# Requirements:

# Print the shape of this array
# Find the total number of elements in the array
# Calculate the highest score
# Calculate the lowest score
# Calculate the range (difference between highest and lowest)

arr = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape :- ",arr.shape)
print("Total Number of Elements :- ",arr.size)
print("Highest Score :- ",np.max(arr))
print("Lowest Score :- ",np.min(arr))
print("Range :- ",np.max(arr) - np.min(arr))
print("-" * 45)




# Task 3: Performance Comparison
# Problem: Compare NumPy array performance against Python lists for a simple calculation.

# Requirements:

# Create a NumPy array with numbers from 1 to 50000 using np.arange(1, 50001)
# Create a Python list with the same numbers using list(range(1, 50001))
# Calculate the sum using NumPy's np.sum()
# Calculate the sum using Python's sum()
# Measure and print the time taken for both operations
# Calculate how many times faster NumPy is
import time

num_arr = np.arange(1, 50001)
pyt_lst = list(range(1, 50001))

# NumPy timing
start_time = time.time()
np_sum = np.sum(num_arr)
numpy_time = time.time() - start_time

print("Time taken by NumPy :", numpy_time)

# Python timing
start_time = time.time()
py_sum = sum(pyt_lst)
python_time = time.time() - start_time

print("Time taken by Python :", python_time)


speed = python_time / numpy_time
print("NumPy is faster than Python by", speed, "times")
