# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = l
    for i in range(l+1,r+1):
        if a[i][0] == x[0]:
            k += 1
            a[i], a[k] = a[k], a[i]
        elif a[i][0] <= x[0]:
            k += 1
            a[i], a[k] = a[k], a[i]
            a[j], a[k] = a[k], a[j]
            j += 1
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m, n = partition3(a, l, r)
    if m != n:
        a[m:n+1] = sorted(a[m:n+1])
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, n + 1, r);


def fast_count_segments(starts, ends, points):
    count_dict = {}
    line = []
    for s in starts:
        line.append((s, 'l'))
    for e in ends:
        line.append((e, 'r'))
    for p in points:
        line.append((p, 'p'))
    randomized_quick_sort(line, 0, len(line) -1)
    count = 0
    for i in range(len(line)):
        if line[i][1] == 'l':
            count += 1
        elif line[i][1] == 'r':
            count -= 1
        else:
            count_dict[line[i][0]] = count
    cnt =[]
    for i in range(len(points)):
        cnt.append(count_dict[points[i]])
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


# while True:
#     n_segments = 50
#     n_points = 100
#     starts = []
#     ends = []
#     points = []
#     for i in range(n_segments):
#         a = random.randint(0,10000)
#         b = random.randint(0,10000)
#         starts.append(a)
#         ends.append(a+b)
#
#     for i in range(n_points):
#         points.append(random.randint(0,20000))
#
#     res1 = naive_count_segments(starts,ends,points)
#     res2 = fast_count_segments(starts,ends,points)
#
#     if res1 == res1:
#         print('OK')
#     else:
#         print(starts)
#         print(ends)
#         print(points)
#         print(res1)
#         print(res2)
#         break






# data = list(map(int, input().split()))
# n = data[0]
# m = data[1]
# starts = data[2:2 * n + 2:2]
# ends = data[3:2 * n + 2:2]
# points = data[2 * n + 2:]
# cnt = fast_count_segments(starts, ends, points)
# for x in cnt:
#     print(x, end=' ')


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
