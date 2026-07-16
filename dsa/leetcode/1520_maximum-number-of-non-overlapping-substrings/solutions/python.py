"""Optimal app-local solution for LeetCode 1520."""


def solve(s):
    first = [len(s)] * 26
    last = [-1] * 26
    for index, char in enumerate(s):
        label = ord(char) - ord("a")
        first[label] = min(first[label], index)
        last[label] = index

    answer = []
    selected_end = -1
    for left, char in enumerate(s):
        label = ord(char) - ord("a")
        if first[label] != left:
            continue
        right = last[label]
        index = left
        while index <= right:
            inner = ord(s[index]) - ord("a")
            if first[inner] < left:
                break
            right = max(right, last[inner])
            index += 1
        else:
            substring = s[left : right + 1]
            if left > selected_end:
                answer.append(substring)
            else:
                answer[-1] = substring
            selected_end = right
    return answer
