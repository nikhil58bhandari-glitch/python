#   * Conditinal Opreaters *
 #  (>, <, ==, <=, >=, !=)

#   * IF-ELSE *

# a = int(input("Enter you age is: "))
# print("your age is: ", a)
#
# if(a > 18):
#     print("you are eligibale for vote")
# else:
#     print("you are not eligibale for vote")
#
# applePrice = 10
# budget = 200
#
# if (budget - applePrice > 50):
#     print("Alexa, add 1 kg Apples to the cart.")

# else:
#     print("Alexa, do not add Apples to the cart.")


#   * ELIF *

# num = int(input("Enter the value of num: "))
# if (num < 0):
#   print("Number is negative.")
#
# elif (num == 0):
#   print("Number is Zero.")
#
# elif (num == 999):
#   print("Number is Special.")
#
# else:
#   print("Number is positive.")
#
# print("I am happy now")


#   * NESTED *

# num = 18
# if (num < 0):
#     print("Number is negative.")
#
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#
#     else:
#         print("Number is greater than 20")
#
# else:
#     print("Number is zero")
#

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
#
# timestamp = int(time.strftime('%H'))
#
# if( timestamp < 12 ):
#     print("Good Morning")
#
# elif(timestamp < 18):
#     print("good afternoon")
#
# elif(timestamp < 21):
#     print("good evening")
#
# else:
#     print("good night")
#


   # ** Short hand if else statement

a = 100
b = 200

print("a") if a > b else print("=") if a==b else print("b")

 # short hand if nd else
result = value_if_true if condition else vale_if_true

 # normal if else statement
if condition:
   result =  value_if_true
else:
   result = value_if_false
