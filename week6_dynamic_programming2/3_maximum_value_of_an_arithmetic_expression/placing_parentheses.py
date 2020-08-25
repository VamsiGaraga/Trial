# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    n_op = len(dataset)//2
    min_dict = [[0 for i in range(n_op + 1)] for j in range(n_op + 1)]
    max_dict = [[0 for i in range(n_op + 1)] for j in range(n_op + 1)]

    def MaxMin(dataset, i, j):
        min_d = 10**18
        max_d = -10**18
        for k in range(i, j):
            a = evalt(min_dict[i-1][k-1], min_dict[k][j-1], dataset[k*2 - 1])
            b = evalt(min_dict[i-1][k-1], max_dict[k][j-1], dataset[k*2 - 1])
            c = evalt(max_dict[i-1][k-1], min_dict[k][j-1], dataset[k*2 - 1])
            d = evalt(max_dict[i-1][k-1], max_dict[k][j-1], dataset[k*2 - 1])
            min_d = min(min_d, a, b, c, d)
            max_d = max(max_d, a, b, c, d)
        return min_d, max_d

    for i in range(n_op+1):
        min_dict[i][i] = int(dataset[2*i])
        max_dict[i][i] = int(dataset[2*i])
    for s in range(1, n_op+1):
        for j in range(0, n_op - s + 1):
            min_dict[j][j+s], max_dict[j][j+s] = MaxMin(dataset, j+1, j+s+1)
    return max_dict[0][n_op]



if __name__ == "__main__":
    print(get_maximum_value(input()))

