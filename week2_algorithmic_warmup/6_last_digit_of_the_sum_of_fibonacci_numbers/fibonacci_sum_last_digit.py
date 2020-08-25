# Uses python3
import sys


def fibonacci_sum(n):
    if n <= 1:
        return n
    s = [0, 1, 2]
    for i in range(3, n+1):
        s.append((2*s[i-1] - s[i-3]) % 10)
    return s[n]


n = int(input())
print(fibonacci_sum(n % 60))
