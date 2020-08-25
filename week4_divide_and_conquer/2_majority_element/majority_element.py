# Uses python3
import sys


def count(a, left, right, elm):
    c = 0
    for i in range(left, right):
        if a[i] == elm:
            c += 1
    return c


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left+right)//2
    me1 = get_majority_element(a, left, mid)
    me2 = get_majority_element(a, mid, right)
    if me1 != -1 and me2 != -1:
        if me1 == me2:
            return me1
        else:
            if count(a, left, right, me1) > (mid-left):
                return me1
            elif count(a, left, right, me2) > (mid-left):
                return me2
            else:
                return -1

    elif me1 != -1 and me2 == -1:
        if count(a, left, right, me1) > (mid-left):
            return me1
        else:
            return -1
    elif me1 == -1 and me2 != -1:
        if count(a, left, right, me2) > (mid-left):
            return me2
        else:
            return -1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

#n, *a = list(map(int, input().split()))
#print(get_majority_element(a, 0, n))