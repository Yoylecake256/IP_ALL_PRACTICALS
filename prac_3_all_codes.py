#Question_1

n = int(input("Enter a number: "))
if n>0:
    print("Number is positive.")
elif n<0:
    print("Number is negative.")

#Question_2

a = int(input("Enter a number: "))
if a%2 == 0:
    print("The number is even. ")
else: 
    print("The number is odd.")

#Question_3
marks = int(input("Enter marks Max 100: "))
if marks > 100:
    print("Marks only max till 100")
elif marks >= 90:
    print("A grade")
elif marks >= 80 and marks < 90:
    print("B Grade")
elif marks >= 70 and marks < 80:
    print("C Grade")
else:
    print("D Grade")

#Question_4
age = int(input("Enter an number: "))
nation = input("Enter your Nationality: ")
if age >= 18:
    if n.lower() == "indian":
        print("Eligible to vote.")
    else:
        print("Not Eligible to Vote(Not Indian)")
else: 
    print("Not eligible to vote")

#Question_5
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the greatest number.")

#Question_6
year = int(input("Enter a year: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Question 7
num_1 = float(input("Enter a number(1): "))
num_2 = float(input("Enter a number(1): "))
op = input("Enter operator(+, -, *, /)")
if op == '+':
    print("Result: ", num_1 + num_2)
elif op == '-':
    print("Result: ", num_1 - num_2)
elif op == '/':
    if num_2 != 0:
        print("Result: ", num_1/num_2)
    else:
        print("ERR: Invalid format.")
elif op == '*':
    print("Result: ", num_1*num_2)
else:
    print("Invalid Format")

#Question_8
amt = float(input("Enter amount: "))
if amt >= 2000:
    disc = amt*0.20
    f_amt = amt-disc
    print("20% Discount")
elif amt == 1000:
    disc = amt*0.10
    f_amt = amt-disc
    print("10% Discount")
else:
    print("No Discount")

#Question_9
s1 = float(input("Enter Side_1: "))
s2 = float(input("Enter Side_2: "))
s3 = float(input("Enter Side_3: "))

if s1 == s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#Question_10
u = int(input("Enter a number: "))
k = int(input("Enter a number: "))
if u > k:
    print(f"{u} is greater than {k}")
elif k > u:
    print(f"{k} is greater than {u}")
else:
    print("Both are equal.")

if u % 2 == 0:
    print(f"{u} is even")
else:
    print("Number is odd")
if k % 2 == 0:
    print(f"{k} is even")
else:
    print("Number is odd")