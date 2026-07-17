from collections import defaultdict
from math import isqrt


def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    modulo = 1_000_000_007
    threshold = isqrt(len(nums)) + 1
    grouped: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for query_index, (start, step) in enumerate(queries):
        grouped[step].append((query_index, start))

    answers = [0] * len(queries)
    for step, pending in grouped.items():
        if step < threshold:
            suffix = [0] * len(nums)
            for index in range(len(nums) - 1, -1, -1):
                suffix[index] = nums[index]
                if index + step < len(nums):
                    suffix[index] += suffix[index + step]
                suffix[index] %= modulo
            for query_index, start in pending:
                answers[query_index] = suffix[start]
        else:
            for query_index, start in pending:
                total = 0
                for index in range(start, len(nums), step):
                    total += nums[index]
                answers[query_index] = total % modulo

    return answers
