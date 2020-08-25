# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_1 = 0
    max_2 = 0
    for i in range(n):
        if numbers[i] > max_1:
            max_2 = max_1
            max_1 = numbers[i]
        elif numbers[i] > max_2:
            max_2 = numbers[i]
    return max_1*max_2


input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
