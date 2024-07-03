# i=1
# while i<11:
#     if i==5 or i==9:
#         continue
#     print(i)
#     i=i+1

# for i in range(1,12):
#     if i==6 or i==8:
#         continue
#     print(i)    


'''Continue Statement'''

# i=0
# str="Atharva"

# while i<len(str):
#     if str[i]=='t' or str[i]=='r':
#         i+=1
#         continue
#     print("Current letters: ",str[i])
#     i+=1


'''Break Statement'''

# i=0 #because string start with 0

# str="Prashant"
# while i< len(str):
#     if str[i]=="h":
#         i+=1
#         break

#     print("Current String is: ",str[i])
#     i+=1

'''pass statement'''

# i=0
# str="Monkey D Luffy"

# while i<len(str):
#     # if str[i]==" ":
#         i+=1
#         pass

# print("the string is: ",i)
    # i+=1


'''Practice'''
# i=0
# str="Monkey D Luffy"

# while i < len(str):
#     if str[i]==" ":
#         # i+=1
#         pass

#     print("The while loop statment is: ",str[i])
#     # print("The while loop statment is: ",i)
#     i+=1

'''print number 1 to 10 using while loop''' 

# i=1
# while (i<=10):
#     print(i,end=' ')
#     i+=1

'''Example -2: Program to print table of given numbers.'''
# Using For loop

# a=int(input("Enter a number to print the table: "))

# for i in range (1,11):
#     print(a,"x",i,"=",a*i)

# Using While Loop
# num = int(input('Enter an integer: '))
# count = 1
# while count <= 10:
#     print(f'{num} x {count} =', num * count)
#     count += 1

# n=int(input("Enter a number to print a table: "))
# count=1
# while (count<=10):
#     print(f'{n} x {count} =', n*count)
#     count+=



# num=int(input("enter a number to print tabel "))

# count=1

# while count<=10:
#     print(f'{num} x {count} =', num*count)
#     count+=1



'''Infinite Loop'''

# while (1):
#     print("This is infinite loop Kidooooos.....")

'''Else With While Loops'''

# i=1

# while i<=5:
#     print(i)
#     i+=1
# else:
#     print("Loop has ended!")


# i=1

# while i<=5:
#     print(i)
#     i+=1
#     if(i==3):
#         break
# else:
#     print("Loop has ended!")

