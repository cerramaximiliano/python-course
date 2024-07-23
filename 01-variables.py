my_variable = 10

my_str_variable = "Hola mundo"

my_num_variable = str(my_variable)


print(my_variable, type(my_variable))

print(my_str_variable)

print(my_num_variable, type(my_num_variable), len(my_num_variable))

my_text = "Este es un texto"
print(my_text)
my_text = 20
print(my_text)

my_number = 40
print(my_number, type(my_number))
my_number = 40.0
print(my_number, type(my_number))

my_number = input("Cual es el número?")

print(my_number)

""" Forzamos el tipo, pero no es tipado """
address: str = "Mi direccion"
address = 32
print(type(address))
