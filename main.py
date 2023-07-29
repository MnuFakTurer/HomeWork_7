
# task 1

# def degree_number(number, degree):
#     if degree <= 1:
#         return number
#
#     return number * degree_number(number, degree - 1)
#
# try:
#
#     integer = float(input("Enter number: "))
#     extent = int(input("Enter degree: "))
#
#     result = degree_number(integer, extent)
#     print(f"{integer} ^ {extent} = {result}")
#
# except Exception as e:
#     print(e)

# degree_number(2, 2) -> 2 * degree_number(2, 1) => 4
# degree_number(2, 1) -> 2

# task 2

# def stars(symbols):
#     if symbols > 0:
#         print("*",end="")
#         stars(symbols -1)
#
# try:
#
#     numbers_stars = int(input("Enter numbers of stars: "))
#     stars(numbers_stars)
#
# except Exception as e:
#     print(e)

# stars(3) -> 3 > 0 -> "*" -> stars(symbols -1)
# stars(2) -> 2 > 0 -> "*" -> stars(symbols -1)
# stars(1) -> 1 > 0 -> "*" -> stars(symbols -1)
# stars(0) -> 0 > 0 -> stars(symbols -1)
# stars(1) -> stars(symbols -1)
# stars(2) -> stars(symbols -1)
# stars(3) -> stars(symbols -1) -> ***

# task 3

# def sum(list, num_one, num_two):
#     if num_one >= len(list):
#         return 0
#     else:
#         return list[num_one] + sum(list, num_one + 1, num_two)
#
# import random
#
# random_list = []
#
# for i in range(9):
#     random_list.append(random.randint(1, 100))
#
# sum_num_one = 1
# sum_num_two = 8
#
# result = sum(random_list, sum_num_one, sum_num_two)
# print(random_list)
# print(f"Sum of numbers from {sum_num_one} before {sum_num_two} = {result}")

# numbers = [1, 2, 3, 4, 5], num1 = 1, num2 = 3:
# sum(numbers, num1, num2) -> 1 >= numbers -> sum([], 1, 3)
# numbers[1] + sum(numbers, num1, num2) -> 1 >= numbers -> sum([], 2, 3)
# 2 + numbers[2] + sum(numbers, num1, num2) -> 1 >= numbers -> sum([], 3, 3)
# 2 + 3 + numbers[3] + sum(numbers, num1, num2) -> 1 >= numbers -> sum([], 4, 3) -> 9

