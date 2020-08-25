#Uses python3

import sys

def is_greater_or_equal(digit,max_digit):
    if len(digit) == len(max_digit):
        return int(digit) >= int(max_digit)
    elif len(digit) > len(max_digit):
        i = 0
        while i < len(max_digit):
            if digit[i] != max_digit[i]:
                return int(digit[i]) >= int(max_digit[i])
            i = i+1
        return is_greater_or_equal(digit[i:], max_digit)
    else:
        i = 0
        while i < len(digit):
            if digit[i] != max_digit[i]:
                return int(digit[i]) >= int(max_digit[i])
            i = i + 1
        return is_greater_or_equal(digit, max_digit[i:])

def largest_number(a):
    res = ""
    while len(a) != 0:
        max_index = 0
        for i in range(len(a)):
            if is_greater_or_equal(a[i], a[max_index]):
                max_index = i
        res = res + a[max_index]
        a.pop(max_index)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))