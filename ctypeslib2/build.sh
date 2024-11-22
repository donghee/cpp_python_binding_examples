cat << EOF > math.cpp
#include "math.h"
#include <string>

int add(int a, int b) {
    return a + b + 100;
}

int multiply(int a, int b) {
    return a * b;
}
EOF

cat << EOF > math.h
#pragma once
#include <string>

extern "C" {
    int add(int a, int b);
    int multiply(int a, int b);
}

EOF

clang++ -std=c++20 -shared -fPIC -o libmath.so math.cpp
clang2py -l ./libmath.so math.cpp > math_.py
python3 app.py
