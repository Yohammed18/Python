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

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    if x1 == x2:
        raise ValueError("The x-coordinates of the two points cannot be the same; the slope is undefined.")
    
    return (y2 -y1) / (x2-x1)

print(f'Linear Slope = {round(calculate_slope((-1, -7),(2, 3)), 2)}')

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath 
def solve_quadratic_eqn(a, b, c):
    """
    Solve the quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    tuple: A tuple containing the two solutions (root1, root2).
           The solutions can be real or complex numbers.
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Compute the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return (root1, root2)

# Example usage:
a, b, c = 1, -3, 2  # Example coefficients for the equation x^2 - 3x + 2 = 0
roots = solve_quadratic_eqn(a, b, c)
print(f'The solutions are: {roots[0]} and {roots[1]}')

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(args):
    
    if isinstance(args, list):
        for i in args:
            print(i, end=" ")
            
print('\nList')
print_list([2,4,7,'123',1])
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list_1(item): 
    reverse_list = list()   
    for i in range(len(item)-1,-1,-1):
        reverse_list.append(item[i])
        
    return reverse_list
print('\n')
print(reverse_list_1([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list_1(["A", "B", "C"]))
# ["C", "B", "A"]


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(cap_list):
    
    for i in range(len(cap_list)):
        cap_list[i] = cap_list[i].capitalize()

    print(cap_list)
    
capitalize_list_items(['potato', 'tomato', 'mango', 'milk'])

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(item, food):
    item.append(food)
    return item

print('\n')
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    """
    Count the number of even and odd digits in a positive integer.

    Parameters:
    num (int): A positive integer.

    Returns:
    str: A formatted string with the counts of even and odd digits.
    """
    even_count = 0
    odd_count = 0
    
    # Ensure num is positive
    if num < 0:
        raise ValueError("The number must be positive.")
    
    for i in range(num+1):
        if i%2 == 0:
            even_count+=1
        else:
            odd_count+=1
    
    return f'\nThe number of odds are {odd_count}.\nThe number of evens are {even_count}.'
            
print(evens_and_odds(100))








