# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples: 
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator (+): to join two or more tuples and to create a new tuple

# Create an empty tuple
empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Kemi', "Toyin")
brother = ('Abdul',) # Single-element tuple requires a trailing comma
# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brother
# How many siblings do you have?
print(f"I have {len(siblings)} siblings.")
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("Fatai")
siblings.append("Kunbi")
family_members = tuple(siblings)
print(family_members)
# Unpack siblings and parents from family_members
siblings = family_members[:3]
parents = family_members[3:]
print(f"Parents: {parents}\nSiblings: {siblings}")
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'mango', 'bananas')
vegetables = ('brocolli', 'spinach', 'carrots')
animal_products = ('steak', 'eggs', 'chicken')
food_stuff_tp = fruits+vegetables+animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[4:5])
# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# print(food_stuff_tp)
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)















