"""Optimal app-local solution for LeetCode 1122: Relative Sort Array."""


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    counts = [0] * 1001
    for value in arr1:
        counts[value] += 1

    answer: list[int] = []
    for value in arr2:
        answer.extend([value] * counts[value])
        counts[value] = 0

    for value, frequency in enumerate(counts):
        answer.extend([value] * frequency)
    return answer
