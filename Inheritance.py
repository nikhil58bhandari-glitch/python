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