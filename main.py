
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