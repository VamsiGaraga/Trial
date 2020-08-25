#Uses python3
import sys
import math
import random


def partition3(a,b, l, r):
    x = a[l]
    j = l
    k = l
    for i in range(l+1,r+1):
        if a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
        elif a[i] <= x:
            k += 1
            a[i], a[k] = a[k], a[i]
            a[j], a[k] = a[k], a[j]
            b[i], b[k] = b[k], b[i]
            b[j], b[k] = b[k], b[j]
            j += 1
    return j, k


def randomized_quick_sort(a, b, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    b[l], b[k] = b[k], b[l]
    m, n = partition3(a, b, l, r)
    randomized_quick_sort(a,b, l, m - 1);
    randomized_quick_sort(a,b, n + 1, r);


def distance(x,y,i,j):
    return math.sqrt((x[i] -x[j])**2 + (y[i] - y[j])**2)


def minimum_distance(x, y, low, high):
    if low >= high:
        return 10**18
    if high == low + 1:
        return distance(x, y, low, high)
    mid = (low + high)//2
    d1 = minimum_distance(x, y, low, mid)
    d2 = minimum_distance(x, y, mid+1, high)
    d = min(d1, d2)
    min_index = low
    max_index = high
    for i in range(mid-1, low-1, -1):
        if x[mid] - d > x[i]:
            min_index = i+1
            break
    for i in range(mid, high+1, 1):
        if x[mid] + d < x[i]:
            max_index = i -1
            break
    x_d = x[min_index:max_index + 1]
    y_d = y[min_index:max_index + 1]
    randomized_quick_sort(y_d, x_d, 0, len(x_d) - 1)
    d_n = 10**18
    for i in range(len(x_d)):
        for j in range(i+1,min(i+5,len(x_d))):
            d_n = min(d_n, distance(x_d, y_d, i, j))
    return min(d, d_n)


def minimum_distance_naive(x, y, low, high):
    min_distance = 10**18
    for i in range(low, high+1):
        for j in range(i+1, high+1):
            min_distance = min(min_distance, distance(x, y, i, j))
    return min_distance

# while True:
#     n_points = 100
#     x = []
#     y = []
#     for i in range(n_points):
#         x.append(random.randint(-20,20))
#         y.append(random.randint(-20,20))
#
#     randomized_quick_sort(x, y, 0, len(x) - 1)
#     res1 = minimum_distance_naive(x,y,0,n_points-1)
#     res2 = minimum_distance(x,y,0,n_points-1)
#
#     if res1 == res1:
#         print('OK')
#     else:
#         print(x)
#         print(y)
#         print(res1)
#         print(res2)
#         break


# data = list(map(int, input().split()))
# n = data[0]
# x = data[1::2]
# y = data[2::2]
# randomized_quick_sort(x,y,0,len(x) -1)
# print("{0:.9f}".format(minimum_distance(x, y, 0, len(x) - 1)))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    randomized_quick_sort(x,y,0,len(x) -1)
    print("{0:.9f}".format(minimum_distance(x, y, 0, len(x) -1)))
