""" Exceptions Handling """


numberOne = 5
numberTwo = 1
numberTwo = "1"

print("***** PRIMER EJEMPLO *****")
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

print("***** SEGUNDO EJEMPLO *****")
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: 
    ## Se ejecuta si no se produce un error
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")

print("***** TERCER EJEMPLO *****")
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError: ## Controla solo errores de tipo
    print("Se ha producido un TypeError")
except ValueError: ## Controla solo errores de valor
    print("Se ha producido un ValueError")

print("***** CUARTO EJEMPLO *****")
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as error: ## Controla solo errores de tipo
    print(f"Se ha producido un TypeError {error}")
except ValueError: ## Controla solo errores de valor
    print("Se ha producido un ValueError")