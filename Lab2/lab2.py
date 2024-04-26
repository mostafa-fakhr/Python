import random

# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:You may create a new list or modify the passed in list.

# def reduce_adjacent_duplicates(input_list):
#     new_list=[]
#     for i in range(len(input_list)):
#         if i==0 or input_list[i]!= input_list[i-1]:
#             new_list.append(input_list[i])
#     return new_list


# def divide_string(string):
#     length = len(string)
#     midpoint = length // 2

#     if length % 2 == 0:
#         front_half = string[:midpoint]
#         back_half = string[midpoint:]
#     else:
#         front_half = string[: midpoint + 1]
#         back_half = string[midpoint + 1 :]

#     return front_half, back_half


# def merge_strings(a, b):

#     # Divide strings a and b into front and back halves
#     a_front, a_back = divide_string(a)
#     b_front, b_back = divide_string(b)

#     result = a_front + b_front + a_back + b_back

#     return result

# 3-Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

# def are_all_unique(numbers):
#     unique_numbers = set(numbers)
#     return len(numbers) == len(unique_numbers)


# 4-Given unordered list, sort it using algorithm bubble sort
# ( read about bubble sort and try to implement it)

# def bubble_sort(arr):
#     array_length = len(arr)
#     for i in range(array_length - 1):
#         for j in range(0, array_length - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 5- Gusses game
# ● Your game generates a random number and gives only 10 tries for the user toguess that number.


# def guessing_game():
#     play_again = True
#     while play_again:
#         number = random.randint(1, 100)
#         attempts = 0
#         prev_guesses = set()

#         while attempts < 10:
#             guess = input("Enter your guess (between 1 and 100): ")

#             if not guess.isdigit():
#                 print("Please enter a number.")
#                 continue
#             guess = int(guess)

#             if (guess < 1) or (guess > 100):
#                 print("Number out of range. Enter a number between 1 and 100.")
#                 continue

#             if guess in prev_guesses:
#                 print("You already entered that number. Try another one.")
#                 continue

#             prev_guesses.add(guess)
#             attempts += 1

#             if guess == number:
#                 print(f"Congratulations! You guessed the number {number} correctly!")
#                 break
#             elif guess < number:
#                 print("Number is too low. Try a higher one.")
#             else:
#                 print("Number is too high. Try a lower one.")

#         else:
#             print(
#                 f"Sorry, you've run out of attempts. The correct number was {number}."
#             )

#         play_again_input = input("Do you want to play again? (yes/no): ").lower()
#         play_again = play_again_input == "yes"


# guessing_game()


# Problem Solving Q: Diagonal difference in a matrix
# def diagonal_difference(matrix):
#     n = len(matrix)

#     primary_diagonal_sum = 0
#     for i in range(n):
#         primary_diagonal_sum += matrix[i][i]

#     secondary_diagonal_sum = 0
#     for i in range(n):
#         secondary_diagonal_sum += matrix[i][n - i - 1]

#     absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

#     return absolute_difference
