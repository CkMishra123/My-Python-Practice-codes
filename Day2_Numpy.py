#1.Array Creation and reshaping:Create a 1D array from 1 to 20 and reshape it into a 4×5 matrix. Then:-(a)Extract the 2nd row (b)Extract the last column
import numpy as np
arr=np.arange(1,21)
print(arr)
#Reshaping the above 1D array
y=arr.reshape(4,5)
print(y)
#Extract 2nd row
print(y[1,:])
#Extracting last column
print(y[-1])


#2.Boolean Indexing: Given an array of random integers (1–50, size 15):Print elements greater than 25 ,Replace elements less than 10 with 0
import numpy as np
arr1=np.arange(1,50,15)
print(arr1)
#Printing element>25
print(arr1[arr1>25])
#Replace elements less than 10 with 0
x=10
new_arr=np.where(arr1<x,0,arr1)
print(new_arr)


#3.Broadcasting concept: Create two arrays and Add using broadcasting ,explain the output shape
import numpy as np
A = np.array([1, 2, 3])
B = np.array([[10], [20], [30]])
#Add A and B using broadcasting
print(A+B)
#Output shape
print(np.shape(A+B))


#4.Row-wise & Column-wise Operations:Create a 5×5 random matrix:(a)Find row-wise mean(b)Find column-wise maximum(c)Normalize each row (value / row sum)
import numpy as np
# Initialize the generator with a fixed seed (e.g., 42)
rng = np.random.default_rng(seed=42)
# Generate a 5*5 matrix of random floats between 0 and 1
matrix = rng.random((5, 5))
print(matrix)
#Finding row wi
se mean
y=

#5.Sorting and Unique: Sort the array,Find unique elements,Count frequency of each unique value
import numpy as np
arr = np.array([5, 2, 8, 2, 9, 1, 5, 3])
#sorting the array
print(np.sort(arr))
#finding the unique element
x=np.unique(arr)
print(x)
#Counting the frequency of each unique value
print(np.unique(x, return_counts=True))


#6.Matrix Multiplication & Determinant: Create two 3×3 matrices:Perform matrix multiplication,Find determinant of each,Check if inverse exists
import numpy as np
x=np.random.rand(3,3)
y=np.random.rand(3,3)
print("The 1st ,2nd and Multiplication of the both matrix is given respectively: ",x,y, x*y)
#Finding determinant of each
print("The determinant of First matrix is : ",np.linalg.det(x))
print("The determinant of Second matrix is : ", np.linalg.det(y))
print("The determinant of Multiplication of those both matrix is : ",np.linalg.det(x*y))
#Checking inverse
print("The inverse of first matrix is : ", np.linalg.inv(x))
print("The inverse of Second matrix is : ", np.linalg.inv(y))
print("The inverse of Multiplication matrix is : ", np.linalg.inv(x*y))
















