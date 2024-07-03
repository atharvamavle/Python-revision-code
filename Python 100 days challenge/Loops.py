# Literating String in Loops
# str="Atharva"
# for i in str:
#     print(i)

'''Program to Print table of Given number'''
# n=int(input("Enter the Number:"))  
# list=[1,2,3,4,5,6,7,8,9,10]

# for i in list:
#     c=i*n
#     print(c)

'''Program to print the Sum of the Given List'''

# list=[10,54,26,98,23]
# sum=0

# for i in list:
#     sum=sum+i
# print("The Sum is ",sum)


'''Loop using Range Function'''

# i=1
# n=int(input("Enter your number to Print"))
# for i in range(0,11):
#     a=i*n

# print(a)

'''************************'''
# a="Python"

# for i in a:
#     print (i)


# for i in range(0,11):
#     print(i*12)

# list=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in list:
#     sum = sum+i
# print("The sum is", sum)

# n=int(input("Enter a number to print table: "))

# for i in range(1,11):
#     c= n*i
#     print(n,"*",i,"=",c)


# list=["Atharva","Hari","Prashant"]
# for i in list:
#     print ("Hello",i)

'''Nested Loops'''

# row=int(input("Enter the rows: "))

# for i in range(0,row+1):

#     for j in range (i):
#         print("*",end="")
#     print()

'''Program number to pryamid'''

# num=int(input("number of Rows: "))

# for i in range(0,num+1):
#     for j in range(i):
#         print(i,end="")
#     print()

'''Else with loops'''

# for i in range (0,5):
#     print(i)

# else:
#     print("loop is exausted since there is no break")


# for i in range(0,5):
#     print(i)
#     break;

# else:
#     print("Loop is totally exausted ")

# print("Loop is broken due to break statement")


'''Practice question'''

# row=int(input("Enter numbers of Row: "))

# for i in range(0,row+1,1):
#     for j in range(i):
#         print(1,i+1,end="")
#     print()

# print("Number Pattern ")

# # Decide the row count. (above pattern contains 5 rows)
# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(2, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")



# row=int(input("Enter a number for row: "))

# for i in range(1,row+1,1):
#     for j in range (1,1+i):
#         print(j,end="")
#     print()



# row=int(input("Enter a number for row: "))

# for i in range(1,row+1,):
#     for j in range (i):
#         print(i,end="")
#     print()

# sum=0
# add=int(input("Enter a number for addition: "))

# for i in range(1,add+1,1):
#     sum+=i

# print("The sum is: ",sum)


# a=int(input("Enter a number to print a table: "))

# for i in range(1,11):
#     b=a*i
#     print(a,"*",i,"=",b)

'''Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
'''



# numbers = [12, 75, 150, 180, 145, 525, 50]

# for items in numbers:
#     if items>500:
#         break
#     elif items > 150:
#         continue

#     elif(items %5==0):
#         print(items)


# numbers = [12, 75, 150, 180, 145, 525, 50]

# for items in numbers:
#     if items>500:
#         break

#     elif items>150:
#         continue

#     elif items%5==0:
#         print(items)


# num=int(input("Enter number to print rows: "))
# num= 5
# for i in range(1,num+1):
#     for j in range(-i,-1):
#         print(j,end="")
#     print()

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()


'''Practices'''
# row=int(input("enter a number for a No of row: "))

# for i in range(0,row+1,1):
#     for j in range(i):
#         print(j, end=" ")
#     print()


# row=int(input("Enter a number for row: "))

# for i in range(1,row+1,1):
#     for j in range (1,1+i):
#         print(j,end="")
#     print()

