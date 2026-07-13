from typing import List

def solve(nums: List[int]) -> List[int]:
    ans = []
    for num in nums:
        if num % 2 == 0:
            ans.append(-1)
            continue

        for bit in range(31):
            if not (num & (1 << bit)):
                ans.append(num ^ (1 << (bit - 1)) if bit > 0 else -1)
                break
        else:
            ans.append(num >> 1)
    return ans
