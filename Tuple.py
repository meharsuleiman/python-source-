#what are tuples?
#syntax
# tuple =(something,something)
# parantheses () are used to indicate the tuple
#in list values can be change "muteable"
#in tuple values can't be change "inmutable"

#if i want to chage the values in tuple i can't
myCar =("ford","hundai","toyota","kia")
#and i wished 0 index change by "ferari"
#myCar[0] = "ford sulaiman" it give me an error
#it means that tupple can't be changed

#how to check that it is a tuple or not
print(type(myCar)) #it gives me a class tuple

#how to check the length of tuple
print(len(myCar)) #it gives us the number of values in tuple

tuple1 =(1,2,3,4,5)
print(tuple1)
#but if you want to create a tuple of 1 element
tuple2 =(1)
print(tuple2) #it does't tuple
#for creating it as a tuple then a comma , wil be add
tuple3 =(1,)
print(tuple3) #now it will be change into tuple, if you don't add comma then interpreter takes
#as a simple variable

#<-----------------------interchange two variables------------->
a = 10
b = 20
#<----------------------tradional method------------->
#temp =a
#a = b
#b = temp
#print(a,b)
#<--------------------python method------------------>
#but in python
a,b =b,a
print(a,b) #hahaha! how interesting:)

#<-------------------------Type Casting-------------------->
#now have a big question that we change the type of tuple into list
#yes we can do it

myCar =("ford","hundai","toyota","kia")
print(type(myCar)) #you can see it has tuple class, but now i wanna change into list

MyCarTemp =list(myCar) #this will change the type of tuple into list
print(type(MyCarTemp))
#now can i change list into tuple

MyCarTuple = tuple(MyCarTemp) #it will change again into tuple
print(type(MyCarTuple))

#it means that i can create changing in tuple values by converting into list and after creating changes
#convert it into again in tuple

#<--------------------------ADVANTAGES--------------------->
'''
unchangeable
ordered
allow duplicates 
'''