""" Dictionaries """

my_dict = dict()

print(my_dict, type(my_dict))

my_other_dic = {"name": "Max", "surname": "Cerra", "languages": {"Python", "Swift", "Kotlin"}}
print(my_other_dic, type(my_other_dic))
print(my_other_dic["name"])
my_other_dic["address"] = "Maure 2362"
print(my_other_dic)
del my_other_dic["address"]
print(my_other_dic)

print(my_other_dic.items())
print(my_other_dic.keys())
print(my_other_dic.values())
