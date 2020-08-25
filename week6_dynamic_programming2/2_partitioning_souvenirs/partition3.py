# Uses python3
import sys
import itertools

partition_dict = {}
def partition(W, A, j):
    W = sorted(W)
    key = str(W[0]) + str(W[1]) + str(W[2]) + str(j)
    if key in partition_dict:
        return partition_dict[key]
    elif W[0] == W[1] == W[2] == 0:
        partition_dict[key] = 1
        return 1
    elif j == 0:
        partition_dict[key] = 0
        return 0
    elif A[j-1] <= W[0]:
        partition_dict[key] = max(partition([W[0] - A[j-1]] + W[1:], A, j-1), partition([W[0], W[1] - A[j-1], W[2]], A, j-1), partition([W[0], W[1], W[2]-A[j-1]], A, j-1))
        return partition_dict[key]
    elif A[j-1] <= W[1]:
        partition_dict[key] = max(partition([W[0], W[1] - A[j-1], W[2]], A, j - 1), partition([W[0], W[1], W[2]-A[j-1]], A, j-1))
        return partition_dict[key]
    elif A[j-1] <= W[2]:
        partition_dict[key] = partition([W[0],W[1],W[2]-A[j-1]],A, j-1)
        return partition_dict[key]
    else:
        partition_dict[key] = 0
        return 0


def partition3(A):
    sum_a = sum(A)
    if sum_a % 3 != 0:
        return 0
    else:
        sum_per = sum_a//3
        W = [sum_per]*3
        return partition(W, A, len(A))


# n, *A = list(map(int, input().split()))
# print(partition3(A))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

