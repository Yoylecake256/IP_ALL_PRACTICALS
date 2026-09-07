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

##Question_5
numbers = [10, 20, 30, 40]
numbers.append(40)
print(f"After Append: {numbers}")

numbers.insert(1, 15)
print(f"After insert: {numbers}")


##Question_6
numbers = [10, 20, 30, 40]

numbers.remove(30)
print("After remove: ", numbers)

numbers.pop()
print("After pop: ", numbers)

try:
    numbers.remove(100)
except ValueError:
    print("ERR: Element not found.")


##Question_7
numbers = [10, 20, 30, 40]

numbers.sort()
print("Ascending Order: ", numbers)

numbers.sort(reverse=True)
print("Descending Order: ", numbers)

numbers.reverse()
print("Reversed: ", numbers)

##Question_8
numbers = [10, 20, 30, 20 ,40]

print("Count of 20: ", numbers.count(20))
print("Index of 30: ", numbers.index(30))

try:
    numbers.index(100)
except ValueError:
    print("ERR: Element not found.")

##Question_9

matrix = [[1, 2],
          [3, 4]]
print(matrix)
print("Element: ", matrix[0][1])
print("Element: ", matrix[1][0])

##Question_10
numbers = [10, 20, 30, 40]
t = tuple(numbers)
print("TupleL ", t)
fruits("Apple", "Banana", "Orange")

l = list(fruits)
print("list", l)
l.append("Orange")
print("Modified List: "l)

##Question_11
numbers = [10, 20, 30, 40]
fruits = ("Apple", "Banana", "Orange")

print("List Elements: ")
for i in numbers:
    print(i)

sum = 0
for i in numbers:
    sum += i

print("Sum = ", sum)
print("\nTuple Elements: ")
for i in fruits:
    print(i)

##Question_12
cart = ["Milk", "Bread"]
categories = ("Food", "Beverages", "Snacks")
print("Categories", categories)
cart.append("Eggs")
print("Shopping Cart: ", cart)
print("Total Items: ", len(cart))
