# Max Dot Product of Two Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1458 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [max-dot-product-of-two-subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/max-dot-product-of-two-subsequences/).

### Goal
Choose a non-empty subsequence from each array, keeping order, so the dot product of the two chosen subsequences is as large as possible.

### Function Contract
**Inputs**

- `nums1`: the first integer list.
- `nums2`: the second integer list.

**Return value**

The maximum dot product of two non-empty subsequences.

### Examples
**Example 1**

- Input: `nums1 = [2,1,-2,5], nums2 = [3,0,-6]`
- Output: `18`

**Example 2**

- Input: `nums1 = [3,-2], nums2 = [2,-6,7]`
- Output: `21`

**Example 3**

- Input: `nums1 = [-1,-1], nums2 = [1,1]`
- Output: `-1`

---

## Solution
### Approach
Dynamic programming similar to sequence alignment. At each pair, either start/take a pair, extend a previous chosen product, or skip one side; initialize so a non-empty pair is required.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`, reducible to `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1, nums2):
    rows, cols = len(nums1), len(nums2)
    dp = [[float("-inf")] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            product = nums1[i - 1] * nums2[j - 1]
            dp[i][j] = max(product, product + max(0, dp[i - 1][j - 1]), dp[i - 1][j], dp[i][j - 1])
    return dp[rows][cols]
```
</details>
