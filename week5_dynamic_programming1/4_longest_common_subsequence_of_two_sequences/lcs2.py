#Uses python3

import sys

def lcs2(a,b):
    lcs2_dict = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    def lcs(a, b, i, j):
        if a[i-1] == b[j-1]:
            return lcs2_dict[i-1][j-1] + 1
        else:
            return max(lcs2_dict[i-1][j], lcs2_dict[i][j-1])

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            lcs2_dict[i][j] = lcs(a,b,i,j)
    return lcs2_dict[i][j]

# data = list(map(int, input().split()))
#
# n = data[0]
# data = data[1:]
# a = data[:n]
#
# data = data[n:]
# m = data[0]
# data = data[1:]
# b = data[:m]
#
# print(lcs2(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
