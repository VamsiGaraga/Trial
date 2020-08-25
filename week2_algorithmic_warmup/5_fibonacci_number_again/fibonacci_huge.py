# Uses python3
import sys

def get_fibonacci_huge(n,m):
    if n <= 1:
        return n
    f = [0, 1]
    period = 0
    i = 2
    while(period == 0):
        f.append((f[i - 1] + f[i - 2]) % m)
        if f[i-1] == 0 and f[i] == 1:
            period = i-1
        i += 1
    return get_fibonacci_m(n%period,m)

def get_fibonacci_m(n, m):
    if n <= 1:
        return n
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % m)
    return f[n]


n, m = map(int, input().split())
print(get_fibonacci_huge(n, m))

