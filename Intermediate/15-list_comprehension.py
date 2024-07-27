### List Comprehension ###

my_original_list = [0,1,2,3,4,5,6,7]

my_list = [i for i in range(12)]
print(my_list, type(my_list))

my_range = range(12)
print(my_range, list(my_range))

my_new_range = [i + 1 for i in range(20)]
print(my_new_range)

def sum_five (number):
    return number + 5
my_list = [sum_five(i) for i in range(10)]
print(my_list)