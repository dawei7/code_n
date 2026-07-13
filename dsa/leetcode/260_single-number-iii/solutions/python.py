def solve(nums: list[int]) -> list[int]:
    combined = 0
    for value in nums:
        combined ^= value
    distinguishing_bit = combined & -combined
    first = 0
    second = 0
    for value in nums:
        if value & distinguishing_bit:
            first ^= value
        else:
            second ^= value
    return [first, second]
