# Functions are reusable blocks of code designed to perform a specific task. They help in organizing code, making it more modular, readable, and easier to maintain. Functions can take inputs, process them, and return outputs.

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(x,y):
    return x+y
print(f'Sum = {add_two_numbers(3,3)}\n')

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return 3.14*(radius**2)
print(f'Area = {area_of_circle(3)}\n')

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):  # Check if arg is an int or float
            total += arg
        else:
            return f"Error: '{arg}' is not a number. Please provide only numeric values."
    return total    
print(add_all_nums(1,23,4,5),"\n") 

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32
print(f'Fahrenheit = {convert_celsius_to_fahrenheit(10)}\n')

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    autumn = ['Septmber', 'October', 'November']
    winter = ['December', 'January', 'February']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']

    if month in autumn:
        return 'Autumn'
    elif month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'   
    elif month in summer:
        return 'Summer'
    else:
        return 'The month enter is not valid.' 

print(f'Season = {check_season('October')}')






















