""" Conditionals """

my_condition = True

if my_condition:
    print("Se ejecuta la condición")

print("La ejecución continúa")

my_condition = False

if my_condition:
    print("Se ejecuta la condición")

print("La ejecución continúa")


my_second_condition = 10

if my_second_condition > 50:
    print("Se cumple la condición 10 > 50")
elif my_second_condition == 10:
    print("Se cumple 10 es igual a 10")
else:
    print("No se cumple la condición 10 > 50")

my_third_condition = 0

if not my_third_condition:
    print("Condición que no se cumple")