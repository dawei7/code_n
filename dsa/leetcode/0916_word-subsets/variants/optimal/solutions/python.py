"""Optimal app-local solution for LeetCode 916."""


def solve(words1, words2):
    required = [0] * 26

    for word in words2:
        counts = [0] * 26
        for letter in word:
            counts[ord(letter) - ord("a")] += 1
        for index in range(26):
            required[index] = max(required[index], counts[index])

    universal = []
    for word in words1:
        counts = [0] * 26
        for letter in word:
            counts[ord(letter) - ord("a")] += 1
        if all(counts[index] >= required[index] for index in range(26)):
            universal.append(word)

    return universal

