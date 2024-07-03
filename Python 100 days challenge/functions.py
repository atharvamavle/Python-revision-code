'''*************Functions*****************'''

# def hello_world():
#     print("Hello Welcome to Programming World")

# hello_world()

'''Return Statement'''

# def add():
#     a=5
#     b=5
#     c=5+5

#     return c
# print("The sum of a+b =",add())

# Creating function without return statement
# def add():
#     a=5
#     b=5
#     c=5+5

#      return c
# print("The sum of a+b =",add())

'''Argument function'''

# def func(name):
#     print("Hello welcome to Tesla",name)

# func("Atharva")

#Python function to calculate the sum of two variables     
# def mysum (a,b):
#     return a+b

# a=int(input("Enter the first number for addition: "))
# b=int(input("Enter the second number for addition: "))

# print("The sum is:",mysum(a,b))

# list1=[10,80,60,70]
# def lists(list1):
#     list1.append(20)
#     list1.append(30)
#     print("the List inside",list1)

# # list1=[10,80,60,70]
# lists(list1)

# print("The list outside:",list1)

# def change_str(str):
#     string2=str + " How you"
#     print("Printing the string inside function",string2)

# string1="Hi i am here"

# change_str(string1)

# print("printing the string outside function: ",string1)


# def add():
#     a=5
#     b=5
#     c=a+b

#     return c


# print("The sum of a+b is",add())

# def str_name(name):
#     print("Hello welcome to",name)

# str_name("Atharva")

# def add(a,b):
#     return a+b

# a=int(input("Enter integer number for addition: "))
# b=int(input("Enter integer number for addition: "))

# print("The sum is",add(a,b))

# list1=[10,20,30,40]
# def change_list(list1):
#     list1.append(50)
#     list1.append(60)
#     print("printing the inside list",list1)
# change_list(list1)

# print("printing the outside list is: ",list1)

# passing mutable objects

# def changing_str(str):
#     str= str + " How you do"
#     print("The inside string is",str)

# string1="I am fine"
# changing_str(string1)

# print("printing outside string",string1)

'''Types of arguments'''

# def func(name):
#     message= 'Hello Welcome to Tesla '+name
#     return message

# name= input("Enter your name: ")
# print(func(name))

'''1.#t he function simple_interest accepts three arguments and returns the simple interest accordingly    '''

# def simple_interest(p,r,t):
#     return p*r*t/100

# p=float(input("Enter the value of Principal: "))
# r=float(input("Enter the value of Rate: "))
# t=float(input("Enter the value of Time: "))

# print(simple_interest(p,r,t))

'''2.#the function calculate returns the sum of two arguments a and b    '''

# def add(a,b):
#     c=a+b
#     return c

# a= int(input("enter the value of a for addition: "))
# b= int(input("enter the value of b for addition: "))

# print("The sum of two number is: ",add(a,b))

'''Default Argument'''

# def printme(name,age=20):
#     print('My name is: ',name,"and my age is",age)

# printme(name="Atharva")


# def printme(name,age=20):
#     print('My name is: ',name,"and my age is",age)

# printme(name="Atharva") #the variable age is not passed into the function however the default value of age is considered in the function    

# printme(name="Luffy",age=26) #the value of age is overwritten here, 26 will be printed as age   

'''Variable-lenght argument'''

# def printme(*names):

#     for name in names:
#         print(name)

# printme("Atharva","Luffy","Hari","Prashant")

'''Keywords Arguments'''

# def func(name,message):
    
#     print("Hello My name is ",name,"And todays message is",message)
# func(name="Atharva",message="Luffy will be king of pirates")

'''2 providing the values in different order at the calling'''

# def simple_intrest(p,r,t):
#     return p*r*t/100

# p= float(input("enter the value of principal: "))
# r= float(input("enter the value of rate: "))
# t= float(input("enter the value of time: "))

# print(simple_intrest(p,r,t))

'''*******************'''
# def func(name,message,name1):
#     print("hello my first name is ",name,"And my second name is",name1,"The message i want to say",message)

# func(name="Atharva",message="I will became sucessfull is an sign of a postive attitude",name1="Mavale")


'''Python provides the facility to pass the multiple keyword arguments which can be represented as **kwargs. It is similar as the *args but it stores the argument in the dictionary format.'''

'''Example 6: Many arguments using Keyword argument'''

# def food(**kwargs):
#     print(kwargs)
       
# food(a="Apple")
# food(fruit="mango",vegetable="Methi")

'''Local variable'''

# def func(message):
#     message="I am going to be King of Pirates"
#     print(message)
# func(message="hello")


'''Table of contents
Exercise 1: Create a function in Python
Exercise 2: Create a function with variable length of arguments
Exercise 3: Return multiple values from a function
Exercise 4: Create a function with a default argument
Exercise 5: Create an inner function to calculate the addition in the following way
Exercise 6: Create a recursive function
Exercise 7: Assign a different name to function and call it through the new name
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Exercise 9: Find the largest item from a given list
Exercise 1: Create a function in Python
'''
'''Write a program to create a function that takes two arguments, name and age, and print their value.'''

# def info(name,age):
#     print('My Name:',name,'\nAge',age)

# info(name="Atharva",age=21)


'''Exercise 2: Create a function with variable length of arguments'''

# def func(*names):

#     for i in names:
#         print (i)

# func(20,40,60)
# func(40,50)

'''Exercise 3: Return multiple values from a function'''
# def add_substract(a,b):
#     add=a+b
#     sub=a-b

#     return add,sub
# a= int(input("Enter a number a: "))
# b= int(input("Enter a number b: "))


# print(add_substract(a,b))

'''Exercise 4: Create a function with a default argument'''

# def employee(name,salary=12000):

#     print("Name: ",name, " and Salary",salary)

# employee(name="Atharva",salary="20,00,000,000,000")
# employee(name="Luffy")

'''Exercise 5: Create an inner function to calculate the addition in the following way
    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it
'''

# outer function

# def outer(a,b):
#     square=a**2

#     # inner function
#     def inner(a,b):
#         return a+b
    
#     result=inner(a,b)

#     return result+5

# print(outer(5,10))

'''Exercise 7: Assign a different name to function and call it through the new name'''

# def employee(name,salary):
#     print("Employee Name is : ",name,"and salary is :",salary)

# employee(name="Atharva",salary=50000000)

# wipro_employee= employee

# wipro_employee(name="Ramcharan",salary=2005050)

'''Exercise 8: Generate a Python list of all the even numbers between 4 to 30'''

# def even():

#     a=list(range(4,30,2))

#     return a

# print("the values are",even())
# for i in even():
#     print (i)


# def odd():

#     a=list(range(3,30,2))

#     return a

# print("the values are",odd())

'''Exercise 9: Find the largest item from a given list'''

# def maxx():

#     x=[4,6,8,9,2,6,8,2]
#     print("The  maximum nuber is: ",max(x))

# maxx()



