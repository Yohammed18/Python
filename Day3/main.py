# Declare your age as integer variable
age = 24
# Declare your height as a float variable
height = 5.11
# Declare a variable that store a complex number
complex_num = 1j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5*base*height
print(f"The area of the triangle is {round(area)}")
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a+b+c
print(f"The perimeter of the triangle is {perimeter}")
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter lenght: "))
width = int(input("Enter width: "))
area_rect = length*width
perimeter_rect = 2 * (length+width)
print(f"Rectangle: \nArea: {area_rect}\nPerimeter: {perimeter_rect}")
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
input_radius = int(input("Enter a radius: "))
circle_area = 3.14 * (input_radius**2)
circle_perimeter = 2 * 3.14 * input_radius
print(f"Cirlce: \nArea: {circle_area}\nPerimeter: {circle_perimeter}")
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = y_intercept/slope
print(f"Slope: {slope}. Y-Intercept {y_intercept}. X-Intercept {x_intercept}")
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python")
print("on" in "dragon")
jargon = "I hope this course is not full of jargon"
# There is no 'on' in both dragon and python
print("jargon" in jargon)
print(not "on" in "python")
print(not "on" in "dragon")
# Find the length of the text python and convert the value to float and convert it to string
text_length = str(float(len('python')))
print(text_length)
print(type(text_length))
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 7
if num%2 == 0:
    print("Even number")
else:
    print("Odd number")
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7/3 == int(2.7))
# Check if type of '10' is equal to type of 10
print('10' == 10)
# Check if int('9.8') is equal to 10
print('9.8' == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter hours:\n")
rate = input("Enter rate:\n")
earnings = int(hours)*int(rate)
print(f"Your weekly earning is {earnings}")
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input("Enter number of years you have lived:\n"))
total = (60*60*24*365) * year
print(f"You have lived for {total} seconds.")
# Write a Python script that displays the following table
print("""1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125""")













