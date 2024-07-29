# PYTHON DECORATORS - A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Explain the difference between 
# map() - applies a function to each item in a list
# filter() - keeps only the items that meet a certain condition.
# reduce() -  combines all items in a list into one value.
# Higher-Order Function: Can accept or return other functions
# Closure: A function that retains access to variables from its creation environment.
# Decorator: A higher-order function that modifies or enhances other functions.

# Define a call function before map, filter or reduce, see examples.
def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5, 6]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))

print('')
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

print('')
from functools import reduce

def add(x, y):
    return x + y

sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers,"\n") 

# Use for loop to print each country in the countries list.
print("\n**********Countries*********")  
for country in countries:
    print(country)
print("\n**********Names*********")  
for name in names:
    print(name)
print("\n**********Numbers*********")  
for number in numbers:
    print(number)

# Use map to create a new list by changing each country to uppercase in the countries list
def upper_case(x):
    return x.upper()
country_list = map(upper_case, countries)
print('\n')
print(list(country_list))
# Use map to create a new list by changing each number to its square in the numbers list
def square(x):
    return x ** 2
number_list = map(square, numbers)
print(list(number_list))
# Use map to change each name to uppercase in the names list
name_list = map(upper_case, names)
print(list(name_list))

# Use filter to filter out countries containing 'land'.
def contain_land(value):
    if 'land' in value:
        return True
    return False

print('\n')
filter_country = filter(contain_land, countries)
print(list(filter_country))
# Use filter to filter out countries having exactly six characters.
def char_count(value):
    if len(value) == 6:
        return True    
    return False

filter_char = filter(char_count, countries)
print(list(filter_char))
# Use filter to filter out countries containing six letters and more in the country list.
def char_count_more(value):
    if len(value) >= 6:
        return True    
    return False

filter_char_more = filter(char_count_more, countries)
print(list(filter_char_more))
# Use filter to filter out countries starting with an 'E'
def country_start_e(value):
    if value[0] == 'E':
        return True
    return False

country_e = filter(country_start_e, countries)
print(list(country_e))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
value = list(map(upper_case, countries))

final_value = list(filter(char_count, value))
print(final_value)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(parameter):
     return isinstance(parameter, str)

is_string = ['Mikal', 'James', 1, 3,5, 'Bool']
check_string = list(filter(get_string_lists, is_string))
print(check_string)


# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def country_sentece(x,y):
    return f'{x}, {y}'


print_sentence = reduce(country_sentece, countries)

print(print_sentence)

if ', ' in print_sentence:
    final_sentence = print_sentence.rsplit(', ', 1)
    final_sentence = f'{final_sentence[0]}, and {final_sentence[1]}'


print(f'{final_sentence} and north European countries.')

























