##Question_1

#List of numbers
numbers = [10, 20, 30, 40]

#Tuple of strings
froots = ("Apple", "Banana", "Mango")

print(numbers)
print(froots)

print(type(numbers))
print(type(froots))


##Question_2

numbers = [10, 20, 30, 40]
items = ("A", "B", "C", "D")

print("\nFirst: ", numbers[0], items[0])
print("Last: ", numbers[-1], items[-1])
print("Middle: ", numbers[2], items[2])


##Question_3
numbers = [10, 20, 30, 40, 50]
items = ("A", "B", "C", "D")
print("\n", numbers[:3])
print(numbers[-2:])
print(numbers[::2])

print(items[:3])
print(items[-2:])
print(items[::2])

##Question_4
numbers = [10, 20, 30, 40]
numbers[1] = 50
print("\n",numbers)

items = ("A", "B", "C", "D")
#items[1] = "X" ##This gives an error!

