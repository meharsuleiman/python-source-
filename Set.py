#syntax of set is
# set()
#A set is a collection which is both unordered and unindexed.
#Sets are unordered, so you cannot be sure in which order the items will appear
#Once a set is created, you cannot change its items, but you can add new items

s = set()
print(type(s))

#we can create set by list
set_from_list = set([1,2,3,4,5]) #this will take list as set
print(set_from_list)
print(type(set_from_list)) #this will check the type

#another method
l = [1,2,3,4,5]
set_from_list2 = set(l) #this is also a set
print(set_from_list2)

#now, how to add value in set
s = set()
#this is an empty set
#if i add some value in set
s.add(1)
s.add(2)
print(s)