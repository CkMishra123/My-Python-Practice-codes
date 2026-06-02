#9.Write a program to reverse a number (example: input 1234 → output 4321) using a while loop.

num = int(input("Enter a number: "))
rev = 0  # variable to store reversed number

while num > 0:
    digit = num % 10          # get last digit
    rev = rev * 10 + digit    # add digit to reversed number
    num = num // 10           # remove last digit from original number

print("Reversed number is:", rev)
