""" Lists """

my_list = list()
print(my_list)

my_other_list = []
print(my_other_list)
print(len(my_other_list))

my_new_list = [3,5,83,7,3,8]
print(my_new_list)
print(len(my_new_list))
print(type(my_new_list))

print(my_new_list[0])
print(my_new_list[5])
print(my_new_list[-1])
print(my_new_list.count(5))

num1, num2, num3, num4, num5, num6 = my_new_list
print(num1)

num1, num2, num3, num4, num5, num6 = my_new_list[5], my_new_list[4], my_new_list[3], my_new_list[2], my_new_list[1], my_new_list[0]
print(num1)

my_other_new_list = list([20,30,40,50])
print(my_new_list + my_other_new_list)

my_other_new_list.append(60)
print(my_other_new_list)

my_other_new_list.insert(0,10)
print(my_other_new_list)

""" Elimina el elemento que ha encontrado """
my_other_new_list.remove(10)
print(my_other_new_list)

""" Elimina el último elemento de la lista """
print(my_other_new_list.pop())
""" Elimina el elemento del indice """
del my_other_new_list[0]
print(my_other_new_list)

other_list = my_other_new_list.copy()
print(other_list)
other_list.reverse()
print(other_list)

my_other_new_list.clear()
print(my_other_new_list)

my_new_list.sort()
print(my_new_list)