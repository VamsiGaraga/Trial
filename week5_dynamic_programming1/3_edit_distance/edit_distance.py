# Uses python3


def edit_distance(s,t):
    edit_dict = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

    def edit_dist(s, t, i, j):
        if s[i-1] == t[j-1]:
            return min(edit_dict[i-1][j] + 1, edit_dict[i][j-1] + 1, edit_dict[i-1][j-1])
        else:
            return min(edit_dict[i-1][j] + 1, edit_dict[i][j-1] + 1, edit_dict[i-1][j-1]+1)
    for i in range(len(s) + 1):
        edit_dict[i][0] = i
    for i in range(1, len(t) + 1):
        edit_dict[0][i] = i
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            edit_dict[i][j] = edit_dist(s, t, i, j)
    return edit_dict[i][j]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

# print(edit_distance(input(),input()))