""" Functions """

def my_function ():
    print("Estoy es una función")

my_function()

def sum_two_values (num1, num2):
    print(num1 + num2)

sum_two_values(10,20)

def sum_two_values_return (num1, num2):
    return num1 + num2

result = sum_two_values_return(15, 20) + 1
print(result)

def print_name (name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name("Max", "Cerra")
print_name(surname="Cerra", name= "Max")

def print_upper_text (*texts):
    for text in texts:
        print(text.upper())

print_upper_text("Max", "hola", "mundo")
