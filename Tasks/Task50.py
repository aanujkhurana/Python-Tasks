from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if it contains no 1's or it contains     //
## no 4's. Use 2 functions only.                                             //
##    1, 2, 3  -> True                                                       //
##    1, 2, 3, 4  -> False                                                   //
##    2, 3, 4  -> True                                                       //
##/////////////////////////////////////////////////////////////////////////////

x = input().split(",")
def onefour(l):
    for i in l:
        if i == 1 or 4:
            return True
        else:
            return False

print(onefour(x))