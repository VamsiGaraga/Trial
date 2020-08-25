# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    while capacity != 0 and len(weights) > 0:
        max_density = values[0]/weights[0]
        max_index = 0
        length = len(weights)
        for i in range(length):
            density = values[i]/weights[i]
            if density > max_density:
                max_index = i
                max_density = density
        if capacity >= weights[max_index]:
            capacity -= weights[max_index]
            value += values[max_index]
            weights.pop(max_index)
            values.pop(max_index)
        else:
            value += capacity * max_density
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
