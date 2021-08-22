#dictionary is nothing but key value pairs
#syntax
# dictionary = { }
#the parentheses are used to define a dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

d1 ={"ali":"burger","awais":"pizza","shahzaib":"mango"}
#print(type(d1)) #this will return me dict class
print(d1["ali"]) #it print coressponding value of ali
print(d1["awais"]) #it print corresponding value of awais
#it is case sensitive
#we shall create dictionary in dictionary
d2 ={"arslan":"repairer","mohid":"carpenter","sulaiman":{"B":"meggei","L":"chicken","N":"drink"}}
#at sulaiman is again a dictionary
#print(d2["sulaiman"]["B"]) #firstly enter in the "sulaiman" and then print corresponding value of "B"
#dictionary is changeable
# if i want to add some other key:value pairs yes i can do it
d2["zill-e-huma"]= "junk food"
d2["rehman"]= "fast food"
print(d2)
#if rehman said to me that my name is cut from dictionary
del d2["rehman"] #this function is delete the key:value pair of rehman from dictionary
print(d2)
#<--------------------------FUNCTIONS OF DICTIONARY------------------>
'''
clear() 	Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items() 	Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault():Returns the value of the specified key. If the key does not exist: insert the key,
             with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''
