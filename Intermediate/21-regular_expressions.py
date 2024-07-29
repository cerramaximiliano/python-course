### Regular Expressions ###

import re

my_string = "Esta es la lección 21 del curso de Python"
my_other_string = "Esta no es la lección 21"

print(re.match("Esta es la lección", my_string))
print(re.match("Esta es la lección", my_other_string))
