"""Optimal solution for LeetCode 1048: Longest String Chain."""


def solve(words: list[str]) -> int:
    longest_by_word: dict[str, int] = {}
    best = 1

    for word in sorted(words, key=len):
        longest = 1
        for index in range(len(word)):
            predecessor = word[:index] + word[index + 1 :]
            longest = max(longest, longest_by_word.get(predecessor, 0) + 1)
        longest_by_word[word] = longest
        best = max(best, longest)

    return best
