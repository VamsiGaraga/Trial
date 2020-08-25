# Uses python3
import sys


def get_change(m):
    min_change = m//10
    m = m % 10
    min_change += m//5
    m = m % 5
    min_change += m
    return min_change


m = int(input())
print(get_change(m))
