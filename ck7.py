#7.Write a program to check whether a number entered by the user is prime or not using a for-else loop.

num = int(input("Enter a number: "))

if num > 1:                       # prime numbers are greater than 1
    for i in range(2, num):

        if num % i == 0:          # if divisible, not prime
            print(num, "is not a prime number ❌")
            break                 # stop checking further
    else:
        print(num, "is a prime number ✅")  # runs only if loop didn't break
else:
    print("Number should be greater than 1.")
