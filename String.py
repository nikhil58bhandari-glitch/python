# from enum import pickle_by_global_name
#
name = "Luffy"
friend = "Zoro"
anotherFriend = 'Sanji'

print("hello ", name)
print("Hello ", friend)
print("hello ", anotherFriend)

apple = 'he said, "I want to an apple" '
print(apple)

mango = '''
he said
you want to eat an mango?
but i refuse
then he offer me an apple
'''   # we can also use """ """" this
print(mango)

print(name[0])
print(friend[3])
# print(friend[4]  # it throws an error becouse index 4 is empty
print(anotherFriend[3])

# # let use a foor loop to count number of string used in apple
#
for character in apple:
    print(character)

    alphabets = "ABCDE"
    for i in alphabets:
        print(i)

    # * SLICING AND OPRATIONS ON STRING *

names = "Naruto,Sasuke,Gara"
print(names[0:6])
print(len(names))

fruit = "mango"
len1 = len(fruit)
print("mango is a", len1, "letter word.")
print(fruit[0: 4]) # including 0 but not 4
print(fruit[1:3])   # including 1 but not 4
print(fruit[:4])
print(fruit[:])

print(fruit[0: -3])  # print(fruit[0:len(fruit): 3])
print(fruit[-1: len(fruit) - 3]) # no answer
print(fruit[-3:-1]) # ng


nm = "harry"
print(nm[-4: -2])

  # * STRING METHODS *

a = "Nikhil"
b = "NIKHIL"
print(len(a))
print(a.upper())     # UPPER()

print(b.lower())     # LOWER()

c = "hey !!!!!"
print(c.rstrip("!"))  # RSTRIP() -> remove any trailing characters.

print(a.replace("Ni", "A"))  # REPLACE(): it replace all occurences of a string with another string.
print(b.replace("NIKHIL", "akhil"))

e = "hey bro how you doing"
print(e.split(" "))  # SPLIT(): split the string at the whitespace

str1 = "hello"   # Capitalize(): turn first letter to capital
capStr1 = str1.capitalize()
print(capStr1)

str2 = "hello World"
print(str2.capitalize())

str1 = "Welcome to the Club banana leclerc  !!!"
print(len(str1))
print(str1.center(50))    # CENTETR(): aligns the string to the center as per the parameter given by hte user.

print(str1.count("a"))     # COUNT(): return the numberof times the given value has occurred whitin the given stings.

print(str1.endswith("!!!"))    # ENDSWITH(): check if the stirng ends with given value, if yes than return true. else return false.
print(str1.endswith("to", 4, 10))

print(str1.find("banana"))     # FIND()

print(str1.index("to"))     # index()

str1 = "Welcometotheconsole"
str2 = "Welcometotheconsole09864"

print(str1.isalnum())    # ISALNUM(): it return true only if the entire string only consits of A-Z, a-z, 0-9. if any characters Or punctuations are present, then it returns False.
print(str2.isalnum())

print(str1.isalpha())    # ISALPHA(): it return true only if the entire string only consits of A-Z, a-z. if any characters Or punctuations or numbres(0-9) are present, then it returns False.
print(str2.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "               #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

