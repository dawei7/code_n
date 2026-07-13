# Maximum Subarray Sum With Length Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-subarray-sum-with-length-divisible-by-k](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/).

### Goal
Given an integer array `nums` and a positive integer `k`, identify the contiguous subarray whose length is a multiple of `k` and whose sum is the largest possible among all such subarrays.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: A positive integer representing the divisor for the subarray length.

**Return value**

- An integer representing the maximum sum found among all subarrays with length $L$ where $L \equiv 0 \pmod k$.

### Examples
**Example 1**

- Input: `nums = [1, 2], k = 1`
- Output: `3`

**Example 2**

- Input: `nums = [-1, -1, -1, -1, 1, 1, 1, 1], k = 4`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, -3, 4, 5], k = 3`
- Output: `6`

---

## Solution
### Approach
The problem is solved using the **Prefix Sum** technique combined with a **Hash Map (or Array)** to track the minimum prefix sum encountered at each index modulo `k`. By maintaining `min_prefix_sum[i % k]`, we can calculate the sum of any subarray ending at index `j` with length divisible by `k` as `prefix_sum[j] - min_prefix_sum[j % k]`.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we perform a single pass over the array.
- **Space Complexity**: $O(k)$, as we only store the minimum prefix sum for each of the $k$ possible remainders.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    n = len(nums)
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    # min_prefix_at_rem[r] stores the minimum prefix_sums[i]
    # encountered so far where i % k == r
    min_prefix_at_rem = [float('inf')] * k
    min_prefix_at_rem[0] = 0

    max_sum = float('-inf')

    for i in range(1, n + 1):
        rem = i % k
        # If we have seen a prefix sum with the same remainder,
        # the subarray between that index and i has length divisible by k.
        if min_prefix_at_rem[rem] != float('inf'):
            current_subarray_sum = prefix_sums[i] - min_prefix_at_rem[rem]
            if current_subarray_sum > max_sum:
                max_sum = current_subarray_sum

        # Update the minimum prefix sum for this remainder
        if prefix_sums[i] < min_prefix_at_rem[rem]:
            min_prefix_at_rem[rem] = prefix_sums[i]

    return int(max_sum)
```
</details>
