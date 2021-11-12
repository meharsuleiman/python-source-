#when you write integer in double quotes it represents as string
var1 = "345"
print(type(var1))
var2 = "34"
print(type(var2))
#now you wanna add var1 and var2
print(var1 + var2) #you expect that the interpreter returns the sum but that is not
#strings are concatinate with each other

#now the question is that are we change the type of var1 and var2 from string to int
#the answer is YEs
#-------------------> TYPE-CASTING
var3 = int(var1)
var4 = int(var2)

print(type(var3))
print(type(var4))
#now you can see the types are changed
print(var3 +var4) #now interpreter returns the sum

#list of type casters
int()
float()
str()


