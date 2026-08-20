a = "1"
b = "3"

# a = 1
# b = 3

print(int(a) + int(b))

#  Explicit TypeCasting:-
string = "15"
number = 7

string_number = int(string) # throws an error if the string is not valid integer

sum = number + string_number
print("the sum of both the number is:", sum)

#   Implicit TypeCasting:-
# python automatically convert
c = 1.9
d = 8
print(c + d)

e = 7   # a is int
print(type(a))

f = 3.0 #python automatically convert f to float
print(type(f))

# python automatically convert g to float as it is a float addition
g = e + f
print(g)
print(type(g))


