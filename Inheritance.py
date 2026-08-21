class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f'the name of Employee is : {self.name} and it id is :{self.id}')

class Programmer(Employee):
    def showLanguage(self):
        print("the default language is python")

e1 = Employee("Rohan", 400)
e1.showDetails()
e2 = Programmer("Ramesh", 404)
e2.showDetails()
e2.showLanguage()

         #   ** Access Modifiers  **

# Public
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age        # public variable
        self.name = name      # public variable

obj = Student(10, "vinod")
print(obj.age)
print(obj.name)

# Private
class Student:
    def __init__(self,age,name):
        self.__age = age     # An Indication of private variable
        self.__name = name   # An Indication of private variable

obj = Student(11, 'Ramesh')
# print(obj.__age)  # Cannot be access directly
# print(obj.__name) # Cannot be access directly

print(obj._Student__age)   # can be accessed indirectly
print(obj._Student__name)  # can be accessed indirectly

print(obj.__dir__())

#Protected
class Student:
    def __init__(self):
        self._name = 'billu'

    def _funName(self):     # protected
        return "billubhayanker"

class Subject(Student):   # inheritance
    pass

obj = Student()
obj1 = Subject()

# calling by object of student class
print(obj._name)
print(obj._funName())

# calling by object of student class
print(obj1._name)
print(obj1._funName())
