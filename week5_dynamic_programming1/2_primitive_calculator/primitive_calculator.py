# Uses python3
import sys

sequence_dict = {}

def optimal_sequence(n):
    for i in range(n+1):
        sequence_dict[i] = list(op_sequence(i))
    return sequence_dict[n]
def op_sequence(n):
    sequence = []
    if n == 0:
        return sequence
    if n % 3 == 0 and n%2 == 0:
        sequence1 = sequence_dict[n//3]
        sequence2 = sequence_dict[n//2]
        sequence3 = sequence_dict[n-1]
        if len(sequence1) <= len(sequence2) and len(sequence1) <= len(sequence3):
            sequence = sequence1 + [n]
        elif len(sequence2) <= len(sequence1) and len(sequence2) <= len(sequence3):
            sequence = sequence2 + [n]
        elif len(sequence3) <= len(sequence1) and len(sequence3) <= len(sequence2):
            sequence = sequence3 + [n]
    elif n%3 == 0:
        sequence1 = sequence_dict[n//3]
        sequence2 = sequence_dict[n-1]
        if len(sequence1) <= len(sequence2):
            sequence = sequence1 + [n]
        else:
            sequence = sequence2 + [n]
    elif n%2 == 0:
        sequence1 = sequence_dict[n//2]
        sequence2 = sequence_dict[n-1]
        if len(sequence1) <= len(sequence2):
            sequence = sequence1 + [n]
        else:
            sequence = sequence2 + [n]
    else:
         sequence = sequence_dict[n-1] + [n]
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

#
# n = int(input())
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
