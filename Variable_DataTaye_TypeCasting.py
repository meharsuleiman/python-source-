var1 = "hello_World"   #string type varible
var2 = 'hello_World'   #also string type varible
var3 = '''hello_World'''   #also string type varible
var4 = 32    # integer type variable
var5 = 13.99   # floating type variable
var6 = True 

#what is varible?
#variable is contenor in which we store some value,
#variable is named memory loction or memory cell in which we store some values]

#python interpreter is very intelligent it automatically detect the type of variable
#let's check the type of variable using type function
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

#<----------------Now-------------->
#if i add var4(int) and var5(float)
print(var4 + var5) #it gives the answer 45.99
#but when i add var1 and var4
#print(var1 + var4)
#it gives the error message
#it means that you are not add string in int or float
#but if the string is consist of like this "345"
#then you convert it into int by typecasting and then add


#<-------------Type Casting---------->
#suppose
var6 = "64"
var7 = "36"
print(var6 + var7) #you think that the answer will be return "100"
#you think wrong because the var6 is string and var7 is also string and the plus+ sign is bind them
#if you want to get 100 then you have to change datatype from string to int
var6 = int(var6)
#also
var7 = int(var7)
#now add
print(var6 +var7)


#<----------------!------------------->
#if you want to print a string 10 times
print(10 * "Hello World\n")
