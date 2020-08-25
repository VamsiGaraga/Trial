# Uses python3
import sys


def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave, right)
    a_new = a[left:ave]
    b_new = a[ave:right]
    i = 0
    while len(a_new) != 0 and len(b_new) != 0:
        if a_new[0] <= b_new[0]:
            a[left + i] = a_new.pop(0)
        elif b_new[0] < a_new[0]:
            a[left+i] = b_new.pop(0)
            number_of_inversions += len(a_new)
        i += 1
    if len(a_new) != 0:
        a[left+i:right] = a_new
    elif len(b_new) != 0:
        a[left+i:right] = b_new
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a)))

#
# n, *a = list(map(int, input().split()))
# print(get_number_of_inversions(a, 0, len(a)))
# print(*a)
