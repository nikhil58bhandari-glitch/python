         # * Tuples *

tuple1 = (1,2,3,4,5,6,67)
tuple2 = ("Red","Blue","Green","Yellow")
tuple3 = ("Abhishek",13,"drag",5.3,True)

print(type(tuple1), tuple1)
print(tuple1)
print(tuple2)
print(tuple3)

# check for item-:
country = ("Spain","Itely","India","USA","Germany","England")
if "India" in country:
    print("India is present")
else:
    print("it is not present")


# Range of items
print(country[2:5])  # using positive indexes
print(country[-5:-2])  # using negative indexes

          # ** Manipulating Tuples **
countries = ("Spain","Franc","Portugal", "Germany","England",)
temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)            # remove item
temp[2] = "Italy"      # change item
countries = tuple(temp)
print(countries)

countries2 = ("Vietnam","Chian","Pakistan","India","Russia")
nations = countries + countries2
print(nations)

       # ** Tuple Methods **

tuple3 = (2,3,4,5,3,3,5,4,6,2,4,3)
res = tuple3.count(3)   # return the numbers of times the given element it have limitec built in methods.

# res = tuple3.index(6)   # return the first occurrence of the given element from the tuple.
res = tuple3.index(3,3,5)
print("count of 3 in tuple is-:", res)
