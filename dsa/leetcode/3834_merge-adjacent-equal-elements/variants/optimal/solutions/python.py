def solve(nums: list[int]) -> list[int]:
    merged: list[int] = []

    for number in nums:
        while merged and merged[-1] == number:
            merged.pop()
            number *= 2
        merged.append(number)

    return merged
