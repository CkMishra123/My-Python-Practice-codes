#1.Check whether a number is positive, negative, or zero.
x=int(input("Enter the number: "))
if x>0:
    print("Number is positive")
elif x==0:
    print("Number is zero")
elif x<0:
    print("Number is negative")

#2.Check whether a number is even or odd.
x=int(input("Enter the number : "))
if x%2==0:
    print("The number is even")
else:
    print("The number is odd")

#3.Take a number and check if it is divisible by 5.
x=int(input("Enter the number : "))
if x%5==0:
    print("The number is divisible by 5")
else:
    print("Not divisible by 5")

#4.Input a person's age and check if they are eligible to vote (18+).
Age=int(input("Enter the Age : "))
if Age>
=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


#5.Take two numbers and print the greater number.
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
if a>b:
    print("First number is greater than second number")
elif a==b:
    print("Both number are equal")
elif a<b:
    print("Second number is greater tha First number")

#6.Take three numbers and print the largest among them.
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if a>b and a>c:
    print("First number is largest among all")
elif b>a and b>c:
    print("Second number is largest among all")
elif c>a and c>b:
    print("Third number is largest among all")
elif a==b and b==c:
    print("All numbers are equal")
elif a==b and a>c:
    print("Both first and second number are equal and both are largest")
elif b==c and b>a:
    print("Both second and third number are equal and largest")

#7.Check whether a given number is a multiple of both 3 and 7.
x=int(input("Enter the number: "))
if x%3==0 and x%7==0:
    print(" The number is multiple of both 3 and 7")
else:
     print("Itsn't multiple of 3 and 7")

#8.Input marks and print grade:90+ → A,75–89 → B,50–74 → C,<50 → Fail
x=float(input("Enter the mark to check the Grade: "))
if x>=90:
    print("Grade A")
elif x>=75 and x<=89:
    print("Grade B")
elif x>=50 and x<=74:
    print("Grade C")
elif x<50:
    print("Fail")

#9.Check whether a year is a leap year.
x=int(input("Enter the year:"))
if (x%4==0) or (x%400==0 and x%100!=0):
    print("Its a Leap Year")
else:
    print("Not a Leap Year")

#10.Take a character and check if it is a vowel or consonant.
x=input("Enter the Character: ")
if x in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

#11.Input a number and check whether it is a 3-digit number.
x=int(input("Enter a number: "))
if x>=100 and x<=999:
    print("Its a 3 digit number")
else:
    print("Not 3 digit number")

#12.Take two numbers and check if they are equal, greater, or smaller.
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
if a>b:
    print("First is greater than second")
elif a==b:
    print("Both numbers are equal")
elif a<b:
    print("Second number is greater than first")

#13.Check whether a number lies between 10 and 50 (inclusive).
x=int(input("Enter the number: "))
if x>=10 and x<=50:
    print("Lies between 10 and 50")
else:
    print("Doesn't lie between 10 and 50")

#14.Input temperature and print:40 → Very Hot,30–40 → Hot,20–29 → Moderate,<20 → Cold
x=float(input("Enter the Temperature: "))
if x==40:
    print("Very Hot")
elif x>=30 and x<=40:
    print("Hot")
elif x>=20 and x<=29:
    print("Moderate")
elif x<20:
    print("Cold")

#15.Check whether a number is divisible by 2, 3, both, or none.
x=int(input("Enter the number to check divisibility :"))
if x%2==0:
    print("Divisible by 2")
elif x%3==0:
    print("Divisible by 3")
elif x%2==0 and x%3==0:
    print("Divisible by both")
elif x%2!=0 and x%3!=0:
    print("Divisible by none")

#16.Input a number and check whether it is prime or not.
x=int(input("Enter the number to check whether it is prime or no: "))
count=0
for i in range (1,x+1):
    if x%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not Prime")

#17.Input three sides and check whether they can form a valid triangle
a=int(input("Enter the 1st side of Triangle : "))
b=int(input("Enter the 2nd side of Triangle : "))
c=int(input("Enter the 3rd side of Triangle : "))
if a+b>=c or b+c>=a:
    print("Triangle can be formed")
elif a+c>=b:
    print("Triangle can be formed")
else :
    print("Triangle can't be formed")

#18.Take a number and check whether it is a palindrome (using conditionals)
x=input("Enter the number : ")
rev=x[::-1]
if x==rev:
    print("The number is palindrome")
else:
    print("Not Palindrome")

#19.Create a simple calculator: (a)Input two numbers and an operator (+, -, *, /).(b)Perform operation using conditionals
 #(a)
a=float(input("Enter the first number :"))
b=float(input("Enter the second number: "))
c=input("Enter operator (+,-, *, /): ")
if c=="+":
    print("The sum of both number is: ",a+b)
elif c=="-":
    print("The Substraction of both number is: ", a-b)
elif c=="*":
    print("The multiplication of both number is: " ,a*b)
elif c=="/":
    print("The Division of both number is: ",a/b)
else:
    print("Invalid operator")














    














