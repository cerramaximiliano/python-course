### Higher Order Functions ###

print("**** Higher Order Functions ****")

def sum_one(value):
    return value + 1

def sum_two_values_add(first_value, second_value):
    return  sum_one(first_value + second_value)

result = sum_two_values_add(10,2)
print(result)

def sum_values(num1, num2, f):
    return f(num1 + num2)

results = sum_values(1, 3, sum_one)
print(results)


### CLOSURES ###
print("**** Closures ****")

def sum_ten():
    def add(value):
        return value + 10
    return add

closures = sum_ten()
print(closures(10))

def sum_value(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_value(5)(1)
print(add_closure)

### Built-in Higher Order Functions ###
print("**** Built-in Higher Order Functions ****")

numbers = [1,2,8,14]

# Map
def multiply_two(number):
    return number * 2

result = list(map(multiply_two, numbers))
print(result)

