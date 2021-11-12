import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)


arr = np.array(["cherry","watermelon","apple","mango"])
print(arr.dtype)


#define datatype as an optional argument
arr = np.array([1,2,3,4], dtype='S')
print(arr.dtype)



#Converting Data Type on Existing Arrays
#you can done it by astype()
print(arr.dtype) #the type of array is string
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype) #but now it would be converted into new integer

