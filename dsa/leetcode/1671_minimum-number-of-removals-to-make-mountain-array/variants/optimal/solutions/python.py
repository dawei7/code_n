from bisect import bisect_left


def solve(nums: list[int]) -> int:
    def increasing_lengths(values: list[int]) -> list[int]:
        tails: list[int] = []
        lengths: list[int] = []
        for value in values:
            position = bisect_left(tails, value)
            if position == len(tails):
                tails.append(value)
            else:
                tails[position] = value
            lengths.append(position + 1)
        return lengths

    increasing = increasing_lengths(nums)
    decreasing = increasing_lengths(nums[::-1])[::-1]
    longest = max(
        increasing[index] + decreasing[index] - 1
        for index in range(1, len(nums) - 1)
        if increasing[index] > 1 and decreasing[index] > 1
    )
    return len(nums) - longest
