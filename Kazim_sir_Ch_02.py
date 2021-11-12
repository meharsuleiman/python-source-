

#int data-type
positive_int = 128
print(positive_int)
print(type(positive_int))

negative_int = -128
print(negative_int)
print(type(negative_int))

Larger_int = 12345678900
print(Larger_int)
print(type(Larger_int))

#floating-point data-type
positive_float = 1.2345
print(positive_float)
print(type(positive_float))

negative_float = -1.2345
print(negative_float)
print(type(negative_float))

Larger_float = 1234567890.234567789890
print(type(Larger_float))

# Lets some fun with floating numbers.
 
# an example of floating point number
n = 3.1234
print(type(n))
 
# see some more examples
import math
from typing import BinaryIO
#print(math.pi)
#print(math.e)
x = math.pi
print(x)
y = math.e
print(y)

#we can convert the integer to floating point 
z = float(23)
print(z)

#binary numbers in python#
# when you convert binary you will write a prefix "0b"
print(0b11001100)
print(0b1100)
print(0b011)
print(0b11100011)

# hexa decimal numbers in python
# hexa-decimal numbers are base 16 consist of 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F 
# hexa decimal numbers are consist of "0x" 

print(0x123)
print(0xABC123)
print(0x123)

# octal numbers are the 8 base 
# they are consist of 0 to 7 
print(0o123)
print(0o012)


#converting between types of number system
# decimal to binary 
decimal_numbers = int(204)
Binary_numbers = bin(decimal_numbers)
print(Binary_numbers)

# decimaal to hexa 

hexa_numbers = hex(decimal_numbers)
print(hexa_numbers)

# decimal to octal 

octal_numbers = oct(decimal_numbers)
print(octal_numbers)

#erthimatic operators
a = 10
b = 3
print(a+b) #for adding
print(a-b) #for suntract
print(a*b) #for multiply
print(a/b) #for qutiont
print(a//b) #for floor qutiont
print(a%b) #for modulus
print(abs(-5))
print(int(5.5))
print(float(5))
print(pow(2,3))
print(2 ** 3)
print(divmod(10//3,10%3))


#assignment operators
x = 10
x+=1
print(x)
x-=1
print(x)
x*=2
print(x)
x%=3
print(x)
x/=3
print(x)
x**=3
print(x)


print(int(5*(4-2) + (100 / (5/2))*2))


#days convert into years weeks and days

days = int(input("enter days:"))

years = days // 365
print(years)
weeks = (days % 365) // 7
print(weeks)
extra_days = days - ((years *365) + (weeks *7))
print(extra_days)
 