from typing import List, Set


def solve(nums: List[int]) -> int:
    ordered = sorted(nums)
    median = ordered[len(ordered) // 2]
    candidates = _nearby_palindromes(median)
    return min(
        sum(abs(value - target) for value in ordered)
        for target in candidates
    )


def _nearby_palindromes(value: int) -> Set[int]:
    text = str(value)
    length = len(text)
    prefix_length = (length + 1) // 2
    prefix = int(text[:prefix_length])
    candidates = {1, 999_999_999}

    lower_boundary = 10 ** (length - 1) - 1
    upper_boundary = 10**length + 1
    if lower_boundary > 0:
        candidates.add(lower_boundary)
    if upper_boundary < 1_000_000_000:
        candidates.add(upper_boundary)

    for candidate_prefix in range(prefix - 2, prefix + 3):
        if candidate_prefix <= 0:
            continue
        left = str(candidate_prefix)
        if length % 2:
            palindrome = int(left + left[-2::-1])
        else:
            palindrome = int(left + left[::-1])
        if 0 < palindrome < 1_000_000_000:
            candidates.add(palindrome)

    return candidates
