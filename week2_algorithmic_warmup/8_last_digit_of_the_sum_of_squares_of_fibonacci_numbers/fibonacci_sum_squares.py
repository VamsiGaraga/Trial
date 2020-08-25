# Uses python3
from sys import stdin

f = [0, 1]
for i in range(2, 61):
    next_num = (f[i - 1] + f[i - 2]) % 10
    f.append(next_num)


def fibonacci_sum_squares(n):
    m = n % 60
    return (f[m]*f[m+1])%10


n = int(input())
print(fibonacci_sum_squares(n))
