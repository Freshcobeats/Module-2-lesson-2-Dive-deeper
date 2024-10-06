#task 1: Identify the greatest
#ask user to input 3 numbers 
num1=int(input("please input first number(1-20):"))
num2=int(input("please input second number(1-20):"))
num3=int(input("please input third number(1-20):"))


if (num1>=num2) and (num1>=num3):
    greatest=num1
elif (num2>=num1) and (num2>=num3):
    greatest=num2
else:
    greatest=num3

print("the greatest number is", greatest )

#task 2: Identify the lowest
#ask user to input 3 numbers 
num1=int(input("please input first number(1-20):"))
num2=int(input("please input second number(1-20):"))
num3=int(input("please input third number(1-20):"))


if (num1<=num2) and (num1<=num3):
    lowest=num1
elif (num2<=num1) and (num2<=num3):
    lowest=num2
else:
    lowest=num3

print("the greatest number is", lowest )