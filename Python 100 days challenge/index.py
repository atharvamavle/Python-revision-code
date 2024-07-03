# print("dfghj")
# print('dfghj')
# print('''fgyhuju''')

# a=input('enter the name')
# print(a)
# b=int(input("enter the no"))
# c=int(input("enter the sec no"))
# d=b+c
# print(d)

'''a=int(input("enter your first number"))
b=int(input("Enter your second number"))
c= a-b
print(c)

n=int(input("enter your first number"))
m=int(input("Enter your second number"))
k= n*m
print(k)

p=int(input("enter your first number"))
v=int(input("Enter your second number"))
l= p/v
print(l)'''

# a=56
# b=89
# c=a+b
# print(c)

# name= "Atharva"
# age=20
# marks= 8.60 

# print(name)
# print(age)
# print(marks)

# name="a"
# naMe="b"
# Name="c"
# nAme="d"
# namE="e"
# NAME="f"
# NaMe="g"
# NAme="h"
# print(name,naMe,Name,nAme,namE,NAME,NAme)



# x=y=z=50
# print(x)
# print(y)
# print(z )

# a,b,c=5,10,15
# print(a)
# print(b)
# print(c)

# def add():
#     a=25
#     b=3
#     c=a+b
#     print(c)
# add()    


# x=20

# def add():
#     global x
#     print(x)

#     y="Welcome To Python Tutorial"

#     print(y)

# add()

# x="Welcome to programming world"

# print(x)

# del x

# print(x)


'''a=100000000000000000000000000000000000000000000000000000000
b=222222222222222222222222222200000000000000000000000000000

c=a+b

print(c)
a=56
b=5
c=98
if a<b and c>a:
    print(True)
for i in range(1,6):
    print(i)'''
# i=0
# while i<5:

#     
#     i=i+1
#     print(i)


# a=int(input("Enter your age: "))

# if(a>18 and a<60):
#     print("You can drive")

# elif(a>60):
#     print("you cannot drive you are too old")

# else:
#     print("you are underage")


# i=0

# while i<10:
#     i=i+1
#     print(i)


# a=4
# c=5
# d=(3*7)/((2-(-1))**2-(a/float(c)))
# print(d)

# x="hello"

# assert x == "Goodbye", "x should be hello"

# class Person():
#     name="Atharva"
#     roll_no =1076
    
# p1 = Person() #object creation
# print(p1.roll_no)


# import calendar as b
# print(b.month_name[8])

# x=-1

# if x<0:
#     raise Exception("Value cannot be less than zero")


# x=int(input("Enter your age: "))

# if not type (x) is int:
#     raise TypeError('Age must be an integer')

# print(x) 

# b=int(input("write a number randomly calculation: "))
# x= lambda a: a*10

# print(x(b))


# def oustside():
#     x="Hello"
#     def inside():
#         nonlocal x
#     x="Shree Ram"
#     inside()
#     return x
# print(oustside())


x =  int(input("enter your number more than 3 "))

try:
  x < 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")
