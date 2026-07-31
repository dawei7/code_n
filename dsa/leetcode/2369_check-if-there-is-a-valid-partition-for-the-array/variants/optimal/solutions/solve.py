from __future__ import annotations


def solve(nums: list[int]) -> bool:
    n = len(nums)
    dp_i_minus_3 = True
    dp_i_minus_2 = False
    dp_i_minus_1 = nums[0] == nums[1]

    if n == 2:
        return dp_i_minus_1

    for i in range(3, n + 1):
        pair = nums[i - 2] == nums[i - 1]
        triple_equal = nums[i - 3] == nums[i - 2] == nums[i - 1]
        triple_consecutive = nums[i - 3] + 1 == nums[i - 2] and nums[i - 2] + 1 == nums[i - 1]
        current = dp_i_minus_2 and pair or dp_i_minus_3 and (triple_equal or triple_consecutive)
        dp_i_minus_3, dp_i_minus_2, dp_i_minus_1 = (
            dp_i_minus_2,
            dp_i_minus_1,
            current,
        )

    return dp_i_minus_1
