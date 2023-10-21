# Tuples are immutable and take less memory space (efficiency), damage-prof
my_tuple = ('dog', 'cat', 'fish')
# casting tuple into a list
list_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))
print(type(list_tuple))

a, b, c = my_tuple
print(a, b, c)

t = 1, 2, 3, 1
print(len(t))
print(t.count(1))
print(t.index(2))
# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(my_tuple.count(2))

# Convert the following tuple to a list, and store it in a variable called my_list.
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
my_list = list(my_tuple)
# Extract the elements of the following tuple into four variables: a, b, c, d
my_tuple = (1, 2, 3, 4)
a, b, c, d = my_tuple
