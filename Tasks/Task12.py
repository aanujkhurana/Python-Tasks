# from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given 2 int lists, print a new list length 4 containing all their         //
## elements.                                                                 //
##    1, 2    3, 4  ->  1, 2, 3, 4                                           //
##    4, 4    2, 2  ->  4, 4, 2, 2                                           //
##    9, 2    3, 4  ->  9, 2, 3, 4                                           //
##/////////////////////////////////////////////////////////////////////////////


def combine(a, b):
    return a + b

a = [1, 2]
b = [3, 4]

print(combine(a, b))