# Uses python3
import sys


def get_change(m):
    t = [1000000]*(m+1)
    t[0] = 0
    coins = [1, 3, 4]
    for i in range(1,m+1):
        for coin in coins:
            if coin <= i:
                t[i] = min(t[i], t[i - coin] + 1)
    return t[m]

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))


m = int(input())
print(get_change(m))
