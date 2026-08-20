print("Decorators")

def greet(fx):
 def mfx(*args, **kwags):
    print("good Morning")
    fx(*args, **kwags)
    print("thanks for using this function")
 return mfx

# @greet
def hello():
    print("hello world")

@greet
def add(a,b):
    print(a+b)

greet(hello)()
add(7,5)