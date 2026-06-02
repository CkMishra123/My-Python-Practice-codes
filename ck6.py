#6.Write a program that keeps asking the user to enter a password until they type "python123", then print "Access Granted" and stop the loop.

while True:
    password=input("Enter the password")
    if password=="python123":
        print("Access Granted")
        break
    else:
        print("Wrong Password! ")

