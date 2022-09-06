""" Write a python program to create a function that checks whether a passed string is palindrome or not. """
from hashlib import new


def fun1(s):
    if s ==s[::-1]:
        print("Yes")
    else :
        print("No")

fun1("ramkumar")
fun1("a")