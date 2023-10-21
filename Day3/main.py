# Program a text analyzer with python
hello_world = "Hello World"

print(hello_world.index(' '))
print(hello_world[1])
print(hello_world[-4])
print(hello_world.index("lo ", 0, 9))
# Find and display on the screen which character occupies the fifth position within the following word
word = "computer"
result = word[4]
print(result)

# SLICE
text = "ABCDEFGHIJKLM"
fragment = text[2:10:2]
print(fragment)


# Find and display the index of the first occurrence of the word "practice" in the following sentence:
sentence = "In theory, theory and practice are the same. In practice, they are not."
print(sentence.index("practice"))

# Find and display the index of the last occurrence of the word "practice" in the following sentence
sentence = "In theory, theory and practice are the same. In practice, they are not."
print(sentence.rindex("practice"))
# Extract the first word of the following sentence using slicing, and display it on the screen:
sentence = "Controlling complexity is the essence of programming"
print(sentence[0:11])
# Take every third character starting from the ninth to the end of the sentence, and print the result.
sentence = "Never trust a computer you can't throw out a window"
print(sentence[8::3])

sentence = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
print(sentence[::-1])
print(sentence.upper())
print(sentence.lower())
