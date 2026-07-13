# Construct the Minimum Bitwise Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3315 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [construct-the-minimum-bitwise-array-ii](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/).

### Goal
Given an array of integers `nums`, construct a new array `ans` of the same length such that for each index `i`, `ans[i] | (ans[i] + 1) == nums[i]`. If multiple such `ans[i]` exist, choose the smallest possible value. If no such value exists for a given `nums[i]`, set `ans[i]` to -1.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element is the result of a bitwise OR operation between some integer `x` and `x + 1`.

**Return value**

- A list of integers representing the smallest possible `x` for each `nums[i]`, or -1 if no solution exists.

### Examples
**Example 1**

- Input: `nums = [2, 9, 16]`
- Output: `[1, 8, -1]`

**Example 2**

- Input: `nums = [15, 11, 1]`
- Output: `[7, 3, 0]`

**Example 3**

- Input: `nums = [7]`
- Output: `[3]`

---

## Solution
### Approach
The core observation is that `x | (x + 1)` effectively turns the least significant zero bit of `x` into a one. Specifically, if `x` has a binary representation ending in `...011...1`, then `x + 1` will end in `...100...0`. The OR operation fills all trailing zeros of `x` with ones. To find the smallest `x` such that `x | (x + 1) == target`, we look for the rightmost zero bit in `target` and flip it to zero while setting the bit to its right to one, effectively creating the smallest candidate. If `target` is even, no solution exists (except for 0, but the problem constraints imply target > 0).

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform constant-time bitwise operations for each element.
- **Space Complexity**: `O(n)` to store the resulting array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> list[int]:
    """
    For each target in nums, we want to find the smallest x such that x | (x + 1) == target.
    Let target = x | (x + 1).
    If x has a 0 at bit position k (from right, 0-indexed), then x+1 will have
    a 1 at position k and 0s at all positions < k.
    The OR operation will result in target having 1s at all positions <= k.
    To minimize x, we want to find the lowest bit k such that setting it to 0
    and setting all bits < k to 1 results in a valid x.
    """
    ans = []
    for target in nums:
        # If target is even, it cannot be represented as x | (x + 1)
        # because x | (x + 1) always results in an odd number (the last bit is always 1).
        if target % 2 == 0:
            ans.append(-1)
            continue

        # We look for the rightmost zero bit in target.
        # If we flip the rightmost zero bit of target to 0, and set the bit
        # to its right to 1, we get the smallest x.
        # Example: target = 7 (111). Rightmost zero is at bit 3 (1000).
        # Actually, the logic is: find the first bit 'k' that is 0 in target.
        # The candidate x is target ^ (1 << (k - 1)).

        found = False
        # Check bits from 0 to 30
        for k in range(31):
            if not (target & (1 << k)):
                # Found the rightmost zero at position k
                # The smallest x is obtained by clearing the bit at k-1
                if k > 0:
                    candidate = target ^ (1 << (k - 1))
                    ans.append(candidate)
                    found = True
                    break

        if not found:
            # If target is all 1s (like 1, 3, 7, 15...),
            # the smallest x is target >> 1
            ans.append(target >> 1)

    return ans
```
</details>
