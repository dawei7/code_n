from typing import List


def solve(nums: List[int]) -> int:
    first_index = {(0, 0): -1}
    prefix_xor = 0
    balance = 0
    longest = 0
    for index, value in enumerate(nums):
        prefix_xor ^= value
        balance += 1 if value % 2 == 0 else -1
        state = (prefix_xor, balance)
        if state in first_index:
            longest = max(longest, index - first_index[state])
        else:
            first_index[state] = index
    return longest
