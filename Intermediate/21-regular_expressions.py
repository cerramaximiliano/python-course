### Regular Expressions ###

import re

my_string = "Esta es la lección 21 del curso de Python"
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
