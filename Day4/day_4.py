# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(words)
print(result)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
x,y,z = "Coding", "For", "All"
# Declare a variable named company and assign it to an initial value "Coding For All".
company = f"{x} {y} {z}"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[0:6])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)
print(company.find("Coding"))
print(company.index("Coding"))
# Replace the word coding in the string 'Coding For All' to Python.
split_list = company.split()
print(split_list)
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
split_word = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")
print(split_word)
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Use the new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")
# Use a tab escape sequence to write the following lines
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libaries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(libaries)
print(result)




















