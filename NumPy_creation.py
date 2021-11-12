#import numpy package
import numpy
from numpy.core.fromnumeric import ndim

#create an array
arr = numpy.array([1,2,3,4,5,6]) #array in NumPy is ndarray "N dimentional array"
print(arr)

#check the type of arr
print(type(arr))

#you can import any package by it's shortcut name "alais"
import numpy as np
arr = np.array([1,2,3,4])
print(arr)

#for checking the version of numpy
print("this is the version of python: ",np.__version__)

#to create an array you can pass it any tuple list to built-in function "array()"

arr = np.array((1,2,3,4,5))
print(arr)


#------------------------->Dimentions in array<---------------------

# 0-Dimentional array
arr_Dimen0 = np.array(45)
print("this is a 0-dimentional array: ",arr_Dimen0)


# 1-dimentional array
arr_Dimen1 = np.array((1,2,3,4,5,6))
print("this is a 1-dimentional array: ", arr_Dimen1)


# 2-dimentional array 
# an array that has one dimentional array as it's element
arr_Dimen2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(arr_Dimen2)


#you can create by 
arr_Dimen_alt = np.array(((1,2,3,4),(5,6,7,8)))
print(arr_Dimen_alt)

# 3-dimentional array
arr_Dimen3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_Dimen3)

#you can check the dimentions by using "ndim"

print(arr.ndim)
print("0-dimentional array: ",arr_Dimen0.ndim)
print("1-dimentional array: ",arr_Dimen1.ndim)
print("2-dimentional array: ",arr_Dimen2.ndim)
print("3-dimentional array: ",arr_Dimen3.ndim)


#higher dimentions array
high_array = np.array([1,2,3], ndmin=5)
print(high_array)




