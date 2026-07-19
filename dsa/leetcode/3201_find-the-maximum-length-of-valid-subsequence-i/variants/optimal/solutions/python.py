from typing import List

def solve(nums: List[int]) -> int:
    count_even = 0
    count_odd = 0
    alternating_end_even = 0
    alternating_end_odd = 0

    for x in nums:
        parity = x % 2
        if parity == 0:
            count_even += 1
            alternating_end_even = alternating_end_odd + 1
        else:
            count_odd += 1
            alternating_end_odd = alternating_end_even + 1

    return max(count_even, count_odd, alternating_end_even, alternating_end_odd)
