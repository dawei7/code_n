# Find the Maximum Length of a Good Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3176 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-maximum-length-of-a-good-subsequence-i](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/).

### Goal
Given an integer array `nums` and an integer `k`, determine the length of the longest subsequence such that the number of adjacent pairs with different values in the subsequence does not exceed `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum allowed count of adjacent elements that are not equal.

**Return value**

- An integer representing the maximum length of the valid subsequence.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 1, 3], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 1], k = 0`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 1, 2, 1, 2], k = 1`
- Output: `3`

---

## Solution
### Approach
Dynamic Programming. Specifically, we maintain a DP table `dp[v][i]` representing the maximum length of a subsequence ending with value `v` having exactly `i` adjacent unequal pairs. Transitions involve iterating through previous values and updating the state based on whether the current element matches the previous one.

### Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the length of the input array and `k` is the allowed number of unequal adjacent pairs.
- **Space Complexity**: `O(n * k)` in the worst case, though it can be optimized to `O(unique_elements * k)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    dp[val][i] stores the maximum length of a subsequence ending with 'val'
    having exactly 'i' adjacent unequal pairs.
    """
    # dp[val][i]
    dp = defaultdict(lambda: [0] * (k + 1))

    # max_len_with_i[i] stores the maximum length of any subsequence
    # ending with any value having exactly 'i' unequal pairs.
    max_len_with_i = [0] * (k + 1)

    for x in nums:
        new_dp_x = [0] * (k + 1)
        for i in range(k + 1):
            # Option 1: Extend a subsequence ending in x (no new unequal pair)
            new_dp_x[i] = dp[x][i] + 1

            # Option 2: Extend a subsequence ending in a different value (new unequal pair)
            if i > 0:
                new_dp_x[i] = max(new_dp_x[i], max_len_with_i[i - 1] + 1)

        # Update the DP table for value x
        for i in range(k + 1):
            dp[x][i] = max(dp[x][i], new_dp_x[i])
            max_len_with_i[i] = max(max_len_with_i[i], dp[x][i])

    return max(max_len_with_i)
```
</details>
