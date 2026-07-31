def solve(nums: list[int]) -> int:
    longest = 0

    for left in range(len(nums)):
        distinct_even: set[int] = set()
        distinct_odd: set[int] = set()

        for right in range(left, len(nums)):
            value = nums[right]
            if value % 2 == 0:
                distinct_even.add(value)
            else:
                distinct_odd.add(value)

            if len(distinct_even) == len(distinct_odd):
                longest = max(longest, right - left + 1)

    return longest
