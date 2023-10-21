from typing import Dict, List

my_dict = {
    'fname': "Mohammed",
    'lname': "Jeffery",
    'height': 1.76,
    'weight': 240
}

print(my_dict)
value = my_dict['height']
print(value)

print(my_dict.keys())

num_dic = {1: 'a', 2: 'b'}
print(num_dic)
num_dic[3] = 'c'
num_dic[2] = num_dic[2].upper()

print(num_dic)
print(num_dic.items())

# EXERCISE
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist

my_dict = {'name': 'Karen', 'surname': 'Jurgens', 'age': 35, 'occupation': 'Journalist'}
print(my_dict)
# Use print to returns the second item of the list called points2, inside the following dictionary.
my_dict: dict[str, dict[str, int] | dict[str, list[int] | int] | str] = {"values_1": {"v1": 3, "v2": 6}, "points": {"points1": 9, "points2": [10, 300, 15]}}
print(my_dict["points"]["points2"][1])
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict["country"] = "Colombia"
my_dict["age"] = 36
my_dict["occupation"] = "Editor"
print(my_dict)


