print("Enter a number: ")
a = input()
print("you entered a number", a)
#a big question
#what is the data-type of "a"
#so, let's check it
print(type(a)) #it's output as string
#it means that "input()" take value as string
#now if you add some number in a as----> a+10
#you now "a" is a string you can't add int in string so firstly you convert "a" into int
a = int(a)
print(type(a))
print("sum of a and 10 is:",a + 10)
