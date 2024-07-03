#conditional Statement

'''IF Statement'''
#program 1
# a=int(input("Enter a number to check that given number is Odd or Even: "))
# if(a%2==0):
#     print("The Entered number is Even")

# else:
#     print("The Entered number is Odd")

'''Program to print the Largest of the three'''

a=int(input("Enter your number a? "))
b=int(input("Enter your number b? "))
c=int(input("Enter your number c? "))

if(a>b and a>c ):
    print ("Largest Number is ",a)

elif(b>a and b>c):
    print("Largest number is ",b)

else:
    print("Largest number is ",c)

# if(b>a and b>c):
#     print('Largest Number is ',b )

# if(c>a and c>b):
#     print ('Largest Number is',c)