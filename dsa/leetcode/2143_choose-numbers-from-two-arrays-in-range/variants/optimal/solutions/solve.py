from collections import defaultdict


def solve(nums1: list[int], nums2: list[int]) -> int:
    modulo = 1_000_000_007
    ending: dict[int, int] = {}
    answer = 0

    for first, second in zip(nums1, nums2):
        current = defaultdict(int)
        current[first] += 1
        current[-second] += 1

        for difference, count in ending.items():
            current[difference + first] = (current[difference + first] + count) % modulo
            current[difference - second] = (current[difference - second] + count) % modulo

        ending = current
        answer = (answer + ending[0]) % modulo

    return answer
