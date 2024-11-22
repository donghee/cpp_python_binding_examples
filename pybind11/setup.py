import os
import sys
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages

ext_modules = [
    Pybind11Extension(
        "pymodule",
        ["text.cpp", "math.cpp", "bindings.cpp"],
    ),
]

setup(
    name="pymodule",
    version="0.0.1",
    author="Donghee Park",
    description="Pybind11 example",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
