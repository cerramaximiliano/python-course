""" Classes """

class Person: 
    pass

print(Person)
my_person = Person

class My_Person:
    def __init__(self, name, surname, alias= "No tiene alias"):
        self.__name = name  # Propiedad privada
        self.surname = surname
        self.alias = alias
    def walk (self):
        print(f"{self.__name} está caminando")
        

my_person = My_Person("Maxi", "Cerra")

print(my_person.surname)
my_person.walk()
my_person.full_name = "Maximiliano Cerra"
print(my_person.alias)
print(my_person.full_name)
