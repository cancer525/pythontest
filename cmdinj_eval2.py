#!/usr/bin/env python
hidden_value = "Secret:leyond.info"
def dangerous_function(filename):
    print open(filename).read()
    user_func = raw_input("type a function: y = ")
    for x in range(1,10):
        print "x = ", x , ", y = ", eval(user_func)

dangerous_function()
