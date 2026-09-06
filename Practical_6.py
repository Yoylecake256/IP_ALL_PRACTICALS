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
#Question_3
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix: ", m1)
print("\nAddition af rows")

for i in range(len(m1)):
    row_sum = 0
    for j in range(len(m1[i])):
        row_sum += m1[i][j]
    print(f"Sum of row {i}: {row_sum}")

print("\nAddition of columns")

for j in range(len(matrix[0])):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]
    print(f"Sum of Column {j}: {col_sum}")

#Question_4
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
result = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j] = m1[i][j] + m2[i][j]

print("Result Matrix:")
for row in result:
    for element in row:
        print(f"{element:4}", end="")
    print()

#Question_5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

print("Original Matrix: ", matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]

print("\nTransposed Matrix: ")
for row in result:
    for element in row:
        print(f"{element:4}", end="")
    print()

#Question_6
import numpy as np
m1 = np.array([[1, 2, 3], [10, 20, 30], [40, 50, 60]])
print("Custom Array")
print(m1)
print(f"Shape: {m1.shape}")      
print(f"Data Type: {m1.dtype}")

m2 = np.zeros((3, 3))
print("\nZeros Matrix")
print(m2)
print(f"Shape: {m2.shape}")
print(f"Data Type: {m2.dtype}")

m3 = np.ones((4, 2), dtype=int)
print("\nOnes Array")
print(m3)
print(f"Shape: {m3.shape}")
print(f"Data Type: {m3.dtype}")

#Question_7
import numpy as np
matrix =np.array( [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix:", matrix)

element = matrix[1, 2]
print("\nSpecific Element at (1, 2): ", element)

e_row = matrix[2, :]
print("\nEntire row: ", e_row)
sub_matrix = matrix[0:2, 0:2]
print("\nSliced 2x2 Matrix: ", sub_matrix)

#Question_8
import numpy as np

# Define two 3x3 matrices
m1 = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]
            ])

m2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
])

print("--- Matrix 1 ---\n", m1)
print("\n--- Matrix 2 ---\n", m2)

add_result = m1 + m2
print("\n1. Addition (m1 + m2):\n", add_result)

# 2. Element-wise Subtraction
sub_result = m1 - m2
print("\n2. Subtraction (m1 - m2):\n", sub_result)

# 3. Element-wise Multiplication (NOT matrix multiplication)
mul_result = m1 * m2
print("\n3. Element-wise Multiplication (m1 * m2):\n", mul_result)

# 4. Element-wise Division
div_result = m1 / m2
print("\n4. Element-wise Division (m1 / m2):\n", div_result)

# 5. Scalar Operations (Applying a single number to the entire matrix)
scalar_result = m2 * 10
print("\n5. Scalar Multiplication (m2 * 10):\n", scalar_result)


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

