import numpy as np

#create an array 
arr = np.array([1,2,3,4,5,6])
print("this is an array: ",arr)

print("valus at 0 index: ",arr[0])
print("value at 1 index: ",arr[1])

#access an element of 2-dimentional array

arr_2dim = np.array([[1,2,3],[4,5,6]])
print("first enter in 1-indexed row and then print the value of indexed-1: ",arr_2dim[1,1])

print("first enter in indexed-0 row and then print the value of indexed-2: ",arr_2dim[0,2])

#access an element of 3-dimentional array
arr_3dim = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print(arr_3dim[1,1,2])


'''
[
    [  at 0-index 
        [1,2,3], 
        [4,5,6]
    ]                    -:this is the basic structure of three dimentional array
    [  at 1-index
        [1,2,3],
        [4,5,6]
    ]
]
'''


