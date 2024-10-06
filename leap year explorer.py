#task 1:leap year checker
#user inputs a year to determine if it is a leap year

year=int(input("Please enter a year:"))

if year %4 ==0 and (year %100!=0 or year%400==0):
    print("true")
else:
    print("false")