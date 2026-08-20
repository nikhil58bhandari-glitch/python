 #    *  For Loops  *
# print(1)
# print(2)
# print(3)

# name = "Abhishek"
# for i in name:
#     print(i, end=", ")
#     if(i == "b"):
#         print("this is something special!")
#
#
# colors = ["red","green","blue", "yellow", "pink"]
# for x in colors:
#     print(x)
#     for i in x:
#         print(i)


# for k in range(5):
#     print(k + 1)
#
# for k in range(2, 10):
#     print(k)

# for  k in range(1, 20, 3):
#     print(k)


     # ** For Loop with else in Python **

# for counter in sequence:
#      # statement inside for loop block
# else:
#     # statement inside else block

# for i in range(5):
#     print(i)
#
# else:
#     print("sorry no i")
#
# for i in range(6):
#     print(i)
#     if i == 5:
#         break
#
# else:
#     print("sorry no i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))

else:
    print("else block in loop")
print("out of loop")