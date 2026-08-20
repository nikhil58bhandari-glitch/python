# dic = {
#     'name' : 'nikhil',
#        'age': 22,
#     'eligible' : True
# }
# print(dic)
#
# info = {
#     334 : 'neha',
#     42 : 'nikhil',
#     543 : 'amit',
#     987 : 'akash'
# }
# print(info[334])
# print(info.get(334))  # accesing single dictionary item
#
# print(info.values())   # accesing multiple values
#
# for key in info.keys():  # we can use this as well to ittret all values
#     print(info[key])
#
# for key in info.keys():
#     print(f"the value corresponding to the key {key} is {info[key]}")
#
# print(info.items())  # accesing key-value pairs:
#
# for key, value in info.items():
#     print(f"The value corresponding to the key {key} is {value}")


      # ** Dictionary Methods **

info = {'name' : 'Luffy', 'age' : 19, 'proffesion' : 'pairet' }
print(info)

      # update() -:
info.update({'age' : 22})
info.update({'first mate' : 'Zoro'})
print(info)

    # clear()
# info.clear()
# print(info)

     # pop()
# info.pop('age')
# print(info)

     #  del()
# del info['age']
# print(info)

del info
print(info)

