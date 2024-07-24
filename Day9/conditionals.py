# Conditional flow in programming allows you to execute different blocks of code based on certain conditions. This is typically achieved using if, else, and elif (else if) statements. Logical operators (and, or, not) are often used in conjunction with these statements to combine multiple conditions.

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: \n"))

if age > 18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = int(input("Enter your age: \n"))
your_age = 30

if my_age == your_age:
    print("We are the same age.")
elif my_age < your_age:
    diff = your_age - my_age
    if diff == 1:
        print(f'You are {diff} year older than me.')
    else:
        print(f'You are {diff} years older than me.')
else:
    diff = my_age - your_age
    print(f"I am {diff} year older than you.") if diff == 1 else print(f"I am {diff} years older than you.")
    
    
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter first number\n")) 
b = int(input("Enter second number\n")) 

if a > b:
    print(f'{a} is greater than {b}.')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}.')
    
# Write a code which gives grade to students according to theirs scores:
grade = int(input("Enter grade number:\n"))

if  grade >= 80:
    print("A")
elif grade >= 70:
    print("B")   
elif grade >= 60:
    print("C")     
elif grade >= 50:
    print("D")     
elif  grade < 50:
    print("F")    
    
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autumn = ['Septmber', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
    
season = input('Enter season:\n')

if season in autumn:
    print('Autumn')
elif season in winter:
    print('Winter')
elif season in spring:
    print('Spring')        
elif season in summer:
    print('Summer')
else:
    print("You did not enter the correct month.")   

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')  
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter a fruit:\n')

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
















