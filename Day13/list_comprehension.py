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

# Lambda Function -  It can take any number of arguments, but can only have one expression.

# To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i < 1]
print()
print(negative_zero)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lists = [z for i in list_of_lists for x in i for z in x]
print()
print(lists)
print('\n')
# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
 
 

list_of_tuples = [
    tuple(
        i**j if j > 0 else i 
        for j in range(7)
    )
    for i in range(11)
]

print(list_of_tuples)












