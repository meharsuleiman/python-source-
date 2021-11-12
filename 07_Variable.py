#variable is a named memory location or memory cell
#when we create a variable it reserve some space in memory that is garbadge for us
var1 = "Hello World " #this is a string
var2 = 'My Name is___' #this is also a string
var3 = 333 #this is an integer variable
var4 = 33.9 #this is floating point var
#if you wanna print the type of variable:
print(type(var1))
#by this method we can check the type of variable
#you can add two strings
print(var1 + var2)
#but you can't add string and integer
# print(var1 + var3) #get an error
print(var3 + var4) #but you can add integer and floating point

# in other language variable name take space in memory 
#  but in python variable value take place in memory rather than name 


# in python variable location set according to it's value not by name 
a = 10
b = 10
#  suppose two variables a,b have same value , so according to upper statement there addresses are the same 
# for checking the location of variable use the function "id" 
print(a,b)
print(id(a), id(b))
# you can see there is no diffrence in adderess of varibales 
