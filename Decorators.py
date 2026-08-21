# print("Decorators")
#
# def greet(fx):
#  def mfx(*args, **kwags):
#     print("good Morning")
#     fx(*args, **kwags)
#     print("thanks for using this function")
#  return mfx
#
# # @greet
# def hello():
#     print("hello world")
#
# @greet
# def add(a,b):
#     print(a+b)
#
# greet(hello)()
# add(7,5)


   # ** Getters and Setters **

class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property     # getter
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter    # setter 
    def ten_value(self, new_value):
        self._value = new_value/10

obj = Myclass(10)
obj.ten_value = 69
print(obj.ten_value)
obj.show()