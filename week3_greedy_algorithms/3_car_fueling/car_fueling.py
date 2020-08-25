# python3
import sys


def compute_min_refills(distance, tank, stops):
    n = len(stops)
    stops.append(distance)
    num_refills = 0
    current_refill = -1
    last_refill = 0
    while last_refill + tank < distance:
        while current_refill < n and stops[current_refill + 1] - last_refill <= tank:
            current_refill += 1
        if stops[current_refill] == last_refill:
            return -1
        num_refills += 1
        last_refill = stops[current_refill]
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
#d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
