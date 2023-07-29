
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
