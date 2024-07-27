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

