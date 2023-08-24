num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1==num2:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
if num1<num2:
    print("Second number is greater than first number")
else:
    print("First number is greater than second number")
if num1<=num2:
    print("Second number is greater than or equal to first number")
else:
    print("First number is greater than or equal to second number")
if num1>1000 and num2>1000:
    print("Both numbers are big")
    print("big_numbers is set to True")
else:
    print("Both numbers are not big")
    print("big_numbers is set to False")