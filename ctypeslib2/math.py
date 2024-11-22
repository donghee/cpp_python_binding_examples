# -*- coding: utf-8 -*-
#
# TARGET arch is: []
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


_libraries = {}
_libraries['libmath.so'] = ctypes.CDLL('./libmath.so')


add = _libraries['libmath.so'].add
add.restype = ctypes.c_int32
add.argtypes = [ctypes.c_int32, ctypes.c_int32]
multiply = _libraries['libmath.so'].multiply
multiply.restype = ctypes.c_int32
multiply.argtypes = [ctypes.c_int32, ctypes.c_int32]
__all__ = \
    ['add', 'multiply']
