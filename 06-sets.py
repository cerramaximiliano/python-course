""" Sets """
""" No tiene indices, no es un estructura ordenada
    no admite repetidos """

my_set = set()
print(my_set, type(my_set))

my_other_set = {}
print(my_other_set, type(my_other_set))
my_other_set = {"Max", "Cerra", 40}
print(my_other_set, type(my_other_set))

name, surname, age = my_other_set
print(name, surname, age)
print(len(my_other_set))

my_other_set.add("Maxi")
print(my_other_set)

languages = {"Kotlin", "Swift", "Python"}
print(languages, type(languages))

my_new_set = languages.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(languages))


