import ctypeslib
from ctypeslib.codegen import clangparser
import pathlib
import math_

py_module = ctypeslib.translate('''int i = 12;''')
print(py_module.i)  # 12

print(math_.multiply(3, 4))
print(math_.add(1, 2))

