# Cpp Python Binding Examples

- ctypeslib2 for C
- pybind11 for C++
- cppyy for C++

## Install

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install setuptools ctypeslib2 clang==16.0.6 pybind11 cppyy
```

## Build

Example of Python Binding For C using ctypeslib2

```
$ cd ctypeslib2
$ ./build.sh

12
12
103
```

Example of Python Binding For C++ using pybind11

```
$ cd pybind11
$ ./build.sh

running build_ext
x86_64-linux-gnu-g++ -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC -I/home/donghee/tmp/cpp_python_binding_examples/.venv/include -I/usr/include/python3.12 -c flagcheck.cpp -o flagcheck.o -std=c++17
copying build/lib.linux-x86_64-cpython-312/pymodule.cpython-312-x86_64-linux-gnu.so -> 
Hello, World!
12
103
```

Example of Python Binding For C++ using cppyy
```
$ cd cppyy
$ ./build.sh
12
103
```
