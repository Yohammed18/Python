# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# Create an empty dictionary called dog
dog = {}
print(type(dog))
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Wilson'
dog['color'] = 'Black'
dog['breed'] = 'Sheppard'
dog['legs'] = 4
dog['age'] = 7
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': "Jonathan",
    'last_name' : "Smith",
    'gender' : 'male',
    'age' : 35,
    "maritual_status": 'single',
    'skills' : ['Software Developer', 'Mechanic'],
    'country' : 'United States',
    'city' : 'Chicago',
    'address' : '620 John Paul Jones'
}
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(f"Skills: {student['skills']}\nData type: {type(student['skills'])}")
# Modify the skills values by adding one or two skills
# temp = list(student['skills'])
# temp.append('Reading')
# temp.append('Writing')

# student['skills'] = temp
# print(student)
new_skills = ["Machine Learning", "Deep Learning"]
student['skills'].extend(new_skills)
print(student)
# Get the dictionary keys as a list & Get the dictionary values as a list
print("Keys = {}.\nValues = {}".format(student.keys(), student.values()))
# Change the dictionary to a list of tuples using items() method
list_tuple = student.items()
print(list_tuple)
print(type(list_tuple))
# Delete one of the items in the dictionary
del student['address']
print(student)
# Delete one of the dictionaries
del student
