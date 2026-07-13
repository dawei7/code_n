# Find Subarray With Bitwise OR Closest to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3171 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-subarray-with-bitwise-or-closest-to-k](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/).

### Goal
Given an array of integers and a target value `k`, identify a contiguous subarray such that the bitwise OR of all its elements results in a value whose absolute difference from `k` is minimized. Return this minimum absolute difference.

### Function Contract
**Inputs**

- `nums`: A list of integers (1 ≤ nums.length ≤ 10^5, 1 ≤ nums[i] ≤ 10^9).
- `k`: An integer (1 ≤ k ≤ 10^9).

**Return value**

- An integer representing the minimum possible value of `|bitwise_OR(subarray) - k|`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 4, 8], k = 6`
- Output: `1`
- Explanation: The subarray `[2, 4]` has a bitwise OR of 6. The difference is `|6 - 6| = 0`. Wait, if we take `[4, 2]`, OR is 6. If we take `[1, 2, 4]`, OR is 7. `|7-6|=1`.

**Example 2**

- Input: `nums = [1, 2, 4, 8], k = 9`
- Output: `0`
- Explanation: The subarray `[1, 8]` has a bitwise OR of 9. `|9 - 9| = 0`.

**Example 3**

- Input: `nums = [1, 2, 4, 8], k = 100`
- Output: `92`
- Explanation: The maximum possible OR is 15. `|15 - 100| = 85`. Actually, the subarray `[8]` gives 8, `|8-100|=92`.

---

## Solution
### Approach
The problem leverages the property that the bitwise OR of a subarray is non-decreasing as the subarray expands. Since there are at most 30 bits, for any fixed starting position, there are at most 30 distinct bitwise OR values as we extend the subarray to the right. We maintain a set of "active" OR values ending at the current index, which allows us to compute the result in linear time relative to the array size and the number of bits.

### Complexity Analysis
- **Time Complexity**: `O(n * log(max(nums)))`, where `n` is the length of the array. Each element update involves iterating through the bits.
- **Space Complexity**: `O(log(max(nums)))` to store the set of distinct bitwise OR values ending at the current index.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum absolute difference between k and the bitwise OR
    of any contiguous subarray.
    """
    ans = float('inf')
    # active_ors stores the set of bitwise OR values of all subarrays
    # ending at the previous index, mapped to their last seen index
    # (though here we just need the values).
    # Because OR is monotonic, there are at most 30 distinct values.
    active_ors = set()

    for x in nums:
        # New set of OR values ending at current index
        new_ors = {x}
        for val in active_ors:
            new_ors.add(val | x)

        # Update the global minimum difference
        for val in new_ors:
            diff = abs(val - k)
            if diff < ans:
                ans = diff

        active_ors = new_ors

        # Optimization: if we found 0, we can't do better
        if ans == 0:
            return 0

    return int(ans)
```
</details>
