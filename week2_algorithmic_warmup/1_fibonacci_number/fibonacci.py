# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    f = [0, 1]
    for i in range(2,n+1):
        next_num = f[i-1]+f[i-2]
        f.append(next_num)
    return f[n]


n = int(input())
print(calc_fib(n))