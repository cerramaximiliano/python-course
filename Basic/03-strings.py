
my_string = "Mi string"
my_other_string = 'Mi other string'

print(len(my_string))
print(len(my_other_string))

print(my_other_string + " " + my_string)
print(len(my_string + my_other_string))

my_new_string = "Estes es un String \ncon salto de linea"
print(my_new_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

""" Formateo """
name, surname, age = "Brains", "Moure", 35
print("Mi nombre es {} {}, mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s, mi edad es %s" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad {age} ")

""" Desempaquetado de caracteres """
language = "Python"
a, b, c, d, e, f, = language
print(a)
print(e)

""" Division """
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

""" Reverse """
language_reverse = language[::-1]
print(language_reverse)

""" Funciones del sistema """
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.lower().islower())
print("Py" == "py")