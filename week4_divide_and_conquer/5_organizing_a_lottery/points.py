#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    print(n)
    arr = []
    max_arr = 0
    for i in range(n):
        arr.append([i+1, 'p'])
    print(len(arr))
    for q in queries:
        arr.append([q[0], 'l', q[2]])
        arr.append([q[1], 'r', q[2]])
    print(len(arr))
    arr = sorted(arr, key=lambda x: (x[0], x[1]))
    run_sum = 0
    for i in range(len(arr)):
        if arr[i][1] == 'l':
            run_sum += arr[i][2]
        elif arr[i][1] == 'p':
            max_arr = max(max_arr,run_sum)
        elif arr[i][1] == 'r':
            run_sum -= arr[i][2]
    return max_arr




nm = input().split()

n = int(nm[0])

m = int(nm[1])
queries = []

for i in range(m):
    if i%10000 == 0:
        print(i)
    queries.append(list(map(int, input().split())))

print('reached')
result = arrayManipulation(n, queries)
print(result)