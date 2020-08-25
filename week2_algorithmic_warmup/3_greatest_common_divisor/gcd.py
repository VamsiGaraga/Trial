# Uses python3
import sys


def gcd(a, b):
    if b == 0:
        return a
    a_new = a % b
    return gcd(b, a_new)


a, b = map(int, input().split())
if a > b:
    print(gcd(a, b))
else:
    print(gcd(b, a))
