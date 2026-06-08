        #Multiplication Table
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n * i, end=" ")



#Even Positioned Characters
# s= input("Enter a String: ")
# for char in range(len(s)):
#     if char % 2 == 0: 
#         print(s[char],end="")




        #While Loop
# n = int(input("Enter a number: "))
# while n >= 0:
#     print(n, end=" ")
#     n -= 1





        #Jumping through While
# n = int(input("Enter a number: "))
# i = 1
# while i**2 <= n:
#     print(i**2, end=" ")
#     i += 1




        #Zero Convertor
# n = int(input("Enter a number: "))
# if n < 0:
#     while n <= 0:
#         print(n, end=" ")
#         n += 1
# else:
#     while n >= 0:
#         print(n, end=" ")
#         n -= 1



        #The Else Statement
# a = int(input("Enter a number: "))
# if a > 100:
#     print("Big")
# else:
#     print("Small")



        #Even Odd Game
# n = int(input("Enter number of apples in bag: "))
# if n % 2 == 0:
#     print("Friend")
# else: 
#     print("You")


# Greatest of three  numbers:
# a = int(input())
# b = int(input())
# c = int(input())

# if(a>b):
#     if(a>c):
#         print(f"{a} is grestest")
#     else:
#         print(f"{c}  is greatest")
# else:
#     if(b>c):
#         print(f"{b}  is greatest")
#     else:
#         print(f"{c}  is greatest")




# Take year input and print if year is a leap year

# year = int(input("Enter the year:"))

# if((year%4==0 and year%100 !=0) or (year%400==0)):
#     print("Leap year")
# else:
#     print("Not a leap year")






# Calculator

# def calculate(a:int,b:int,operator:int):
#     match operator:
#         case 1:
#             print(a+b)
#         case 2:
#             print(a-b)
#         case 3:
#             print(a*b)
#         case 4:
#             print(a/b)
#         case _:
#             print("Invalid operator")

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# operator=int(input("Enter the operator number: (1='+',2='-',3='*',4='/')"))
# calculate(a,b,operator)



#The FizzBuzz Program
# n= int(input("Enter a number: "))
# if(n%3==0 and n%5==0):
#     print("FizzBuzz")
# elif(n%3==0):
#     print("Fizz")
# elif(n%5==0):
#     print("Buzz")
# else:
#     print(n)




#DIfference between tables of 2 numbers
# n1= int(input("Enter first number: "))
# n2= int(input("Enter second number: "))
 
# for i in range(1,11):
#     diff= n1*i - n2*i
#     print(diff, end=" ")

##########################################################################

# Square wall
# n= int(input("Enter n: "))
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print("")




#RIght angle triangle

# n= int(input("Enter n: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



#Hollow RIght angle triangle

# n=int(input("ENter n:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(i==1 or j==1 or i==j or i==n):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")





#Inverted RIght angle triangle

# n=int(input("Enter n: "))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



#Factorial

# n=int(input("ENter n: "))
# fact=1
# for i in range(n,1,-1):
#     fact= fact*i
# print(fact)


# Divisor
# n=int (input("Enter n: "))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=" ")
    



# CHeck Prime number

# n=int(input("Enter n: "))

# for i in range(1,n+1):
#     if(n%i==0 and i!=1 and i!=n):
#         result="Not Prime"
#         break
#     else:
#         result="Prime Number"
# print(result)      


##############################################################################################

# Next Prime number

# n= int(input("Enter n: "))

# for i in range(n+1,501):
#     for j in range(1,i+1):
#         if(i%j==0 and j!=i and j!=1):
#             break
#     else:
#         result=i
#         print(result) 
#         break
 #############################################################################################   
    

                                # n = int(input("Enter n: "))

                                # for i in range(n + 1, 501):
                                #     for j in range(2, i):
                                #         if i % j == 0:
                                #             break
                                #     else:
                                #         print(i)
                                #         break








# i=10
# for i in range(1,i):
#     print("hello",end=" ")
# else:
#     print("WOrld")



















