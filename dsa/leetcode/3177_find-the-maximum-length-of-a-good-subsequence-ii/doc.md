# Find the Maximum Length of a Good Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3177 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-maximum-length-of-a-good-subsequence-ii](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/).

### Goal
Given an integer array `nums` and an integer `k`, determine the length of the longest subsequence such that the number of adjacent pairs with different values in the subsequence does not exceed `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum allowed count of index-adjacent elements that are not equal.

**Return value**

- An integer representing the maximum length of the "good" subsequence.

### Examples
**Example 1**

- Input: `nums = [1,2,1,1,3], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1,2,3,4,5,1], k = 0`
- Output: `2`

**Example 3**

- Input: `nums = [1,1,1,1], k = 0`
- Output: `4`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with state optimization. Let `dp[v][i]` be the maximum length of a good subsequence ending with value `v` having exactly `i` "mismatches" (adjacent unequal elements). To optimize, we maintain `max_len[i]` (the global maximum length for `i` mismatches) and `best_with_val[v][i]` (the max length ending in `v` with `i` mismatches). By tracking the top two values for each `i`, we can update the DP state in $O(n \cdot k)$ time.

### Complexity Analysis
- **Time Complexity**: $O(n \cdot k)$, where $n$ is the length of the input array and $k$ is the allowed mismatch count.
- **Space Complexity**: $O(n \cdot k)$ in the worst case for the DP table, though it can be optimized to $O(k \cdot \text{distinct elements})$.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # dp[i][v] stores the max length of a good subsequence
    # ending with value v having exactly i mismatches.
    # We also track the global max for each i and the best value for each i.

    # dp[i] is a dictionary: {value: max_length}
    dp = [defaultdict(int) for _ in range(k + 1)]

    # max_vals[i] stores (max_len_1, val_1, max_len_2, val_2)
    # to allow O(1) transition when the current element matches the best value.
    max_vals = [[0, -1, 0, -1] for _ in range(k + 1)]

    for x in nums:
        for i in range(k, -1, -1):
            # Option 1: Extend a subsequence ending in x (0 mismatches added)
            res = dp[i][x] + 1

            # Option 2: Extend a subsequence ending in a different value (1 mismatch added)
            if i > 0:
                # Use the best value that isn't x to minimize mismatches
                best_len, best_val, second_len, second_val = max_vals[i-1]
                if best_val != x:
                    res = max(res, best_len + 1)
                else:
                    res = max(res, second_len + 1)

            # Update DP table
            if res > dp[i][x]:
                dp[i][x] = res

                # Update max_vals for this mismatch level i
                m1, v1, m2, v2 = max_vals[i]
                if x == v1:
                    max_vals[i][0] = res
                elif res > m1:
                    max_vals[i] = [res, x, m1, v1]
                elif res > m2 and x != v1:
                    max_vals[i][2] = res
                    max_vals[i][3] = x

    return max(max_vals[i][0] for i in range(k + 1))
```
</details>
