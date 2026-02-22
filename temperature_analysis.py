# Task 1
import numpy as np
temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32

print(f"Temperatute in Celsius : {temps_celsius}")
print(f"Temperature in Fahrenheit : {temps_fahrenheit}")
print(f"Average temperature (Fahrenheit) : {np.mean(temps_fahrenheit):.1f}")
print("\n")

# Task 2
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print(f"Shape : {scores.shape}")
print(f"Total elements : {scores.size}")
print(f"Highest Score : {np.max(scores)}")
print(f"Lowest score : {np.min(scores)}")
print(f"Range: {np.max(scores) - np.min(scores)}")
print("\n")

# Task 3
import time
numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

# Python List Summation
start = time.time()
python_sum = sum(python_list)
list_time = time.time() - start

# Numpy array summation
start = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start

print(f"Numpy sum : {numpy_sum}")
print(f"Python sum : {python_sum}")
print(f"Numpy time : {numpy_time}")
print(f"Python time : {list_time}")
print(f"Numpy is {list_time/numpy_time}x faster")