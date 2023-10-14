import math

first_number = 1
first_name = 'Michal Jordan'
first_float = 23.123
isTrue = False
first_list = ['Jackson', 1.2, 4, True]
first_set = {1, 3, 3, 2, 1, 5, 1.3}
first_tuple = ("apple", "banana", "cherry", "banana", "vinegar")
print(first_number)
print(type(first_number))
print(type(isTrue))
print(type(first_name))
print(type(first_float))
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
print(type(first_list))
print(first_list)
# A set is a collection which is unordered, unchangeable*, and un-indexed.
# Sets are written with curly brackets.
print(type(first_set))
print(first_set)
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
print(type(first_tuple))
print(first_tuple)

num = 7.5
print(type(int(num)))

num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))

# Formatting Strings
tempNum = 12
print(f"My numbers are {tempNum}")
print("The sum of {} and {} is equal to {}".format(tempNum, num, num + tempNum))

associate_name = "Jesse Pinkman"
associate_number = 399058
print("Dear {}, your associate number is: {}".format(associate_name, associate_number))

x = 6
y = 2
z = 7

print(f"{x} plus {y} equals {x + y}")
print(f"{z} divided to the floor of {y} equals {z//y}")
print(f"{z} modulo of {y} equals {z%y}")
print(f"{x} to the power of {y} equals {x**y}")
print(f"{x} to the power of 3 equals {x**3}")
print(f"the square root of {x} is {x**0.5}")

# Print on the screen the floor division of the following two numbers: 874 divided by 27
print(874//27)
# Print on the screen the modulus of 456 divided by 33
print(456%33)
# Calculate and print the square root of 783
print(783**0.5)
# Round the result of the division 10/3 to a number with 2 decimal places, and print the rounded value on the screen.
print(round(10/3,2))
# Round the number 10.676767 to the nearest integer, and print the result.
num = 10.676767
print(round(num))
# Calculate the square root of 5, and print the result rounded to 4 decimal places.
print(round(math.sqrt(5),4))

