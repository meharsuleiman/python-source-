#input function is used to take input from the user
print("Enter 1st Number:",end=" ") #end function detail in 03_RemoveNewLineBetweenPrint.py
user_input1 = input()
print("Enter 2nd Number:",end=" ")
user_input2 = input()
#NOTE: input function takes input as string
#if you want to print sum of user_input1 and 2
#firstly type casting from string to int
print("your sum is:",int(user_input1) + int(user_input2))