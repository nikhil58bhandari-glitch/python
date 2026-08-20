def hello():
    print("you buddy")

hello()

# railwayFrom  --> class(bluprint)
# harry ->> harry ki info wala form = object[enttity]
# tom ---> tom ki info wala from \



      # **  Class nd Object

# class person:
#     name = "harry"
#     occupation = "Softwear Devloper"
#     networth = 10000
#     def info(self):      # the self  perameter is a reference to the cuttent indtance of thr class, ans is udef to accrss variablesf that belongs to the class.
#                          # It must be provided as the extra parameter inside the method definition.
#         print(f"{self.name} is a {self.occupation}")
#
# a = person()
# a.name = "nikhil"
# a.occupation = "CA"
# # print(f"name = {a.name}, occupation = {a.occupation}, networth = {a.networth}")
# a.info()
#
# b = person()
# b.name = "Luffy"
# b.occupation = "king of pirates"
# b.info()

     # ** Constructors **

class person:
    # name = "nikhil"
    # occ = "Devloper"
    def __init__(self,n,o):    # Parameterized Constructor
        print("hey i am a person")
        self.name = n
        self.occ = o

    def info(self):         # Default Constructor
     print(f"{self.name} is a {self.occ}")


a = person("naruto", "hokage")
b = person("hinata", "naturo wife")
a.info()
b.info()

# print(a.name)
# a.name = "Zoro"
# a.occ = "Bounty Hunter"
# a.info()

