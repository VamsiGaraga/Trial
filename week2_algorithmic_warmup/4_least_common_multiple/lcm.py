# Uses python3
import sys


def gcd(a, b):
    if b == 0:
        return a
    a_new = a % b
    return gcd(b, a_new)


def lcm(a, b):
    if a > b:
        hcf = gcd(a, b)
    else:
        hcf = gcd(b, a)
    return int(a*b/hcf)


a, b = map(int, input().split())
print(lcm(a, b))

