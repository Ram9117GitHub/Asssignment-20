""" Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not."""
def prime(num):
    if num % 2 != 0:
        print("prime number")
    else:
        print("Not")
prime(3) # prime number
prime(4) # not prime number