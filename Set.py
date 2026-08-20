info = {"calra", 19, False, 5.8, 19,}
print(info)

dog = set()
print(type(dog))

# Accesing set items:
for item in info:  # using For Loop
    print(item)


#  ** Set Methods **
s1 = {1,2,5,6}
s2 = {3,6,7}
s3 = {1,2,4,3}

        #  union() and update()->
# s3 = (s1.union(s2))
# print(s3)
# s1.update(s2)
# print(s1)

       # Intersection and intersection_update()->
# s4 = s1.intersection(s3)
# print(s4)
# s1.intersection_update(s3)
# print(s1)
#
#     # Symmetric_diffrence() and symmetric_diffrence_update() ->
# s4 = s1.symmetric_difference(s3)
# print(s4)
# s1.symmetric_difference_update(s3)
# print(s1)

    # diffrence() and diffrence_update() ->
s4 = s1.difference(s3)
print(s4)
s1.symmetric_difference_update(s3)
print(s1)

    # isdisjoint() ->
print(s1.isdisjoint(s2))

   # issuperset() ->
print(s1.issuperset(s2))

   # issubset() ->
print(s3.issubset(s1))