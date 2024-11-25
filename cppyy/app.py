import cppyy

#cppyy.include("math.cpp") # easy way to use cpp code

cppyy.include('math.h')
cppyy.load_library('libmath.so')
Math = cppyy.gbl.Math

math_ = Math()
print(math_.multiply(3, 4))
print(math_.add(1, 2))


