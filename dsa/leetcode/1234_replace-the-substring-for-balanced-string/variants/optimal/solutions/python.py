from collections import Counter


def solve(s: str) -> int:
    outside = Counter(s)
    target = len(s) // 4
    answer = len(s)
    left = 0

    for right, character in enumerate(s):
        outside[character] -= 1
        while left <= right and all(outside[value] <= target for value in "QWER"):
            answer = min(answer, right - left + 1)
            outside[s[left]] += 1
            left += 1

    return 0 if all(count == target for count in Counter(s).values()) else answer
