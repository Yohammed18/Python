# Day 2: 30 Days of python programming
first_name = "Lebron"
second_name = "James"
full_name = first_name+" "+second_name
country = "Nigeria"
city = "Chicago"
age = 35
year = 2024
is_married = False
is_true = True
is_light_on = False
x, y, z = "Martin", "Luther", "King"

# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(second_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
# Using the len() built-in function, find the length of your first name
print()
print(len(first_name))
print(len(first_name) == len(second_name))
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product Divide num_one by num_two and assign the value to a variable division Use modulus division to find num_two divided by num_one and assign the value to a variable remainder Calculate num_one to the power of num_two and assign the value to a variable exp Find floor division of num_one by num_two and assign the value to a variable floor_division
num_one = 5
num_two = 4
total = num_one+num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one//num_two
# The radius of a circle is 30 meters
import math
radius = 30
area_of_circle = math.pi * (radius**2)
circum_of_circle = (math.pi**2) * radius 

input_radius = int(input("Enter a radius value: "))
print("Area of a circle is: {}".format(round(math.pi * (input_radius**2))))




