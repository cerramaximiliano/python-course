### Regular Expressions ###

import re

my_string = "Esta es la lección 21 del curso de Python: Expresiones Regulares"
my_other_string = "Esta no es la lección 21: lección 1"

match = re.match("Esta es la lección", my_string, re.I)
print(re.match("Esta es la lección", my_other_string))



if match != None:
    print(match)
    span = match.span()
    print(match.span())
    start, end = span
    print(my_string[start:end])


search = re.search("Esta es la lección", my_string, re.I)
print(search)

email = "cerramaximiliano@gmail.com"

findall = re.findall("lección", my_string, re.I)
print(findall)

split = re.split(":", my_other_string)
print(split)

substitution = re.sub("Esta", "esta", my_string)
print(substitution)

# Patterns
pattern = r'[lL]ección'
print(re.findall(pattern, my_string))
pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))
pattern = r'[0-9]'
print(re.findall(pattern, my_string))
pattern = r'\d'
print(re.findall(pattern, my_string))
pattern = r'\D'
print(re.findall(pattern, my_string))
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
email = "cerramaximiliano@gmail.com"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))