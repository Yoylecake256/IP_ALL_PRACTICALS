#Question 9

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Mean: ", np.mean(arr))
print("Median: ", np.median(arr))
print("Standard Deviation: ", np.std(arr))


#Questoin 10

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print("\nOriginal Array")
print(arr)
new_arr = arr.reshape(2, 3)
print("2D Array: ")
print(new_arr)
print("Reshaped again: ")
print(arr.reshape(3, 2))

#Question 12
import numpy as np
#Student marks
marks = np.array([[85,90, 78, 88], [70, 75, 80, 85], [95, 95, 85, 91]])
print("Student Marks: ")
print(marks)

print("Avg marks per student:")
print(np.mean(marks, axis=1))

print("Highest marks")
print(np.max(marks))

print("Lowest Marks: ")
print(np.min(marks))

print("Average marks per subject: ")
print(np.mean(marks, axis=0))

