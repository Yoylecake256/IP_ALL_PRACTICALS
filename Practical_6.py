#Question_1

matrix = [["a", "b", 1], 
          ["c", "d", 2], 
          ["e", "f", 3]]
print("\nEntire matrix:")
print(matrix)
print("\nFirst Row:")
print(matrix[0])
print("\nFor element at (2, 3)")
print(matrix[1][2])

#Question_2
matrix = [
    ["a", "b"], 
    ["c", "d"], 
    ["e", "f"]
]

print("Row-wise traversal:")
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(f"Element at ({r}, {c}): {matrix[r][c]}")

matrix = [["a", "b"], 
          ["c", "d"], 
          ["e", "f"]]

print("\nColumn-wise traversal")
for i in range(len(matrix[0])): 
    for j in range(len(matrix)): 
        print(f"Element at ({j}, {i}) is: {matrix[j][i]}")


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

