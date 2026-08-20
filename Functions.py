# a  = 9
# b = 18
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# c = 8
# d = 17
# gmean2 = (c*d)/(c+d)
# print(gmean2)

# def calculateGmean(a,b):
#     mean = (a *b)/(a+b)
#     print(mean)
#
# calculateGmean(a,b)
# calculateGmean(c,d)
#
# i = 76
# j = 43
# def isGreater(a,b):
#    if( a > b ):
#     print("a is grater than b")
#    else:
#       print("second number is grater or equal")
#
# isGreater(i,j)
# isGreater(c,d)
#
#
# def isLesser(a,b):
#     pass
#

#   * Function Arguments *

#  * Default value -: in this the program execute 8,4 not 1,4 becuse it execute new value
# def average(a = 1,b = 4):
#     print("The average is:", (a+b)/2)
#
# average(8,4)
# average(2)
# # average(b  = 4)
# #
# # average(b= 54, a = 4)   # * Keyword argument
#
# # average(a = 43)  # Required argument
#
# # * Variable length argument
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     #print("average is:", sum / len(numbers))
#     return sum/len(numbers)
#
# c = average(6,8,5,7,8,3,5,6)
# print(c)


# def name(**name):
#     print(type(name))
#     print("Hello," , name["fname"], name["mname"], name["lname"])
# name(mname = "buchanan", lname = "barnes", fname = "james")


  # **  Enumerate Function **

marks = [23,54,76,87,76,54,87,59]

       #  normal code
# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("you did great")
#     index += 1

      # Enumerate Function,

for index, mark in enumerate(marks):
    print (mark)
    if index == 3:
        print ("you did great")
    index += 1

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#  changing the start index

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start = 1):
    print(index,fruit)