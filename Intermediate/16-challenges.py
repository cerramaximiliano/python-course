### Challenges ####

""" 
FIZZ BUZZ
    Escribe un código que imprima por consola los números
    del 1 al 100 (ambos incluidos y con un salto de línea
    entre cada impresión), sustituyendo los siguientes:
        Múltiplos de 3 por la palabra "fizz",
        Múltiplos de 5 por la palabra "buzz",
        
 """
print("*** Fizz Buzz ***")
def fizz_buzz ():
    numbers = range(1, 101)
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz()


""" 
ANAGRAMA
    Escribe una funcion que reciba dos parámetros (String) y 
    retorne verdadero o falso según sean o no anagramas.
 """
print("*** Anagrama ***")
def is_anagram(str1, str2):
    if str1.lower() == str2.lower():
        return False
    return sorted(str1.lower()) == sorted(str2.lower())

print(is_anagram("amor", "roma"))


""" 
FIBONACCI 
"""
print("*** Fibonacci ***")
def fibonacci():
    prev = 0
    next = 1
    index = 0
    while index < 50:
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        index = index + 1

## fibonacci()


""" Escribe un código que se encargue de comprobar si
un número es primo o no
Que imprima los números primos entre 1 y 100
 """
print("*** Es primo? ***")
def is_prime():
    for number in range(1,101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
            if not is_divisible:
                print(number)

is_prime()

""" 
INVIRTIENDO CADENAS
Crea una función que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan del forma automática
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 """
print("*** REVERSE ***")
def reverse(string):
    index = -1
    result = ""
    for i in string:
        result += string[index]
        index = index - 1
    return result

result = reverse("hola")
print(result)