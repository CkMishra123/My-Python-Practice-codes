#1.finding elements from datetime format
from datetime import datetime
x=datetime(2025,10,29,20,24,45)
y=x.day
b=x.second
c=x.hour
print(y,b,c)

#2.Using strftime() to change date/time to formatted string
from datetime import datetime
x=datetime(2025,10,29,20,24,45)
print(x.date())
print(x.time())
print(x.strftime("%d-%m-%y %H:%M AM"))

#3.Using strptime to change from string to datetime object
from datetime import datetime
x=datetime(2025,10,29,20,24,45)
print(datetime.strptime("20230529", "%y%m%d"))

#4.Substracting dates from datetime module
from datetime import datetime
d1=datetime(2026,5,26)
d2=datetime(2026,5,20)
diff=d1-d2
print(diff)

#5.Adding Days to the existing
from datetime import datetime, timedelta
today=datetime.now()
future=today+timedelta(days=5)
print(future)

#6.Write a program to display the current date in the format:Monday, 26 May 2026
from datetime import datetime
now=datetime.now()
print(now.strftime("%A, %d %B %Y"))

#7.Convert the string "2026/12/25 18:45" into a datetime object using strptime().
from datetime import datetime

x = datetime.strptime("2026122518:45", "%Y%m%d%H:%M")
print(x)
formatted=x.strftime("%y/%m/%d %H:%M")
print(formatted)

#8.Write a program to calculate the number of days between "01-01-2026" and "26-05-2026".
from datetime import datetime

d1=datetime(2026,1,1)
d2=datetime(2026,5,26)
diff=d2-d1
print(diff)

#9.Write a program to add 45 days and 5 hours to the current date and time.
from datetime import datetime, timedelta
today=datetime.now()
future=today+timedelta(days=5,hours=5)
print(future)


#10.Take a date from user in "dd-mm-yyyy" format and print the weekday name of that date.
from datetime import datetime
x=input("Enter the date (dd/mm/yyyy): ")
y=datetime.strptime(x, "%d/%m/%Y")
print(y.strftime("%A"))

#11.Convert current datetime into the format:2026-05-26 | 09:45 PM
from datetime import datetime
today=datetime.now()
new_formate=datetime.strftime(today, "%Y-%m-%d | %H:%M PM")
print(new_formate)

#12.Write a program to find how many hours are remaining until New Year from current datetime.


#16.Write a program to calculate a person's age in days using their birthdate.
from datetime import datetime,timedelta
bday=datetime(2003,8, 18)
date2=datetime.now()
diff=date2-bday
years=diff.days//365
days=diff.days%365
print("Total Years: ",years ,"Total Days: ",days, sep='\n')

#17.Write a program to check whether a given year is a leap year using the datetime module.
from datetime import datetime
x=int(input("Enter the year (YYYY) : "))
if (x%400==0) or ( x%4==0 and x%100!=0):
    print("The year is leap year")
else:
    print("Not Leap year")

#18.Write a program to find the difference in minutes between two times entered by the user
from datetime import datetime
x=input("Enter the first date (dd-mm-yyyy): ")
d1=datetime.strptime(x, "%d-%m-%Y")
y=input("Enter the second date (dd-mm-yyyy): ")
d2=datetime.strptime(y, "%d-%m-%Y")
diff=d2-d1
print(diff)


#19.Write a program to print the current month name and total number of days passed in the current year.
from datetime import datetime
today=datetime.now()
x=datetime.strftime(today, "%B")
str_day=datetime(today.year,1,1)
diff=(today-str_day).days+1
print(x, diff, sep="\n")










