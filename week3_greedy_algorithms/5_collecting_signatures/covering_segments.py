# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    while len(segments) != 0:
        length = len(segments)
        min_b_i = 0
        for i in range(length):
            if segments[i][1] < segments[min_b_i][1]:
                min_b_i = i
        point = segments[min_b_i][1]
        points.append(point)
        for i in range(length-1, -1, -1):
            if segments[i][0] <= point:
                segments.pop(i)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
#n, *data = map(int, input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
