colors = ["voilet","indigo","blue","green"]
colors.sort()  # list.sort()-: this  sorts the list in accending order.
print(colors)

num = [9,8,6,6,5,2,3,5,6,2,2,1,1,2,3,3,5,6]
num.sort(reverse = True)   # reverse = ture -: this sorts the list in decending order
print(num)

l = [1,22,3,4,3,2,2]
# l.append("23")    # list.append() -: add somthing in end
# l.reverse()         # list.reverse() -: reverse the order of the list.
# print(l)

print(l.index(4))  # list.index() -: it returns the index of the first occurrence of the list item.
print(l.count(2))   # list.count() -: it return the count of the number of items with the given value.

m = l.copy()   # list.copy() -: it return copy if the list.
               # this can be done to perform operations on the list without modifying the original list
print(l)
print(m)

l.insert(3, 76)  # list.insert() -: insert an item at given index.
print(l)

m = [54,54,23,8,7,544,35,4]
l.extend(m)   # extend() -: it add an entire list or any other coolection database to the existing list.
print(l)

k = l + m
print(k)






