 # * this is string formating *
# letter = "Hey my name is {} and i am form {}"
# country = "India"
# name = "nikhil"
#
# print(letter.format(name, country))
#
# letter = "Hey my name is {1} and i am form {0}"
# country = "India"
# name = "nikhil"
#
# print(letter.format( country, name ))
#
# print(f"hey my name is {{name}} and i am from {country}")
#
# txt = "for only {price:.2f} dollers!"
# print(txt.format(price = 49.09999))
#
# price = 49.09999
# txt = f"for only {price:.2f} dollers!"
# print(txt)
#
# print(f"{23  * 3}")
# print(type(f"{22* 32}"))
#

    # **  Docstrings in Python  **
  # -> Python docstings are the sting literals that
  # -> appear right the definition of a function, method, class, or module.

def square(n):
    ''' Takes in a number n, returns the square of n '''
    print(n ** 2)
square(5)   # '''Takes in a number n, returns the square of n''' is a docstring which will not appear in output.

print(square.__doc__)