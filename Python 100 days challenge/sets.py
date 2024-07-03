'''.....Sets......'''

'''Tuples is unoredered'''
# tp=set(["hello","Atharva","mavale"])
# print(type(tp))

# for i in tp:
#     print("i is ",i)

# print(tp)



# set={1,2,3,"Atharva",201.697,987}

# print(type(set))

# tp1={1,23,["Hello World",201.36]}
# print(tp1)


# st8={}
# print(type(st8))

# st4= set()
# print(type(st4))

#set doesn't take duplicate elements

# sets1={1,2,3,3,3,6,6,58,85,574,1}
# print("The set have unique vale")

# for i in sets1:
#     print(i)

'''Adding Items in a Set'''

# Months={"jan","Feb","Mar","Apr","may"}
# print(Months)
# Months.add("jun")
# print(Months)

'''Python provides the update() method. It accepts iterable as an argument.'''

# months = {"Jan", "feb", "mar", "april", "May"} 
# months.update(["jun","jul","aug","sep"]) 
# print(months)
# for i in months:
#     print(i)


'''Removing Items in Sets'''

# months={"jan","feb","mar","apr","may"}

# print(months)

# months.remove("jun") using Remove throw error when item is mot presented in list
# months.discard("jun") using discard throws no error even if item is not presented in the sets 
# print(months)

'''Consider the following example to remove the item from the set using pop() method.'''

# months={"Jan","Feb","Mar","Apr","May","june","july","Aug"}

# for i in months:
#     print(i)

# months.pop()
# print(months)

'''Python provides the clear() method to remove all the items from the set.'''
# months.clear()
# print(months)

'''Python Sets operation'''
'''Union'''
# day1={"mon","tue","wed","thu","frid"}
# day2={"sun","tue","mon"}

# print(day1|day2) #printing the union sets

# print(day1.union(day2))

'''Intersection'''

# months1={"Jan","Feb","Mar","Apr","May","june"}

# months2={"Jan","Feb","Mar","Apr","july","Aug"}

# months3={"Apr","May","june","july","Aug"}

# print((months1 & months2))

# print(months1.intersection(months2))

'''Intersection update'''

# months1.intersection_update(months2,months3)
# print(months1)

'''Difference between two sets'''
# print(months1-months3) # prints the difference of the two sets months1 and months3 
# print(months1.difference(months3))

'''Symmetric difference of sets, it removes that element which is present in both sets'''

# a={1,2,3,5,6,9,8}
# b={4,5,8,5,2,58,9}
# c= a^ b
# print(c)

# c=a.symmetric_difference(b)
# print(c)

'''Set Comparisons'''
# a={"Mon","Tue","Wed","Thu","Fri"}
# b={"Mon","Tue"}

# print(a>b) #b is subset of a
# print(a<b) #b is not subset of b
# print(a==b) # a & b are not equal  

'''Frozen Sets'''
'''The frozen sets are the immutable form of the normal sets'''

# Frozensets= frozenset([1,2,3,5,5,8,8])

# print(type(Frozensets))

# for i in Frozensets:
#     print(i)

# Frozensets.add(5)

# print(Frozensets)

'''Frozenset for the dictionary'''

# dictionary={"Name":"Mavale","Std":"Under-Graduate","Age":21}

# print(type(dictionary))

# Frozenset= frozenset(dictionary)

# print(type(Frozenset))

# for i in Frozenset:
#     print(i)

'''Write a program to remove the given number from the set.'''

# a={"Mon","Tue","Wed","Thu","Fri"}

# a.remove("Mon")

# print(a)

'''Write a program to add multiple elements to the set.'''

# a={"Jan","Feb","Mar"}

# a.update(["Apr","may","jun"])

# print(a)

'''Write a program to find the union between two set.'''

# a={1,2,3,5,69,7}
# b={5,6,8,1,5,58,7}

# print(a.union(b))

'''Write a program to find the intersection between two sets.'''
# print(a.intersection(b))

'''Write the program to add element to the frozenset.'''
#certainly we couldn't add element in frozen set because it is immutable

# frozensets= frozenset([1,2,33,58,5,2,236,7])

# print(type(frozenset))

# for i in frozenset:
#     print(i)

# frozenset.add(45)
# print(frozensets)

'''Write the program to find the issuperset, issubset and superset.'''

# a={1,2,3,5,5,6,68,7}
# b={1,2,3}
# c={7,5,2,6,98,233,582,7}

# superset=a>b
# print(superset) #b is subset of a

# issubset=c<b
# print(issubset)

'''**********************End of Sets********************************'''
