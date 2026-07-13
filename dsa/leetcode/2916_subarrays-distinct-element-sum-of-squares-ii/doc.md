# Subarrays Distinct Element Sum of Squares II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2916 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [subarrays-distinct-element-sum-of-squares-ii](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/).

### Goal
Calculate the sum of the squares of the count of distinct elements for every possible contiguous subarray of a given integer array. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the sum of the squares of the number of distinct elements in all subarrays, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `15`
- Explanation: Subarrays are [1], [2], [1], [1, 2], [2, 1], [1, 2, 1]. Distinct counts are 1, 1, 1, 2, 2, 2. Squares are 1, 1, 1, 4, 4, 4. Sum = 15.

**Example 2**

- Input: `nums = [2, 2]`
- Output: `3`
- Explanation: Subarrays are [2], [2], [2, 2]. Distinct counts are 1, 1, 1. Squares are 1, 1, 1. Sum = 3.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `14`

---

## Solution
### Approach
The problem is solved using a Segment Tree with Lazy Propagation. We iterate through the array, maintaining the contribution of each subarray ending at the current index `i`. If an element `x` was last seen at index `prev`, adding `x` at index `i` increases the distinct count by 1 for all subarrays starting in the range `(prev, i]`. Using the identity $(x+1)^2 = x^2 + 2x + 1$, we can update the sum of squares efficiently by maintaining the sum of distinct counts and the sum of squares of distinct counts in a segment tree.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the array, due to the segment tree operations performed for each element.
- **Space Complexity**: `O(n)`, required for the segment tree and the hash map storing the last seen indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    # Segment tree stores:
    # sum_sq: sum of squares of distinct counts for subarrays ending at current index
    # sum_val: sum of distinct counts for subarrays ending at current index
    # lazy: lazy propagation value for incrementing distinct counts
    sum_sq = [0] * (4 * n)
    sum_val = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def push_up(node):
        sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
        sum_val[node] = (sum_val[2 * node] + sum_val[2 * node + 1]) % MOD

    def apply(node, start, end, val):
        # (x+v)^2 = x^2 + 2xv + v^2
        # sum((x+v)^2) = sum(x^2) + 2v*sum(x) + v^2 * count
        count = end - start + 1
        sum_sq[node] = (sum_sq[node] + 2 * val * sum_val[node] + val * val * count) % MOD
        sum_val[node] = (sum_val[node] + val * count) % MOD
        lazy[node] += val

    def push_down(node, start, end):
        if lazy[node] != 0:
            mid = (start + end) // 2
            apply(2 * node, start, mid, lazy[node])
            apply(2 * node + 1, mid + 1, end, lazy[node])
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l <= start and end <= r:
            apply(node, start, end, val)
            return
        push_down(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            update(2 * node, start, mid, l, r, val)
        if r > mid:
            update(2 * node + 1, mid + 1, end, l, r, val)
        push_up(node)

    last_seen = {}
    total_sum = 0
    current_sum_sq = 0

    for i, x in enumerate(nums):
        prev = last_seen.get(x, -1)
        # Update range (prev, i]
        update(1, 0, n - 1, prev + 1, i, 1)
        last_seen[x] = i
        # sum_sq[1] now holds the sum of squares of distinct counts for all subarrays ending at i
        total_sum = (total_sum + sum_sq[1]) % MOD

    return total_sum
```
</details>
