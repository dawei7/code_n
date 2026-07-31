from typing import List


def solve(ideas: List[str]) -> int:
    groups = [set() for _ in range(26)]
    for idea in ideas:
        groups[ord(idea[0]) - 97].add(idea[1:])

    total = 0
    for left in range(26):
        for right in range(left + 1, 26):
            common = len(groups[left].intersection(groups[right]))
            left_only = len(groups[left]) - common
            right_only = len(groups[right]) - common
            total += 2 * left_only * right_only
    return total
