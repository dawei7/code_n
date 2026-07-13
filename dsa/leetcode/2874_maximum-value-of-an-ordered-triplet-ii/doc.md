# Maximum Value of an Ordered Triplet II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2874 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-value-of-an-ordered-triplet-ii](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/).

### Goal
Given an array of integers, find the maximum value of the expression `(nums[i] - nums[j]) * nums[k]` for all indices `i < j < k`. If the result of the expression is negative, return 0.

### Function Contract
**Inputs**

- `nums`: A list of integers where `3 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^6`.

**Return value**

- An integer representing the maximum possible value of the triplet expression, or 0 if all possible results are negative.

### Examples
**Example 1**

- Input: `nums = [12,6,1,2,7]`
- Output: `77`
- Explanation: The triplet (i=0, j=1, j=2) gives (12 - 6) * 1 = 6. The triplet (i=0, j=1, j=4) gives (12 - 6) * 7 = 42. The triplet (i=0, j=2, j=4) gives (12 - 1) * 7 = 77.

**Example 2**

- Input: `nums = [1,10,3,4,19]`
- Output: `133`
- Explanation: The triplet (i=0, j=2, j=4) gives (1 - 3) * 19 = -38. The triplet (i=1, j=2, j=4) gives (10 - 3) * 19 = 133.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `0`
- Explanation: (1 - 2) * 3 = -3. Since the result is negative, return 0.

---

## Solution
### Approach
The problem is solved using a single-pass linear scan (prefix/suffix tracking). By maintaining the maximum value seen so far (`max_i`) and the maximum difference `(nums[i] - nums[j])` seen so far (`max_diff`), we can calculate the potential result for each index `k` in constant time.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of (nums[i] - nums[j]) * nums[k]
    for i < j < k using a single-pass approach.
    """
    max_val = 0
    max_i = 0
    max_diff = 0

    for x in nums:
        # If we treat the current element as nums[k],
        # the result is max_diff * x.
        max_val = max(max_val, max_diff * x)

        # Update max_diff: the best (nums[i] - nums[j]) seen so far.
        # This is either the previous max_diff or (max_i - current_element).
        max_diff = max(max_diff, max_i - x)

        # Update max_i: the maximum value of nums[i] seen so far.
        max_i = max(max_i, x)

    return max_val
```
</details>
