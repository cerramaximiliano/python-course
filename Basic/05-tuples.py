

my_tuple = tuple()
print(my_tuple)
print(type(my_tuple))

my_new_tuple = (32, 15)
print(my_new_tuple)
print(type(my_new_tuple))

my_other_new_tuple = (35, 1.80, "Max", "Cerra", "Cerra")
print(my_other_new_tuple)
print(my_other_new_tuple[0])
print(my_other_new_tuple[-1])

print(my_other_new_tuple.count("35"))
print(my_other_new_tuple.count(35))
print(my_other_new_tuple.count(1.80))
print(my_other_new_tuple.count("Max"))
print(my_other_new_tuple.count("Cerra"))

print(my_other_new_tuple.index("Max"))
""" 
    print(my_other_new_tuple.index("Maximiliano")) 
"""
""" 
    Una tupla es inmutable
    my_other_new_tuple[2] = 2.1
    my_other_new_tuple[1] = 1.5
"""

print(my_other_new_tuple + my_new_tuple)
print(my_other_new_tuple[3:5])

""" Transformo una tupla en una lista """
my_other_new_tuple = list(my_other_new_tuple) 
print(my_other_new_tuple, type(my_other_new_tuple))