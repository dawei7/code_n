from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    For each num in nums, we need to find the smallest x such that x | (x + 1) == num.
    Let x be the value. x + 1 is the value after flipping the rightmost 0 bit of x to 1
    and all trailing 1s to 0s.
    The OR operation x | (x + 1) results in setting all bits from the rightmost 0 
    position of x to the rightmost bit to 1.
    """
    ans = []
    for num in nums:
        found = False
        # We search for the smallest x. Since x | (x + 1) == num,
        # x must be less than num.
        for x in range(num + 1):
            if (x | (x + 1)) == num:
                ans.append(x)
                found = True
                break
        if not found:
            ans.append(-1)
    return ans
