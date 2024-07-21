# Open the python interactive shell and do the following operations. The operands are 3 and 4.
print(3+4)# addition(+)
print(3-4)# subtraction(-)
print(3*4)# multiplication(*)
print(3%4)# modulus(%)
print(3/4)# division(/)
print(3**4)# exponential(**)
print(3//4)# floor division operator(//)
#  Write strings on the python interactive shell. The strings are the following: Your name, Your family name, Your country, I am enjoing the 30 days of python challenge
print("Billy")
print("Alli")
print("United States")
print("I am enjoing the 30 days of python challenge")
# Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Kobe', 'Python', 'Italy']))
print(type("Billy"))
print(type("Alli"))
print(type("United States"))
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

print("\nData Structures")
temp_list = ['Kobe', 'Python', 'Italy']
temp_set = {1,1,3,2,5,"29"}
temp_tuple = (23,12,4j, "Hello", 'world')
temp_dict = {
    1: "Lebron",
    2: "James"
}
print(type("Kobe" in temp_list))
print(type(temp_list))
print(temp_list)
print(type(temp_set))
print(temp_set)
print(type(temp_tuple))
print(temp_tuple)
print(type(temp_dict))
print(temp_dict)

# Find an Euclidian distance between (2, 3) and (10, 8)
import math

# Define the coordinates
point1 = (2, 3)
point2 = (10, 8)

# Calculate the Euclidean distance
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

print("The Euclidian distance between {} and {} is {}.".format(point1, point2, round(distance, 2)))