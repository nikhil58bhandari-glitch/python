# -> Recusion -: in Pyhton, we know that  a function can call other function.
# -> it is even possible for the function to call itself.
# -> these types of construct are termed as recursive function.

  # factorial(n) = n * factorial(n-1)
def factorial(num):
    if num == 0 or num == 1 :
        return 1
    else:
        return (num * factorial(num - 1))

      # 5 * factrial(4)
      # 5 * 4 * factorial(3)
      # 5 * 4 * 3 * factorail(2)
      # 5 * 4 * 3 * 2 * factorial(1)
      # 5 * 4 * 3 * 2 * 1

#  Drive Code
num = 7
for i in range(num):
    print(factorial(i), end=" ")
print("Number: ", num)
print("Factorial: ", factorial(num))

def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return  fibonacci(n - 1) + fibonacci (n - 2)

n = 10
for i in range(n):
    print(fibonacci(i), end=" ")



