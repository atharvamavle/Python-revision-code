# Dict={}
# print(type(Dict))
# print(Dict)

# Dict= dict({"Name":"Atharva","Age":21})
# print(Dict)

# Dict=dict([(1,"Ram"),(2,"Sham")])
# print(Dict)

'''Accessing the Dictnary values'''
# Employee={"Name":"Atharva","Age":21,"Salary":"$1,00,0000"}

# print("Name: %s" %Employee["Name"])

# print("Age: %d" %Employee["Age"])

# print("Salary %s" %Employee["Salary"])1


'''Adding Dictionary'''

# Dict={}
# print("Empty Dictionary")
# print(Dict)

# Dict[0]= "Atharva"
# Dict[1]= "Prashant"
# Dict[2]= "Harikesh"
# print(Dict)
# Dict['Emp_ages']=21,25,22
# print(Dict)

# Employee={"Name":"Sham","Age":26,"Salary":"$3000","Company":"Wipro"}
# print(Employee)

# print("Enter the new details of new employee")

# Employee["Name"]= input("Name: ")
# Employee["Age"]= input("Age: ")
# Employee["Salary"]= input("Salary: ")
# Employee["Company"]= input("Company: ")

# print("Printing new data")
# print(Employee)




'''Deleting Elements'''

Employee={"Name":"Atharva","Age":21,"Salary":"$1,00,0000"}
# del Employee['Name']
# print(Employee)
# del Employee
# print(Employee)

# Employee.pop('Age')
# print(Employee)

## for loop to print all the keys of a dictionary
# Employee={"Name":"Atharva","Age":21,"Salary":"$1,00,0000","Company":"GPT AI"}

# for i in Employee:
#     print(i)

# print("\n")

#for loop to print all the values of the dictionary

# for i in Employee:
#     print (Employee [i])

#for loop to print the values of the dictionary by using values() method.
# for i in Employee.values():
#     print(i)

#for loop to print the items of the dictionary by using items() method.

# for x in Employee.items():
#     print(x)

#for loop to print the items of the dictionary by using keys() method.

# for i in Employee.keys():
#     print(i)

'''Properties of Dict'''

# Employee={"Name":"Atharva","Age":21,"Salary":"$1,00,0000","Company":"GPT AI","Name":"Sham"}

# for i in Employee.items():
#     print(i)

'''We can use numbers, strings, or tuples as the key, but we cannot use any mutable object like the list as the key in the dictionary.'''

# Employee={"Name":"Atharva","Age":21,"Salary":"$1,00,0000","Company":"GPT AI",[10011,2023]:"Department_ID"}

# print(Employee)

# Employee=('name','age')
# y=0
# thedict=dict.fromkeys(Employee,y)
# print(thedict)

# Employee={"Name":"Atharva","Age":21,"Salary":"$1,00,0000","Company":"GPT AI"}

# a=Employee.get("Name")
# print(a)
# def add():
#     a=45
#     b=45
#     c=a+b
#     return c
# print("sum is",add()) 