# main.py file
import module
print(module.generate_full_name('James', 'Brown')) # James Brown

# Like other programming languages we can also import modules by importing the file/function using the key word import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

from random import random, randint
print(round(random()*10))


# Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    """
    Generate a random six-character user ID consisting of digits and letters.
    
    Returns:
    str: A randomly generated six-character user ID.
    """
    string_generator = '0123456789abcdefghijklmnopqrstuvwxyz'
    user_id = ""
    
    for i in range(6):
        num = randint(0, len(string_generator)-1)
        user_id += string_generator[num]
        
    return user_id
        
print(random_user_id(), "\n")
# # Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# def user_id_gen_by_user():
#     """
#     Generate a list of random user IDs based on user input for the number of characters per ID and the number of IDs to generate.
#
#     Param : number_char, number_id
#
#     Returns:
#     list: A list of randomly generated user IDs.
#     """
#     number_char = int(input("Enter the number of characters:\n"))
#     number_id = int(input("Enter number of IDs:\n"))
#     string_generator = '0123456789abcdefghijklmnopqrstuvwxyz'
#
#     ids = list()
#
#
#     for _ in range(number_id):
#         id = ''
#         for _ in range(number_char):
#             num = randint(0, len(string_generator)-1)
#             id += string_generator[num]
#
#         ids.append(id)
#
#     return ids;
#
# print(user_id_gen_by_user())

# # Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# def rgb_color_gen():
#     """
#     Generate rgb colors (3 values ranging from 0 to 255 each
#
#     Returns:
#     str: A string representing the RGB color in the format 'rgb(R, G, B)'.
#     """
#     rbg_list = list()
#     for _ in range(3):
#         num = randint(0,255)
#         rbg_list.append(num)
#
#     return f'\nRBG\nrgb({rbg_list[0]},{rbg_list[1]},{rbg_list[2]})'
#
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
