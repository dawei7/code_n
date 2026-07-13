# Count Substrings That Satisfy K-Constraint II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3261 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-substrings-that-satisfy-k-constraint-ii](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/).

### Goal
Given a binary string `s` and an integer `k`, determine the number of substrings within specified ranges `[l, r]` that satisfy the "k-constraint." A substring satisfies the k-constraint if the count of '0's is at most `k` OR the count of '1's is at most `k`. For multiple queries, efficiently calculate the total count of valid substrings contained entirely within each query range.

### Function Contract
**Inputs**

- `s`: A string consisting of characters '0' and '1'.
- `k`: An integer representing the maximum allowed frequency of either '0's or '1's.
- `queries`: A 2D list where each element `[l, r]` defines the start and end indices of a substring range.

**Return value**

- A list of integers where each element corresponds to the count of valid substrings for the respective query.

### Examples
**Example 1**

- Input: `s = "0001111", k = 2, queries = [[0, 6]]`
- Output: `[26]`

**Example 2**

- Input: `s = "010101", k = 1, queries = [[0, 7], [2, 3], [0, 3]]`
- Output: `[15, 3, 6]`

**Example 3**

- Input: `s = "11111", k = 1, queries = [[0, 4]]`
- Output: `[9]`

---

## Solution
### Approach
The solution utilizes a **Sliding Window** to precompute the leftmost valid starting index `left[i]` for every position `i` in the string. By using **Prefix Sums** on the lengths of valid substrings ending at each index, we can answer range queries in constant time. Specifically, for a query `[L, R]`, we identify the valid range `[start, end]` and calculate the sum of valid substrings using the precomputed prefix array.

### Complexity Analysis
- **Time Complexity**: `O(n + q)`, where `n` is the length of the string and `q` is the number of queries. The sliding window takes `O(n)`, and each query is answered in `O(1)`.
- **Space Complexity**: `O(n)` to store the `left` boundary array and the prefix sum array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str, k: int, queries: list[list[int]]) -> list[int]:
    n = len(s)
    left_bound = [0] * n
    # prefix_sum[i] stores the sum of (i - left_bound[i] + 1) for 0 to i-1
    prefix_sum = [0] * (n + 1)

    count = [0, 0]
    left = 0
    for right in range(n):
        count[int(s[right])] += 1
        while count[0] > k and count[1] > k:
            count[int(s[left])] -= 1
            left += 1
        left_bound[right] = left
        prefix_sum[right + 1] = prefix_sum[right] + (right - left + 1)

    results = []
    for l, r in queries:
        # Find the first index 'i' in [l, r] such that left_bound[i] >= l
        # This is the point where the valid window is fully contained within [l, r]
        import bisect
        idx = bisect.bisect_left(left_bound, l, l, r + 1)

        # Substrings ending before idx: start at left_bound[i], end at i.
        # Since left_bound[i] < l, we must cap the start at l.
        # Number of valid substrings = (i - l + 1) * (i - l + 2) // 2
        count_before = (idx - l) * (idx - l + 1) // 2

        # Substrings ending at or after idx: start at left_bound[i], end at i.
        # These are fully contained within [l, r].
        count_after = prefix_sum[r + 1] - prefix_sum[idx]

        results.append(count_before + count_after)

    return results
```
</details>
