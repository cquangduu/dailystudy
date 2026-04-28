# Import the NumPy library
import numpy as np

# Create the first vector wuth 3 elements
v1 = np.array([1, 2, 3])

# Create the second vector with 3 elements
v2 = np.array([4, 5, 6])

# Add the two vectors
vector_addition = v1 + v2
print("v1 + v2 =", vector_addition)

# Subtract the two vectors
vector_subtraction = v1 - v2
print("v1 - v2 =", vector_subtraction

# Calculate the dot product of the vectors 
dot_product = np.dot(v1, v2)
print(np.dot(v1, v2) =", dot_product)

# Create a 2x3 matrix
M1 = np.array([
	[1, 2, 3],
	[4, 5, 6]
])

# Print the matrix
print("M1 =")
print(M1)

# Print the shappr of the matrix
print("M1.shape =", M1.shape)
