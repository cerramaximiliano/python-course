""" Modules """

import module

module.sum_two_values(10,5)

module.printValue("value")

from module import sum, printValue

sum(15, 20)
printValue(10)


## Modulos incorporados en Python
import math
from math import pi as PI_VALUE
print(math.pi)
print(math.pow(2,8))
print(PI_VALUE)