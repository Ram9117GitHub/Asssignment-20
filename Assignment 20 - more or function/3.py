""" Write a python program to create a function that prints the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""
def even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
