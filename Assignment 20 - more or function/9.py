""" Write a python program to create a function to check whether a string is a pangram or not. """
def pangram(s):
    check=""
    small=s.lower()
    combine=small.replace(" ","")
    for i in combine:
        if i in check:
            return False
        else:
            check+=i
    return True
print(pangram("The quick brown fox jumps over the lazy dog"))
