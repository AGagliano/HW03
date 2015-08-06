#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare

#Returns 1, -1, or 0 depending if x is greater than, less than, or equal to y (respectively)
def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else: 
        return 0

################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.

from math import sqrt

#Returns the length of right triangle hypotenuse given two legs as inputs.
def hypotenuse(a, b):
    c = sqrt(a**2 + b**2)
    return c

################################################################################
# Exercise 3
# When you submit only include your final function: is_between

#Returns TRUE x is less than or equal to y, and y is less than or equal to z.
#Returns FALSE otherwise.
def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else: 
        return False

################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome

#Returns TRUE if a string input is a palindrome, FALSE otherwise.
def is_palindrome(s):
    length = len(s)
    if length == 1 or length == 0:
        return True
    if s[0] == s[length-1]:
        s = s[1:-1]
        is_palindrome(s)
        return True
    else:
        return False 

################################################################################
# Exercise 7
# When you submit only include your final function: is_power

from math import log

#Determines if a is a power of b. 
#Ex: b^x = a, such that x is an integer.
def is_power(a, b):
    #Recursion in the function, if successful, concludes at a = 1. 
    #The same is true for the (-a, -b) case, because the implied odd exponent results in a positive 1.
    if a == 1:                       
        return True
    #Recursive step as long as a is divisible by b.
    elif float(a).is_integer() and abs(a)>1:
        a = float(a)/b
        return is_power(a, b)
    #During the recurrsion process, if a becomes a fraction, then the test fails.
    else:
        return False


################################################################################
def main():
    """Your functions will be called within this function."""
    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")

    ############################################################################
    # Uncomment the below to test and before commiting:

    # Exercise 1
    print compare(1,1)
    print compare(1,2)
    print compare(2,1)
    print '-----------------------------'
    # Exercise 2
    print hypotenuse(1,1)
    print hypotenuse(3,4)
    print hypotenuse(1.2,12)
    print '-----------------------------'
    # Exercise 3
    print is_between(1,2,3)
    print is_between(2,1,3)
    print is_between(3,1,2)
    print is_between(1,1,2)
    print '-----------------------------'
   # Exercise 6
    print is_palindrome("Python")
    print is_palindrome("evitative")
    print is_palindrome("sememes")
    print is_palindrome("oooooooooooo")
    print '-----------------------------'   
    # Exercise 7
    print is_power(28,3)
    print is_power(27,3)
    print is_power(248832,12)
    print is_power(248844,12)
    print '-----------------------------'
    # Additional edge case checking for Exercise 7
    print is_power(-248832, -12)      #True
    print is_power(-2985984, -12)     #False 
    print is_power(-1, 1)             #False
    print is_power(1, -1)             #True
    print is_power(-27, 3)            #False
    print is_power(16, -4)            #True
    print is_power(0, 1)              #False          
    print is_power(1, 5)              #True

if __name__ == "__main__":
    main()