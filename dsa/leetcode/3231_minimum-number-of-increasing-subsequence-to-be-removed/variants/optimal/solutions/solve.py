from bisect import bisect_right


def solve(nums: list[int]) -> int:
    tails: list[int] = []

    for value in nums:
        transformed = -value
        position = bisect_right(tails, transformed)
        if position == len(tails):
            tails.append(transformed)
        else:
            tails[position] = transformed

    return len(tails)
