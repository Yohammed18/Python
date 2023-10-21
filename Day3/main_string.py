text = "We are going to learn six method today!"
print(text)
# upper case
print(text.upper())
print(type(text.upper()))
# lower case
print(text.lower())
# split a string into a list based on the empty space between each word
print(text.split())
# split string into a list by inserting a value into the split method
print(text.split('are'))
# join method
a = 'Learning'
b = 'Python'
c = 'is'
d = 'amazing.'
e = " ".join([a, b, c, d])
print(e)
# find() vs index() - the find() method will return -1 if the element inserted is not found
result = text.find('q')
print(result)
# replace() is use to replace an element by passing 2 parameters.
result = "1/2/3/4/5/6/7/8/9".replace('/', ' ')
print(result)
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple", "is", "better", "than", "complex."]
word_list = " ".join(word_list)
print(word_list)

sentence = "If the implementation is hard to explain, it might be a bad idea."
sentence = sentence.replace('hard', 'easy')
sentence = sentence.replace('bad', 'good')
print(sentence)