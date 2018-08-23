"""
A Voodoo Prime is a prime number whose reciprocal(in decimal) has the same number in its digits.
For example, 7 is a voodoo prime beacuse its reciprocal 1/7=0.14285714285 contains 7.
"""
from decimal import *

getcontext().prec = 100


def is_prime(x):
    for i in range(2, (x//2+1)):
        if x % i == 0:
            return False
    return True


def voodoo(num):
    result = Decimal(1)/Decimal(num)
    print(result)
    if str(num) in str(result) and is_prime(num):
        return True
    else:
        return False


print(voodoo(1))