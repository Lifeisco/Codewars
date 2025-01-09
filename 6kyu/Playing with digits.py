'''
Examples:

n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''

def dig_pow(n, p):
    result = 0
    for i in str(n):
        result += int(i) ** p
        p += 1
    if result % n:
        return -1
    else:
        return result // n

print(dig_pow(46288,3))
