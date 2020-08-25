def twoStacks(x, a, b):
    if x<a[0] and x<b[0]:
        return 0
    a_sum = [0]
    b_sum = [0]
    sum = 0
    for i in range(len(a)):
        sum+=a[i]
        a_sum.append(sum)
    sum = 0
    for i in range(len(b)):
        sum += b[i]
        b_sum.append(sum)
    max_rem = 1
    n=0
    while(max_rem>0):
        n += 1
        max_rem = float('-inf')
        start = max(0, n-len(b))
        stop = min(n+1, len(a)+1)
        if start <= stop:
            for i in range(start, stop):
                rem = x-a_sum[i]-b_sum[n-i]
                max_rem = max(max_rem, rem)
    return n-1


x = 10

a = [5, 1, 1, 1, 1, 1]

b = [4, 4, 2, 1, 1, 1]

print(twoStacks(x, a, b))