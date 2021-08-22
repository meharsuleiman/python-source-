str1 = "sulaiman is a good boy"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
#what it mean?
#string is collection of words
#every letter in"str1" has an index
#in python index start from "0"


#if you want to print a piece of string then you try to slicing it
#slicing meaning is break into pieces

print(str1[0:7]) #----> it's output is that "sulaima"
#another method
print(str1[:7])  #----> when we blank starting index interpreter takes place as "zero"
#let's suppose "str1[x:y]", "x" is starting point and "y" is ending point
#x is an included number and y is an excluded number

print(str1[0:100]) #----> when i write ending index as 100 it show no error and the orignal length of string print
#<-----------------Length of String---------------->
print(len(str1))


'''
S|U|L|A|I|M|A|N|
0|1|2|3|4|5|6|7|
'''

#<----------------------------Negative indexs--------------------->
'''
S |U |L |A |I |M |A |N |
-8|-7|-6|-5|-4|-3|-2|-1|
'''
#NEGATIVE indexes take string in endpoint direction
mystr="sulaiman"
print(mystr[-9:-1])
# -9 as starting point that is "s" and and -1 is ending point that is "a"
#if i want to write full string then
print(mystr[-9:]) #---->  when i take y as blank then it print complete string


#<-------------------------------Advance Slicing----------------------------->
str2 = "sulaiman is a bad boy"
#this is a string, if you want to print this string by skipping letters
print(str2[0: :2]) #str2[x:y:z} "z" is by default 1 but when we change it by 2 it skips charachter by 1
print(str2[ : :3]) #when 1 take z as 3 then it skip 2 charachters

#negative string

print(str2[ : :-1]) #when i put -1 then it reverse the string
print(str2[ : :-2]) #then it reverse the string and skip the charachters by 1



#<-----------------------------------------String Functions-------------------------------------->
print(mystr.isalnum()) #alpha numeric string in which space are not
print(str1.isalnum()) #understand by run the program
print(str1.isalpha())
print(str1.endswith("boy")) #it means what is a word that is ended the string in my case "boy" is the last word
#that end the string
print(str1.count("a"))  #count function firstly count the letter in string and print in my case a is used 3 times
print(str1.capitalize()) #it capitalize the first letter of string
print(str1.find("boy")) #it gives 19 it means that boy start at 19 index
#it is use to find in strings
print(str1.upper()) #complete string convert into upper case
print(str1.lower())
print(str1.replace("is","are"))# it replace the word by a new word
