# Maximum Multiplication Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3290 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-multiplication-score](https://leetcode.com/problems/maximum-multiplication-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-multiplication-score/).

### Goal
Given two integer arrays `a` (length 4) and `b` (length `n`), select four indices `i0 < i1 < i2 < i3` from `b` to maximize the sum of products: `a[0]*b[i0] + a[1]*b[i1] + a[2]*b[i2] + a[3]*b[i3]`.

### Function Contract
**Inputs**

- `a`: A list of 4 integers.
- `b`: A list of `n` integers, where `n >= 4`.

**Return value**

- An integer representing the maximum possible score obtained by selecting four indices from `b` in increasing order.

### Examples
**Example 1**

- Input: `a = [3, 2, 5, 6], b = [2, -6, 4, -5, -3, 2, -7]`
- Output: `26`
- Explanation: We choose indices 0, 2, 5, 6. Calculation: `3*2 + 2*4 + 5*2 + 6*(-7)` is not optimal; the optimal selection yields 26.

**Example 2**

- Input: `a = [-1, 4, 5, -2], b = [-5, -4, -3, -2, -1]`
- Output: `-1`

**Example 3**

- Input: `a = [1, 1, 1, 1], b = [1, 1, 1, 1, 1]`
- Output: `4`

---

## Solution
### Approach
Dynamic Programming. Specifically, this is a variation of the "Longest Increasing Subsequence" or "Subset Selection" pattern where we maintain the state of the maximum score achievable after picking the $k$-th element of `a` (where $k \in \{0, 1, 2, 3\}$).

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of array `b`. We iterate through `b` once, performing constant-time updates for each of the 4 states.
- **Space Complexity**: `O(1)`, as we only store the maximum scores for the 4 possible stages of the selection process.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(a: list[int], b: list[int]) -> int:
    # dp[k] stores the maximum score using the first k+1 elements of a
    # Initialize with a very small number to handle negative products
    inf = float('inf')
    dp = [-inf, -inf, -inf, -inf]

    for val in b:
        # Update dp[3]: max score using all 4 elements of a
        # It is either the previous dp[3] or the best dp[2] + a[3]*val
        dp[3] = max(dp[3], dp[2] + a[3] * val)

        # Update dp[2]: max score using first 3 elements of a
        dp[2] = max(dp[2], dp[1] + a[2] * val)

        # Update dp[1]: max score using first 2 elements of a
        dp[1] = max(dp[1], dp[0] + a[1] * val)

        # Update dp[0]: max score using first element of a
        dp[0] = max(dp[0], a[0] * val)

    return int(dp[3])
```
</details>
