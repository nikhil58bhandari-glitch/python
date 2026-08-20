# a = input()
# print(a)

a = input("my name is :")
print("my name is:",a)

x = input("Enter first number: ")
y = input("Enter second number: ")

print(x + y) # this will not add X and Y because pyhton assuming them as a string not number our output will become firstnum second num

print(int(x) + int(y)) # this will add X and Y
print(float(x)+ float(y))
