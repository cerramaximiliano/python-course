

print("Python")

import numpy
print(numpy.version.version)
numpy_array = numpy.array([1,2,3,5,7,2,4,8])
print(type(numpy_array))
print(numpy_array * 2)

import pandas
print(pandas)

import requests
print(requests)
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

from mypackage import arithmetics
print(arithmetics.sum_two_values(1, 4))
