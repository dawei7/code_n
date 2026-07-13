# Longest Increasing Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2407 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Dynamic Programming, Binary Indexed Tree, Segment Tree, Queue, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-increasing-subsequence-ii](https://leetcode.com/problems/longest-increasing-subsequence-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-increasing-subsequence-ii/).

### Goal
Given an integer array `nums` and an integer `k`, find the length of the longest subsequence such that for any two consecutive elements in the subsequence, their absolute difference is at most `k`. Specifically, if the subsequence is `s[0], s[1], ..., s[m]`, then `s[i+1] - s[i] <= k` and `s[i+1] > s[i]` must hold for all valid `i`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input sequence.
- `k`: An integer representing the maximum allowed difference between consecutive elements.

**Return value**

- An integer representing the length of the longest subsequence satisfying the condition.

### Examples
**Example 1**

- Input: `nums = [4,2,1,4,3,4,5,8,15], k = 3`
- Output: `5`

**Example 2**

- Input: `nums = [7,4,5,1,8,12,4,7], k = 5`
- Output: `4`

**Example 3**

- Input: `nums = [1,5], k = 1`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a Segment Tree. Since we need to find the maximum length of a subsequence ending at a value `v` such that the previous value was in the range `[v-k, v-1]`, we can treat the values in `nums` as indices in a Segment Tree. The Segment Tree stores the maximum subsequence length found so far for each value. For each number `x` in `nums`, we query the range `[max(1, x-k), x-1]` to find the maximum length, then update the position `x` in the tree with `max_length + 1`.

### Complexity Analysis
- **Time Complexity**: `O(n log M)`, where `n` is the length of `nums` and `M` is the maximum value in `nums` (the range of the segment tree).
- **Space Complexity**: `O(M)`, required to store the segment tree nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    # The maximum value in nums is 10^5 based on problem constraints
    MAX_VAL = 100000
    # Segment tree size: 4 * MAX_VAL is sufficient
    tree = [0] * (4 * (MAX_VAL + 1))

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

    def query(node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return max(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r))

    max_len = 0
    for x in nums:
        # Query the range [max(1, x-k), x-1]
        prev_max = query(1, 1, MAX_VAL, max(1, x - k), x - 1)
        current_len = prev_max + 1
        update(1, 1, MAX_VAL, x, current_len)
        max_len = max(max_len, current_len)

    return max_len
```
</details>
