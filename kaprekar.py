"""
Kaprekar numbers

Consider an n-digit number k. Square it and add the right n digits to the left n or n-1 digits. If the resultant sum is k, then k is called a Kaprekar number. For example, 9 is a Kaprekar number since 92 = 81 and 8 + 1 = 9 and 297 is a Kaprekar number since 2972 = 88209 and 88 + 209 = 297.

Implementation does not rely on converting the int to a string.
"""
import math

def kaprekar(num):
    sq = num * num
    digits = int(math.log10(sq))+1
    n = digits / 2
    if digits % 2 == 1:
        n += 1
    right = sq % (10 ** n)
    left = sq / (10 ** n)
    return (right + left) == num

print '9: {0}'.format(kaprekar(9))
print '81: {0}'.format(kaprekar(81))
print '17: {0}'.format(kaprekar(17))
print '297: {0}'.format(kaprekar(297))
