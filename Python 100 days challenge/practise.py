# # star= int(input("enter a number to print row: "))

# # for i in range(1,star+1):
# #     for j in range(i):
# #         print('*',end='')
# #     print()

# '''Write a Python function to find the maximum of three numbers.'''

# # a= int(input("Enter a number: "))
# # b =int(input("Enter another number: "))
# # c = int(input("Enter third number: "))
# # def max_of_three(a, b, c):
# #     if (a > b) and (a > c):
# #         return a
# #     elif (b > a) and (b > c):
# #         return b
# #     else:
# #         return c
# # print ("The maximum of", a, ",", b, ",", c, "is", max_of_three(a, b, c))

# '''Write a Python function to sum all the numbers in a list.'''

# # List = (8, 2, 3, 0, 7)

# # def add(list):
# #     total = 0
# #     for num in list:
# #         total += num
# #     return total

# # print(add(List))

# '''Write a Python function to multiply all the numbers in a list.'''
# # list=[8, 2, 3, -1, 7]

# # def mul (list):
# #     total=1
# #     for num in list:
# #         total *=num
# #     return total

# # print("The multiplication of ",list,"is",mul(list))

# '''Write a Python program to reverse a string.'''
# # def rev(string):
# #     return string[::-1]
# # print("Reversed String is :",rev("234abcd"))


# # def rev(string):
# #     return string[::-1]
# # print("Reversed String is :",rev("1234abcd"))

# '''Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.'''

# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n-1)
# # n=int(input("Input a number to compute the factiorial : "))
# # print(factorial(n))

# # n=int(input("enter a number to do factorial of a number: "))

# # def factorial(n):
# #     if n==0:
# #         return 1
# #     else:
# #         return n*factorial(n-1)
# # print("The factorial of a given number is: ",factorial(n))

# '''Write a Python function to check whether a number falls within a given range.'''

# # a=int(input("enter a number: "))
# # b=int(input("Enter a number: "))


# # def with_range(a,b):
# #     if with_range in range (1,20):
# #         print("%s is in range"%str(with_range(a,b)))

# #     else:
# #         print ("%s is not in range" %str(with_range(a,b)))

# # with_range(a,b)

# '''Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'''

# # s=input("Enter a statement to check number of lower case and upper case in the statement: ")

# # def check(s):
# #     d={"Upper_case":0,"Lower_case":0}

# #     for c in s:
# #         if c.isupper():
# #             d["Upper_case"]+=1

# #         elif c.islower():
# #             d["Lower_case"]+=1
# #         else:
# #             pass

# #     print("Orginal String is", s)
# #     print("The uppper case is: ",d["Upper_case"])
# #     print("The Lower case is: ",d["Lower_case"])

# # print(check(s))
# /

        

'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.'''

# def unique_list(l):
#     x=[]
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x
# print(unique_list([1, 3, 4, 5, 6, 7, 8, 8]))



# def unique(l):
#     x=[]

#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x
    
# print(unique([1,2,3,3,3,33,55,258,2,8,2,2]))


'''Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.'''

# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))



'''While loop'''
# print number 1 to 10

# i=1
# while i<=10:
#     print(i)
#     i+=1

'''multiplication from user'''

# num=int(input("Enter a number to print a table: "))
# count=1

# while count<=10:
#     print(f'{num} X {count} =',num*count)
#     count += 

'''
Print the following patterns using loop :
a.
*
**
***
****
'''

# using for loop

# row=int(input("enter a number for a row: "))

# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print('* ',end='')
#     print()
    
'''Using break statement'''
# i=0
# str="Prashant"

# while i<len(str):
#     if str[i]=="h":
#         i+=1
#         break
#     print("Current letters are:",str[i])
#     i+=1



# i=0
# str="Atharva"

# while i<len(str):
#     if str[i]=='h' or str[i]=="v":
#         i+=1
#         continue

#     print("The currnt string is: ",str[i])
#     i+=1


'''Pass'''

# i=0
# str="Monkey D luffy"

# while i<len(str):
#     if str[i]=="":
#         # i+=1
#         pass

#     print("The current strin is: ",str[i])
#     i+=1

# 3 Program to print Fibonacci numbers to given limit


# a=int(input("Enter a number to print numbers of row: "))


# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print('*', end = " ")
#     print()


#functions


# def inter(name):
#     message= "Hello Welcome to programming World " + name
#     return message

# name= input("Enter your name Grateful Message To view: ")
# print(inter(name))


# Simple Interest

# def simple_interest(p,t,r):
#     return p*t*r/100

# p=int(input("Enter a value of a Principal: "))
# t=int(input("Enter a value of time: "))
# r=int(input("Enter a rate of interest: "))

# print("The simple of given P,T, R is ",simple_interest(p,t,r))

# def add(a,b):
#     return a+b

# a=int(input("Enter a number of a: "))
# b=int(input("Enter a number of b: "))

# print("the sum of two number is: ",add(a,b))


# def employee(Name,Age,Company,Salary):
#     data=f'Welcome to {Company} {Name} and your age is {Age} and I am glade to Say that your Salary is {Salary}'

#     return data

# Name=input("Enter Your name for your Data: ")
# Age=int(input("Enter your Age: "))
# Company=input("Enter Company Name: ")
# Salary=float(input("Enter Salary: "))

# print(employee(Name,Age,Company,Salary))

'''OOPs Practice'''

# class person():
#     a=34

# p1=person()
# print(p1.a)

# class mult:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def multply(self):
#         return (self.x * self.y)
# print(mult().multply())

# x=int(input("enter the value of X: "))
# y=int(input("enter the value of Y "))

'''Going to Print the * '''

'''Multiple inheritance'''
# class parent():
#     def wild(self,name):
#         print(f"{name} is an animal.")
    
# class parent1():
#     def domestic(self,name):
#         print(f'{name} is an domestic animal')

# class child(parent, parent1):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name

# obj=child("dog")
# result=obj.domestic("dog")
# print(result)

'''Factorial'''

# n=int(input("Enter a number: "))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# f=factorial(n)

# print(f'The factorial of {n} is {f}')


# class parent:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def emp(self):
#         print(f'{self.name} and my age is {self.age}')

# name=input("Enter name: ")
# age=int(input("Enter your age: "))
# salary=int(input("Enter salary: "))    

# obj=parent(name,age,salary)
# obj.emp()

''' Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def car(self):
#         print(f"I am a {self.name}, I can go up to {self.max_speed} mph and milage is {self.mileage}")

# class child(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)

# obj=child("Toyota",250,15)
# obj.car()


'''Define a property that must have the same value for every class instance (object)'''

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)
    

# class Car(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)



