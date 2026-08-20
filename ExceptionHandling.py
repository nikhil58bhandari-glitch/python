# try:
#      Statements which could generate
#      exception
# except:
#     solution of generated exception

# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
#
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X  {i}  = {int(a) * i}")
#
# except Exception as e:
#     # print(e)
#      print("Invalid Input! ")
#
#
# print("Some imp lines of code")
# print("End of the code")

# try:
#     num = int(input("Enter the number: "))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
#
# except IndexError:
#     print("index error")


       # ** Finally keyword  **

# try:
#     l = [1,2,3,4,56]
#     i = int(input("enter the index-: "))
#     print(l[i])
#
# except:
#     print("some error occured")
#
# finally:
#    print("I am always executed")
#
# def func1():
#     try:
#        l = [1,2,3,4,56]
#        i = int(input("enter the index-: "))
#        print(l[i])
#        return 1
#
#     except:
#       print("some error occured")
#       return 0
#
#     finally:
#      print("I am always executed")
#
# x = func1()
# print(x)
#


    # ** Raising custom errors **

a = int(input("Enter any number between 5 to 9 -:"))

if (a < 5 and  b > 9) :
    raise ValueError("Value should be bettwen 5 and 9")

salary = int(input("enter salary ammont -: "))
if not 2000 < salary < 5000:
    raise ValueError("not a valid salary")


   # ** Define Custom Exceptions **

class CustomError(Exception):
    # code....
    pass

try:
    # code......

except CustomError:
    # code...
