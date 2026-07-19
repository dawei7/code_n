"""Optimal app-local solution for LeetCode 1156."""

from collections import Counter


def solve(text: str) -> int:
    total = Counter(text)
    answer = 0
    index = 0
    while index < len(text):
        run_end = index
        while run_end < len(text) and text[run_end] == text[index]:
            run_end += 1

        second_end = run_end + 1
        while second_end < len(text) and text[second_end] == text[index]:
            second_end += 1

        joined = (run_end - index) + (second_end - run_end - 1)
        answer = max(answer, min(joined + 1, total[text[index]]))
        index = run_end
    return answer
