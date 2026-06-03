#1.Write a Python program to print "Hello, World!".
print("Hello , World!")


#2.Write a program to take your name as input and print a welcome message.
x=input("Enter Your Name: ")
print("Welcome ! to the new world of python",x)

#3.Write a program to add two numbers entered by the user.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(a+b)

#4.Write a program to find the area of a rectangle using length and breadth.
l=float(input("Enter the length of rectangle: "))
b=float(input("Enter the breadth of rectangle: "))
area=l*b
print(area)

#5.Write a program to check whether a number is even or odd
a=int(input("Enter the number: "))
if a%2==0:
    print(" The number is Even")
else:
    print("The number is Odd")


#6.Write a program to find the largest of two numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    print("First number is greater than second ")
elif a <b:
    print("Second number is greater than first")
elif a==b:
    print("Both number are equal")


#7.Write a program to swap two variables.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
a,b=b,a
print(a,b)

#8.Write a program to convert Celsius temperature into Fahrenheit.
temp=float(input("Enter the temperature in Celsius: "))
F=((9/5)*temp)+32
print("The temperature in Fahrenheit is", F)

#9.Write a program to find the square and cube of a number.
a=float(input("Enter the first number: "))
sq=a*a
cube=a*a*a
print(sq,cube)

#10.Write a program to check whether a person is eligible to vote or not.
x=int(input("Enter the Age to check eligibility: "))
if x>=18:
    print("The person is eligible to vote")
else:
    print("Not Eligible to Vote")

#11.Write a Python program to print numbers from 1 to 10 using a loop
n=int(input("Enter the number: "))
for i in range (n):
    print(i)


#12.Write a program to print the multiplication table of a number.
n=int(input("Enter the number: "))
for i in range(1,n):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print()
    
#13.Write a program to find the sum of first n natural numbers.
n=int(input("Enter the number: "))
print(f" The Sum of first {n} Natural number is: ", (n*(n+1))/2)

#14.Write a program to find the factorial of a number.
n=int(input("Enter the number whose factorial you want to find out: "))
fact=1
for i in range (1,n+1):
    fact=fact*i
print("Factorial : ", fact)

#15.Write a program to count the number of vowels in a string.
x=input("Enter the string to count: ")
count=0
for ch in x:
    if ch in 'aeiouAEIOU':
        count+=1
print("The number of vowels is: ", count)
print()

#16.Write a program to reverse a string.
x=input("Enter the string to count: ")
rev=x[::-1]
print(rev)

#17.Write a program to check whether a string is a palindrome or not.
x=input("Enter the string to count: ")
y=x[::-1]
if x==y:
    print("The string is Palindrome")
else:
    print("Not Palindrome")

#18.Write a program to find the largest element in a list
x=[1,2,3,4,5,6,7,8]
print(max(x))

""""
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print(lst)
#this one is for taking the enteries of list by user
#Explanation
input().split() → splits input into list of strings
map(int, ...) → converts each element into integer
list(...) → converts map into list
"""
#18(a)Take space-separated integers as input and print their squares using map()
x=list(map(int, input("Enter the number : ").split()))
square=[]
for i in x:
    square.append(i*i)
print(square)


#19.Write a program to calculate the average of elements in a list.
x=list(map(int, input("Enter the number : ").split()))
print(x)
print(sum(x)/len(x))

#20.Write a program to check whether a number is prime or not.
x=int(input("Enter the number to check whether it's prime or not: "))
if x>1:
    for i in range(2, x):
        if x%i==0:
            print("The number is not prime")
        else:
            print("Prime")






















