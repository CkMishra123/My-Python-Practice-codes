#1.Create a 1D NumPy array of numbers from 1 to 10.Find its shape, ndim, and dtype.
import numpy as np
data=np.arange(1,11)
print(data)
print(data.shape)
print(data.ndim)
print(data.dtype)

#2.Create a 2D array: [[2, 4, 6],[8, 10, 12]] Find: shape,number of dimensions,total number of element.
import numpy as np
data1=np.array([[2, 4, 6],[8, 10, 12]])
print(data1)
print(data1.shape)
print(data1.ndim)
print(np.size(data1))

#3.Create an array using np.arange() from 5 to 25 with step 5. Check its dtype and convert it into float type.
import numpy as np
data2=np.arange(5,25,5)
print(data2)
print(data2.dtype)
print(data2.astype(float))

#4.Create a 3×3 array of all ones.Multiply the entire array by 5 and print the result.
import numpy as np
data3=np.ones((3,3))
print(data3)
print(data3*5)

#5.Create two arrays:A = [1, 2, 3] B = [4, 5, 6] Perform: addition multiplication (element-wise)
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a*b)


#6.Create an array: [1, 2, 3, 4, 5] Add 10 to each element and then square the result.
import numpy as np
x=np.array([1,2,3,4,5])
print(x+10)

#7.Create a 2D array using np.full() with shape (2, 3) filled with value 9. Find its dtype and change it to float.
import numpy as np
y=np.full((2,3),9)
print(y)
print(y.dtype)
print(y.astype(float))


#8.Create a 3×3 identity matrix using np.eye().Then:change diagonal position using k=1 observe the difference
import numpy as np
z=np.eye(3)
print(z)
L=np.eye(3,None,1,dtype=float)
print(L)
print(z-L)

#9.Create an array using np.linspace() from 0 to 2 with 5 values. Find: shape dtype number of elements
import numpy as np
P=np.linspace(0,2,5)
print(P)
print(P.shape)
print(P.dtype)
print(np.size(P))


#10.Create a random 2×2 array using np.random.rand(). Then: multiply it by 10 find its shape and dtype
import numpy as np
h=np.random.rand(2,2)
print(h)
print(h*10)



























































