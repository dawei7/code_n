"""Optimal solution for LeetCode 1408: String Matching in an Array."""


def solve(words: list[str]) -> list[str]:
    answer: list[str] = []
    for i, word in enumerate(words):
        if any(i != j and word in other for j, other in enumerate(words)):
            answer.append(word)
    return answer
