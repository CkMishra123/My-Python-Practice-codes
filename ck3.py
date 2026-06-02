#3.Write a program to print numbers from 1 to 30 but skip all numbers divisible by 3 using the continue statement.

for i in range(1,31):
    if i%3==0:
        continue
    print(i)
