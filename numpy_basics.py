import numpy as np


arr1 = np.array([1, 2, 3])
print("1D Aray:",arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n",arr2)

zeros = np.zeros((2, 3))
print("Zeros Array:\n",zeros)

ones = np.ones((2, 3))
print("Ones Array:\n",ones)

range_arr = np.arange(0, 10, 2)
print("Range Array:",range_arr)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\na + b =", a + b)
print("a*b =", a * b)

print("Mean of a:", np.mean(a))
print("Sum of a:", np.sum(a))


reshaped = np.arange(1, 13).reshape(3, 4)
print("Reshaped Array (3x4):\n", reshaped)