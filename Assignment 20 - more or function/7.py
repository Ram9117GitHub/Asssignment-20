""" Write a python program to access a function inside a function. """

def Inside_function(a):
    def add(b):
        nonlocal a
        a+=1
        return a+b
    return add
func = Inside_function(4)
print(func)