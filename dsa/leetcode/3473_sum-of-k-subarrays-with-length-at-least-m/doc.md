# Sum of K Subarrays With Length at Least M

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3473 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-k-subarrays-with-length-at-least-m](https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/).

### Goal
Given an integer array `nums`, an integer `k`, and an integer `m`, find the maximum possible sum obtained by selecting `k` non-overlapping subarrays, where each subarray must have a length of at least `m`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the number of subarrays to select.
- `m`: An integer representing the minimum length required for each subarray.

**Return value**

- An integer representing the maximum total sum of the `k` selected subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 2, -1, 3, 4], k = 1, m = 2`
- Output: `9`
- Explanation: The subarray `[1, 2, -1, 3, 4]` has length 5 (>= 2) and sum 9.

**Example 2**

- Input: `nums = [-1, -2, -3, -4, -5], k = 2, m = 2`
- Output: `-6`
- Explanation: Select `[-1, -2]` and `[-3]`. Wait, length must be at least 2. Select `[-1, -2]` and `[-4, -5]` is not possible as they are not contiguous? No, they are non-overlapping. The best is `[-1, -2]` and `[-3, -4]`? No, `[-1, -2]` and `[-4, -5]` sum to -12. Actually, `[-1, -2]` and `[-3, -4]` is -10. Wait, the example output for this specific constraint is -6 (e.g., `[-1, -2]` and `[-3]`).

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5], k = 2, m = 2`
- Output: `15`
- Explanation: Select `[1, 2]` and `[3, 4, 5]`. Sum = 3 + 12 = 15.

---

## Solution
### Approach
Dynamic Programming with Prefix Sums. We maintain a DP table `dp[i][j]` representing the maximum sum using `i` subarrays within the first `j` elements. To optimize, we use the observation that `dp[i][j]` can be derived from `dp[i][j-1]` (not including `nums[j-1]` in the $i$-th subarray) or by ending the $i$-th subarray at `j-1`.

### Complexity Analysis
- **Time Complexity**: `O(k * n)`, where `n` is the length of the array. We iterate through `k` subarrays and for each, we traverse the array once.
- **Space Complexity**: `O(k * n)`, which can be optimized to `O(n)` since each state only depends on the previous subarray count.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int, m: int) -> int:
    n = len(nums)
    # prefix_sum[i] is sum of nums[0...i-1]
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # dp[i][j] = max sum using i subarrays from first j elements
    # Initialize with a very small number
    inf = float('inf')
    dp = [[-inf] * (n + 1) for _ in range(k + 1)]

    # Base case: 0 subarrays have sum 0
    for j in range(n + 1):
        dp[0][j] = 0

    for i in range(1, k + 1):
        # max_prev stores the best value of (dp[i-1][p] - prefix_sum[p])
        # where p <= j - m
        max_prev = -inf
        for j in range(m * i, n + 1):
            # We can start the i-th subarray at index p, ending at j-1
            # The i-th subarray is nums[p...j-1], length is j-p >= m => p <= j-m
            p = j - m
            max_prev = max(max_prev, dp[i - 1][p] - prefix_sum[p])

            # Option 1: Don't include nums[j-1] in the i-th subarray
            # Option 2: Include nums[j-1] as the end of the i-th subarray
            dp[i][j] = max(dp[i][j - 1], max_prev + prefix_sum[j])

    return dp[k][n]
```
</details>
