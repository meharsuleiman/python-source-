#syntax
#list = [somethin,something]
#the square bracket [] use to indicate the string

#another syntax
mylist = list(("soap","banana","jam"))
print(mylist)
thislist = list(("apple", "banana", "cherry"))
print(thislist)


#what are list ? it is collection of things
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop"]
#suppose you want to access one thing from list then,
print(grocery[4])

shopping = ["soap", "shampoo"]
print(shopping[0])

number = [1 ,2 , 3 , 4, 72, 27, 21]
print(number) #list is print
#you see that number.list unsorted
#if you want to sort it
number.sort()
print(number)  #you see that the unsorted list sort out
#if you want to reverse the list
number.reverse()
print(number)
#<---------------------------SLICING IN LIST------------------>
list1 = [1,2,3,4,5,6,7,8,9,0,10,11,12]
print(list1[0:13])
#slicing concept in list same as in string

print(list1[::-1])# -1 change the list in reverse
#but when you write -2 at the place of -1
print(list1[::-2]) #first;y, it will reverse the list and then jump by 1
#but this will work only when x,y parameters blank
print(list1[0:13:-2]) #it will gives the blank list
print(max(list1)) #it gives the max number in list
print(min(list1)) #it gives the min number in list
print(len(list1)) #Len function gives the lenth of list

#<-------------------append in list---------------------->
# append mean to add something at the end
list2 = [2,3,4,5,6,7,8,9,0]
list2.append(92) #when you write this it wil be add 92 at the end of list
print(list2)
#it will add the number at the end of list, if you want to add at any index in list then
#<-------------------insert in list---------------------->
list2.insert(1,23) # ",.insert(x,y)" x show the index and y show the number that wil be added
print(list2)
#<------------------remove in list----------------------->
list2.remove(5) #you entered the number % it will remove the value 5 in list
print(list2)
#<----------------pop in list---------------------->
list2.pop() #POP remove the number from list if it blank then remove the number from last
#it is used to remove at specified postition
print(list2)
#<------------------------ list function------------------->
'''
append():	Adds an element at the end of the list
clear():	Removes all the elements from the list
copy(): 	Returns a copy of the list
count():	Returns the number of elements with the specified value
extend():	Add the elements of a list (or any iterable), to the end of the current list
index():	Returns the index of the first element with the specified value
insert():	Adds an element at the specified position
pop():  	Removes the element at the specified position
remove():	Removes the first item with the specified value
reverse():	Reverses the order of the list
sort(): 	Sorts the list
'''

'''
remove() delete the matching element/object whereas del and pop removes the element at a specific index.
del and pop deals with the index.
The only difference between the two is that- pop return deleted
the value from the list and del does not return anything
'''

#<------------------------------index function----------------->
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
#<---------------------------copy function--------------------->
num1 = [1,1,23,4,5,6,7]
x = num1.copy()
print(x)
