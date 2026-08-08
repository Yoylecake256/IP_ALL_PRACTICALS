#Quesrtion_2
a = 23.23
print(type(a))
print(a)
b = "23.23"
print(type(b))
print(b)

#Question_3
PI = 3.1415
GRAVITY = 9.8
MAX_USERS = 100
print("Initial values: ", PI, GRAVITY, MAX_USERS)

#Question_4
integer_val = 25
float_val = 12.5
string_val = "Johnny.B.Goode"
bool_val = True
print("\nInteger Value: ", integer_val)
print(type(integer_val))

print("\nFloat Value: ", float_val)
print(type(float_val))

print("\nString Value: ", string_val)
print(type(string_val))

print("\nBoolean Value: ", bool_val)
print(type(bool_val))

#Question_5
age = input("Enter age: ")
marks = input("Enter marks: ")
#Display original type
print("\nBefore Conversion")
print(type(age, marks))

#Changing type of value.
age = int(age)
marks = float(marks)
total_marks = marks + 10
future_age = age + 5

print("\nAfter Conversion: ", age, marks)
print("Total marks: ", total_marks)
print("Age in 5 years: ", future_age)

#Question_6
n1 = 10
f1 = 45.39
res = n1 + f1
print(res)
print("Type: ", type(res))
x = 15
y = "YAAY!"
#print(x + y) <--- Yields Error

#Question_7
a = 10
b = 10
print("a id: ", id(a))
print("b id: ", id(b))
a = 20
b = 10
print("\nAfter Converstion: ")
print("a: ", a, "id: ", id(a))
print("b: ", b, "id: ", id(b))

#Question_8

#Method_1
i = 10
j = 20
print("\nBefore Swap (1st Method)", i, j)
temp_i = i
i = j
j = temp_i
print("\nAfter Conversion(Method 1): ", i, j)
#Method_2
q = 100
r  = 300
print("\nBefore Conversion(Method 2)", q, r)
q,r = r,q
print("\nAfter Conversion:", q, r)

#Question_9

v = input("Enter First Value: ")
z = input("Enter Second Value: ")
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

if is_float(v) and is_float(z):
    v = float(v)
    z = float(z)
    result_1 = v + z
    print("\nBoth inputs are numeric.")
    print("Sum: ", result_1)
elif isinstance(v, str) and isinstance(z, str):
    result_1 = v + z
    print("\nConcatenation: ", result_1)

else:
    print("\nInvalid Output types: Add string OR Integer on BOTH sides")

#Question_10
age = 20
marks_1 = 75
is_adult = age>18
is_pass = marks>50
print("Is Adult: ", is_adult, "Is Pass", is_pass)
if is_adult and is_pass:
    print("Eligibe for admission.")
else:
    print("THOU ART UNWORTHY!")

#Question_11
cel = float(input("Enter temp in celcius: "))
fahr = (cel * 9/5) + 32
print(f"\nTemperature in Fahrenheit", fahr)