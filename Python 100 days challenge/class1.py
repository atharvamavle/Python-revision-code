# class person():
#     a=34
# p1=person()  
# print(p1.a)


# class hello():
#     a=34

# hello_obj = hello()
# print(hello_obj.a)

# class add():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def sum(self):
#         return self.x+self.y
# print(add(5,5).sum())


# class ko:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def mul(self):
#         return self.x*self.y
#         # return mul
# print(ko(2,6).mul())

# x=int(input("Enter a number for sub: "))
# y=int(input("Enter a number for sub: "))
# class main:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def sub(self):
#         return self.x-self.y
    
# print("The sub of given number is:",main(x,y).sub())


# name=input("Enter your name: ")
# age=int(input("Enter your age in Integer format: "))
# company=input("Enter your company name: ")
# salary=int(input("Enter your salary: "))

# class info():
#     def __init__(self,name,age,company,salary):
#         self.name=name
#         self.age=age
#         self.company=company
#         self.salary=salary

# a=info(name,age,company,salary)

# print("The name of given employee is: ",a.name)
# print("The age of given employee is: ",a.age)
# print("The name of company is: ",a.company)
# print(f'The salary of {a.name} is {a.salary}')

'''Inheritance'''
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()


# class parents():
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def printname(self):
#     print(self.name,self.age)
# class child(parents):
#   def __init__(self, name, age):
#     super().__init__(name, age)
# obj=child("sdf",56)
# obj.printname()


# class parent():
#     def __init__(self,name,age,salary):
#         self._name=name
#         self._age=age
#         self._salary=salary

#     def employee(self):
#         print(f'The name of employee is {self.name} and age is {self.age} and salary is {self._salary}')

# class child(parent):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age,salary)

# object=child("Atharva",21,"100,000,000")
# object.employee()


# class parent():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def employee (self):
#         print(f"The name of the employee is {self.name},and his/her age is {self.age},and he/her Salary is {self.salary}")

# class child(parent):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age,salary)

# object=child("Atharva",20,2000000000)
# object.employee()


# class parent():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add (self):
#         return self.a+self.b
    
    
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))

# class child(parent):
#     def __init__(self,a,b):
#         super().__init__(a,b)

# addition_object=child(a,b)

# print(addition_object.add())

# class Parent():
#     def __init__(self,name,age,company,salary):
#         self.name = name
#         self.age = age
#         self.company = company
#         self.salary = salary

#     def employee (self):
#         print(f'The name is {self.name} and age is {self.age} and my company is {self.company} and my Salary is {self.salary}')

# name=input("Enter a name: ")
# age=int(input("Enter your age: "))
# company=input("Enter your company name: ")
# salary=float(input("Enter your salary: "))

# class child(Parent):
#     def __init__ (self,name,age,company,salary):
#         super().__init__(name,age,company,salary)

# emp_obj=child(name,age,company,salary)
# emp_obj.employee()


# class parents:
#     def fun1(self):
#         print("first")
# class parents2:
#     def fun3(self):
#         print("third")

# class child(parents,parents2):
#     def fun2(self):
#         print("second")
# obj=child()
# obj.fun3()

'''Multiple Inheritance'''
# class parent():
#     def wild(self, name):
#         print(f"{name} is an animal.")

# class parent2():
#     def domestic(self, name):
#         return f"{name} is a domesticated animal."

# class child(parent, parent2):
#     def __init__(self, name):
#         super().__init__()  # Initialize parent classes
#         self.name = name

# func = child("Dog")
# result = func.domestic("Dog")
# print(result)


'''Multilevel'''
# class parents:
#     def fun1(self):
#         print("first")
# class parents2(parents):
#     def fun3(self):
#         print("third")

# class child(parents2):
#     def fun2(self):
#         print("second")
# obj=child()
# obj.fun1()   
# obj.fun2() 

'''Multi-level'''
# class parent:
#     def wild (self,name):
#         print(f"{name} is an animal.")

# class parent1(parent):
#     def domestic(self,name):
#         print(f"{name} is a domesticated animal.")
    
# class child(parent1):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name

# obj=child("none")
# obj.wild('lion')
# obj.domestic("Dog")

'''HTBRID Inheritance '''
# Python program to demonstrate hybrid inheritance

# class Office:

#     def func1(self):
#         print ('This function is in Office.')

# class Emp1(Office):

#     def func2(self):
#         print ('This function is in Employee 1.')

# class Emp2:

#     def func3(self):
#         print ('This function is in Employee 2.')

# class Emp3(Emp1, Emp2):

#     def func4(self):
#         print ('This function is in Employee 3.')

# # Driver's code

# object = Emp3()
# object.func1()
# object.func2()

'''Polymorphism'''

# class car:
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model=model
    
#     def move(self):
#         print("Drive")

# class boat:
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model= model
    
#     def move(self):
#         print ("Sail")

# class plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.modl=model

#     def move(self):
#         print("Fly")

# car1=car("Mustang","2018")
# boat1=boat("Bayliner","2019")
# plane1=plane("Airbus", "A350")

# car1.move()
# boat1.move()
# plane1.move()
# for x in (car1,boat1,plane1):
#     x.move()

'''polymorphism'''
# class wild:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def animal(self):
#         print(f"{self.name} is a {self.color}")

# class domestic:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def animal(self):
#         print(f"{self.name} is a {self.color}")

# class endangered:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def animal(self):
#         print(f'{self.name} and {self.color} ')


# wild1=wild("Lion","golden")
# wild1.animal()
# domestic1=domestic("Dog","black")
# domestic1.animal()
# endangered1=endangered("Elephant","grey")
# endangered1.animal()

'''Overloading'''
# class a:
#     def show(self):
#         print("hey..")
#     def show(self,fname=""):
#         print("hey..",fname)
#     def show(self,fname="",lname=""):
#         print("hey..",fname,lname)
# obj=a()
# obj.show()  
# obj.show('techgen')              
# obj.show('training') 

# parent and child class called overriding.
# class a:
#     def disp(self):
#         print("this is parent class method")
# class b(a):
#     def disp(self):
#         super().disp()
#         print("this is child class method")
# obj=b()
# obj.disp()

# class a:
#     z=456   #public
#     _a=10   #private
#     __b=45  #protected
#     def show(self):
#         print("z",self.z)
#         print("a=",self._a)
#         print("b=",self.__b)
# obj=a()
# obj.show()  
# print(obj.__b)


# class a:
#     b=5
#     _d="hello"
#     __e=98

#     def num(self):
#         print("Z is public", self.z)
#         print("d is private", self._d)
#         print("e is protected", self.__e)

# obj=a()
# print(obj._d)

'''Local Scope'''

# def Func():
#     x = "Hello World!"
#     print(x)

# Func()

# def outerfunc():
#     x="Hello World"
    

#     def inner_func():
#         print(x)
#     inner_func()

# outerfunc()

