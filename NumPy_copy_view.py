import numpy as np

#create an array
arr = np.array([1,2,3,4,5])
print("This is the orignal array: ",arr)

arr_copy = arr.copy()
print("this is the copy of array: ",arr_copy)

#now when i create a change in copied_array it will not provide any affect to orignal_array

arr_copy[0] = 11
print("this is the copied array and affected: ",arr_copy)

print("thi is the orignal array: ",arr)

print()
#-----------------> view <---------------
arr = np.array([1,2,3,4,5,6])

print("this is the orignal list: ",arr)

view_array = arr.view()
print("this is the view of array: ",view_array)

#now i make a change in view array

#The original array SHOULD be affected by the changes made to the view.
view_array[0] = 23
print("changed view array: ",view_array)
print("orignal list:",arr)

#as mentioned above copy has own data and view has not own data
#how can we check it 

x = arr.copy()
y = arr.view()
print("copy returns none: ",x.base)
print("veiw returns array: ",y.base)
