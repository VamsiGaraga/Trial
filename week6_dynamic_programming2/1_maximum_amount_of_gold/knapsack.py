# Uses python3
import sys


def optimal_weight(W, w):
    weight_dict = [[0 for i in range(len(w) + 1)] for j in range(W+1)]

    def opt_weight(i, w, j):
        if i == 0:
            return 0
        elif j == 0:
            return 0
        elif i >= w[j-1]:
            return max(weight_dict[i][j-1], weight_dict[i-w[j-1]][j-1] + w[j-1])
        else:
            return weight_dict[i][j-1]

    for i in range(W + 1):
        for j in range(len(w) + 1):
            weight_dict[i][j] = opt_weight(i, w, j)

    return weight_dict[W][len(w)]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


W, n, *w = list(map(int, input().split()))
print(optimal_weight(W, w))
