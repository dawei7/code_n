"""Optimal app-local solution for LeetCode 1002."""


def solve(words):
    common = [0] * 26
    for character in words[0]:
        common[ord(character) - ord("a")] += 1

    for word in words[1:]:
        current = [0] * 26
        for character in word:
            current[ord(character) - ord("a")] += 1
        for index in range(26):
            common[index] = min(common[index], current[index])

    answer = []
    for index, amount in enumerate(common):
        answer.extend([chr(ord("a") + index)] * amount)
    return answer
