"""Optimal app-local solution for LeetCode 953."""


def solve(words, order):
    rank = {character: index for index, character in enumerate(order)}

    def ordered(first, second):
        for left, right in zip(first, second):
            if left != right:
                return rank[left] < rank[right]
        return len(first) <= len(second)

    return all(ordered(first, second) for first, second in zip(words, words[1:]))
