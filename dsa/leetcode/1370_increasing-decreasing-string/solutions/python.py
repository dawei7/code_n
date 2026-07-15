"""Reference solution for LeetCode 1370."""


def solve(s):
    counts = [0] * 26
    for char in s:
        counts[ord(char) - ord("a")] += 1

    answer = []
    remaining = len(s)
    while remaining:
        for index in range(26):
            if counts[index]:
                answer.append(chr(ord("a") + index))
                counts[index] -= 1
                remaining -= 1
        for index in range(25, -1, -1):
            if counts[index]:
                answer.append(chr(ord("a") + index))
                counts[index] -= 1
                remaining -= 1

    return "".join(answer)
