# Find Maximum Non-decreasing Array Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2945 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Stack, Queue, Monotonic Stack, Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-maximum-non-decreasing-array-length](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/).

### Goal
Given an array of integers, you can perform an operation where you merge adjacent elements into a single element equal to their sum. The objective is to find the maximum number of elements in the resulting array such that the elements are in non-decreasing order.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.

**Return value**

- An integer representing the maximum length of a non-decreasing array achievable through the specified merge operations.

### Examples
**Example 1**

- Input: `nums = [5, 2, 2]`
- Output: `1`
- Explanation: Merging all elements results in `[9]`, which is non-decreasing.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `4`
- Explanation: The array is already non-decreasing.

**Example 3**

- Input: `nums = [4, 3, 2, 6]`
- Output: `3`
- Explanation: Merge 4 and 3 to get `[7, 2, 6]` (not non-decreasing). Merge 3 and 2 to get `[4, 5, 6]`, which is non-decreasing.

---

## Solution
### Approach
The problem is solved using Dynamic Programming optimized with a Monotonic Queue (or a monotonic stack/binary search approach). We define `dp[i]` as the maximum number of elements in a non-decreasing array formed by the prefix `nums[0...i-1]`, and `last[i]` as the minimum possible value of the last element in such an array. By maintaining the prefix sums, we can efficiently determine if a merge is valid and use a monotonic queue to keep track of optimal transitions, reducing the complexity from $O(n^2)$ to $O(n)$.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as each element is processed a constant number of times using the monotonic queue.
- **Space Complexity**: `O(n)` to store the DP arrays and the queue.

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left

def solve(nums: list[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i, num in enumerate(nums):
        prefix_sum[i + 1] = prefix_sum[i] + num

    dp = [0] * (n + 1)
    best_previous = [0] * (n + 2)

    for i in range(1, n + 1):
        best_previous[i] = max(best_previous[i], best_previous[i - 1])
        previous = best_previous[i]
        dp[i] = dp[previous] + 1

        current_sum = prefix_sum[i] - prefix_sum[previous]
        next_prefix = prefix_sum[i] + current_sum
        next_index = bisect_left(prefix_sum, next_prefix)
        if next_index <= n:
            best_previous[next_index] = max(best_previous[next_index], i)

    return dp[n]
```
</details>
