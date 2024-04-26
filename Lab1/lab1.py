import math

# 1- Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(last_name + " " + first_name)

# 2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.

# n = int(input("Enter a number"))
# result = n + int(str(n) * 2) + int(str(n) * 3)
# print(result)

# 3-Write a Python program to print the following here document. Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print(
#     """
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
#      """
# )

# 4- Write a Python program to get the volume of a sphere with radius 6.

# radius = 6
# volume = 4 / 3 * math.pi * (radius**3)
# print(volume)

# 5-- Write a Python program that will accept the base and height of a triangle and compute the area.

# base = int(input("Enter the base of the triangle: "))
# height = int(input("Enter the height of the triangle: "))
# area = 0.5 * base * height
# print(f"Area = {area}")

# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# max_rows = 5
# for i in range(1, max_rows * 2):
#     if i <= max_rows:
#         for j in range(i):
#             print("*", end=" ")
#     else:
#         for j in range(max_rows * 2 - i):
#             print("*", end=" ")
#     print()

# 7- Write a Python program that accepts a word from the user and reverse it.

# word = input("Enter one word: ")
# reversed_word = word[::-1]
# print(reversed_word)

# 8-Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# max_number = 6
# for i in range(max_number):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# 9-Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# def fibonacci_series(limit):
#     a, b = 0, 1
#     fibonacci_list = []

#     while a <= limit:
#         fibonacci_list.append(a)
#         a, b = b, a + b
#     return fibonacci_list


# limit = 50
# print(fibonacci_series(limit))

#  Python program that accepts a string input and calculates the number of digits and letters in that string:

# sentence = input("Enter a string: ")

# num_of_digits = 0
# num_of_letters = 0

# for char in sentence:
#     if char.isdigit():
#         num_of_digits += 1
#     elif char.isalpha():
#         num_of_letters += 1

# print("Number of digits is ", num_of_digits)
# print("Number of letters is ", num_of_letters)
