# build the shared library and run the python script
g++ -fPIC -rdynamic -O2 -shared math.cpp -o libmath.so

python app.py
