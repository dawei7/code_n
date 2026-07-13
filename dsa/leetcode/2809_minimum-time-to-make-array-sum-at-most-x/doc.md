# Minimum Time to Make Array Sum At Most x

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2809 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-make-array-sum-at-most-x](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/).

### Goal
Given two integer arrays `nums1` and `nums2` of the same length, you can perform an operation at each second: choose an index `i` and set `nums1[i] = 0`. Simultaneously, every element in `nums1` increases by the corresponding value in `nums2`. Determine the minimum time required to make the sum of `nums1` less than or equal to `x`. If it is impossible, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the initial values.
- `nums2`: A list of integers representing the growth rates.
- `x`: An integer representing the target sum threshold.

**Return value**

- An integer representing the minimum seconds required, or -1 if the target is unreachable.

### Examples
**Example 1**

- Input: `nums1 = [1,2,3], nums2 = [1,2,3], x = 4`
- Output: `3`

**Example 2**

- Input: `nums1 = [1,2,3], nums2 = [3,3,3], x = 4`
- Output: `-1`

**Example 3**

- Input: `nums1 = [1,2,3], nums2 = [1,2,3], x = 10`
- Output: `0`

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with a greedy sorting strategy. By sorting the pairs `(nums2[i], nums1[i])` by their growth rates (`nums2`), we ensure that we prioritize resetting elements that grow faster. The DP state `dp[j]` represents the maximum reduction in the total sum of `nums1` achievable using `j` operations after considering a prefix of the sorted elements.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the arrays, due to the nested loops in the DP transition.
- **Space Complexity**: `O(n)`, as we only need a 1D array to store the DP states for the current number of operations.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1: list[int], nums2: list[int], x: int) -> int:
    n = len(nums1)
    # Pair elements to sort by growth rate (nums2)
    pairs = sorted(zip(nums2, nums1))

    # dp[j] will store the maximum sum reduction possible using j operations
    # after processing some prefix of the sorted pairs.
    dp = [0] * (n + 1)

    # Total sum of nums1 if we did nothing
    sum1 = sum(nums1)
    # Total sum of nums2
    sum2 = sum(nums2)

    for i in range(n):
        b, a = pairs[i]
        # Update DP table backwards to avoid using the same element twice
        for j in range(i + 1, 0, -1):
            # If we perform j operations, the current element contributes
            # its initial value 'a' plus its growth 'b * j' to the reduction.
            dp[j] = max(dp[j], dp[j - 1] + a + b * j)

    for t in range(n + 1):
        # The sum after t seconds is:
        # (Initial sum1 + t * sum2) - (reduction achieved by t operations)
        if sum1 + t * sum2 - dp[t] <= x:
            return t

    return -1
```
</details>
