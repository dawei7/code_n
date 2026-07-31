from typing import List


def solve(ideas: List[str]) -> int:
    suffixes = [set() for _ in range(26)]
    for idea in ideas:
        suffixes[ord(idea[0]) - ord("a")].add(idea[1:])

    answer = 0
    for first in range(26):
        for second in range(first + 1, 26):
            shared = len(suffixes[first] & suffixes[second])
            answer += (
                2
                * (len(suffixes[first]) - shared)
                * (len(suffixes[second]) - shared)
            )
    return answer
