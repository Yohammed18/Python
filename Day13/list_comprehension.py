# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.
# [i for i in iterable if expression]
# generate a list of characters
char_list = [i for i in 'Lebron']
print(char_list)
print()
# generate a List of numbers
num_list = [i for i in range(10)]
print(num_list, "\n")
# generate mutliples of 2s
multiple_of_two = [2 * i for i in range(1,6)]
print(multiple_of_two)



