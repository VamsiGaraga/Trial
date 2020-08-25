# Uses python3
import sys

f = [0, 1]
for i in range(2, 61):
    next_num = (f[i - 1] + f[i - 2]) % 10
    f.append(next_num)


def fibonacci_partial_sum(from_, to):
    m = from_ % 60
    n = to % 60
    if n >= m:
        return sum(f[m:n+1])%10
    else:
        return (sum(f[m:]) + sum(f[:n+1]))%10


from_, to = map(int, input().split())
print(fibonacci_partial_sum(from_, to))