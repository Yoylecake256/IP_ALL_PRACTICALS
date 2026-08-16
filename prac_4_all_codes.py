#Question_1.
print("Number from 1 to 10.")
for i in range (1, 11):
    print(i)
#Modifying to only show even nos.
print("\nEven Numbers.")
for i in range (2, 11, 2):
    print(i)

#Question_2.
i = 1
print("While Loop.")
while i<= 10:
    print(i)
    i = i+1
print("\nFor Loop.")
for i in range (1, 11):
    print(i)

#Question_3.
n = int(input("How many numbers: "))
sum = 0
for i in range(n):
    num = int(input("Enter a number: "))
    sum = sum+num
avg = sum/n
print("Sum: ", sum)
print("Average: ", avg)

#Question_4.
##For Loop
print("\nFor Loop")
n = int(input("Enter a number: "))
fact = 1
for i in range (1, n+1):
    fact = fact*i
print("Factorial: ", fact)

##While Loop.
n = int(input("Enter a number: "))
fact = 1

i = 1
while i <= n:
    fact = fact*i
    i = i+1
print("Factorial: ", fact)

#Question_5.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#Question_6.
n = int(input("Enter a number"))
original = n
rev = 0
while n > 0:
    digit = n%10
    rev = rev*10 + digit
    n = n // 10
print("Reversed number: ", rev)
if original == rev:
    print("Palindrome.")
else:
    print("Not a Palindrome.")

#Question_7
n = int(input("Enter a number: "))
total = 0
even = 0
odd = 0
while n>0:
    digit = n%10
    total = total + 1
    if digit % 2 == 0:
        even = even + 1
    else:
        n = n//10
print("Total digits: ", total)
print("Even digits: ", even)
print("Odd digits: ", odd)

#Question_8.
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Composite Number")

#Question_9.
n = int(input("Enter a number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a+b
    a = b
    b = c

#Question_10.
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
