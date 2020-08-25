#Uses python3

import sys


def lcs3(a, b, c):
    lcs3_dict = [[[0 for i in range(len(c) + 1)] for j in range(len(b) + 1)] for k in range(len(a) + 1)]

    def lcs(a, b, c, i, j, k):
        if a[i-1] == b[j-1] == c[k-1]:
            return lcs3_dict[i-1][j-1][k-1] + 1
        else:
            return max(lcs3_dict[i-1][j][k], lcs3_dict[i][j-1][k], lcs3_dict[i][j][k-1])

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                lcs3_dict[i][j][k] = lcs(a, b, c, i, j, k)
    return lcs3_dict[len(a)][len(b)][len(c)]


# data = list(map(int, input().split()))
# an = data[0]
# data = data[1:]
# a = data[:an]
# data = data[an:]
# bn = data[0]
# data = data[1:]
# b = data[:bn]
# data = data[bn:]
# cn = data[0]
# data = data[1:]
# c = data[:cn]
# print(lcs3(a, b, c))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
