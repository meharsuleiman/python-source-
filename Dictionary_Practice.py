from typing import Mapping, OrderedDict


dictionary = {}
print("first method",type(dictionary))

#second method to create a dictionary
dictionary2 = dict()
print("second method :",type(dictionary2))

#in both cases, dict will be created,
#you can check whether the actual dictionary
print(isinstance(dictionary,dict)) #isinstance take two arguments, first will check and second is the type that will confirmed yet,and returns the boolean value as true or false 
#another example 

print(isinstance(dictionary2,tuple)) #the answer is false because dictionary2is dict not a tuple

#to create a dictionary
D = {'state':'Punjab','city':'Hafizabad'}
print(type(D))
print("first method",D)

#second method 
D2 = dict(state = 'Punjab', city = 'Hafizabad')
print(type(D2))
print("second method",D2)

#now we see how to add data in dictionaries

D2['town'] = 'sukheke'
print(D2)

#if you want to edit value in existing key
D2['town'] = 'lahore'
print("updated: ",D2)

#reading data from dictionary 
print("reading data from dict:",D2['town'])
print(D2['state'])

#get a key:value that is not exist in dictionary you faced an error
#print(D2['PO'])
#if you want that program will not crash and work will be done correctly
print(D2.get('PO','PO is not found')) #if key is exist in dict then str will no be run more


#for iteration with dictionary
for item in D2:
    print(item) #this command print only keys
print("\n")   
for item in D2:
    print(D2[item]) #this command print only values
print("\n")
#you can iterate by only keys
for keys in D2.keys():
    print(keys)
print("\n")
#iterate by only values
for values in D2.values():
    print(values)
print("\n")
#iterate by both at same
for key,value in D2.items():
    print(key,"have ",value)

print("\n")


#you can check whether thi keyy:value exist in dict without iterating
print('state' in  D2) #it will return answer in boolean 
print('birds' in D2)

print("\n")


#methods of dictionary

#how to update a dict
a = {} #an empty  dictionary
#a.update({'birds':'parrot'})
a.update(dict(bird = 'parrot'))
print("updated dict:", a)

#you can update existing key value pair by update
a.update({'bird':'sparow'})
print("updated value:",a)

#to clear a dictionary
a.clear()
print("cleared dict:",a)

#create a new dict 
a = {'bird':'parrot','animal':'lion','pets':'dog'}

#dict.del()

del(a['animal'])
print("updated dict",a) #del is used to delete item by calling key

b = a.pop('bird') #pop returns the value that will be deleted 
print("after poping:",a)
print(b)

#for copying one dict and store as another independent dict
b = a.copy()
print("copied dict:",b)

#check that are they independent???

a.update({'pets':'aliphant'})
print(a) #a will only changed the change is not implement to b 
print(b)


human = {'gender':'male','age':'10','weight':'55','name':'sakandar'}
print("orignal dictionary:", human)

print("searched value:",human.setdefault('name'))

print(human.setdefault('status','marriage'))
print(human)

print(human.setdefault('city')) #if second argument is missing it will take as none automatically
print(human)

a =dict.fromkeys(['name','age','gender','weight'],'nothing yet here') #if second argument will be empty then it is set default as none 
print(a)

#activity

def sentence_analyzer(sentence):
    solutions = {}
    for char in sentence:
        if char is not ' ':
            if char in solutions:
                solutions[char] += 1
            else:
                solutions[char] = 1
    return solutions


#ordered dictionary
from collections import OrderedDict
a = OrderedDict(name = 'sakandar',age = '10', gender = 'male')
print(a)


def key_masher(dict_a,dict_b):
    for key, value in dict_b.items():
        if key not in dict_a:
            dict_a[key] = value
    return dict_a



#print(sentence_analyzer('python'))
if __name__ == "__main__":
    print(sentence_analyzer('pythonn'))
    print(key_masher({'name':'sakandar'},{'age':'10'}))



