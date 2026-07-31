"""Optimal app-local solution for LeetCode 3598."""


def solve(words):
    def lcp(first, second):
        length = 0
        limit = min(len(first), len(second))
        while length < limit and first[length] == second[length]:
            length += 1
        return length

    n = len(words)
    adjacent = [lcp(words[i], words[i + 1]) for i in range(n - 1)]

    prefix_max = adjacent[:]
    for i in range(1, n - 1):
        prefix_max[i] = max(prefix_max[i], prefix_max[i - 1])

    suffix_max = adjacent[:]
    for i in range(n - 3, -1, -1):
        suffix_max[i] = max(suffix_max[i], suffix_max[i + 1])

    answer = [0] * n
    for i in range(n):
        if i >= 2:
            answer[i] = max(answer[i], prefix_max[i - 2])
        if i + 1 < n - 1:
            answer[i] = max(answer[i], suffix_max[i + 1])
        if 0 < i < n - 1:
            answer[i] = max(answer[i], lcp(words[i - 1], words[i + 1]))

    return answer
