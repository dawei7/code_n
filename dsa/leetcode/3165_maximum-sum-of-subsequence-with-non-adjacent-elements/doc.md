# Maximum Sum of Subsequence With Non-adjacent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3165 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Dynamic Programming, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-of-subsequence-with-non-adjacent-elements](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/).

### Goal
Given an array of integers and a series of point updates, calculate the maximum sum of a subsequence such that no two elements in the subsequence are adjacent in the original array. After each update, return the total sum of these maximums across all queries, modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `queries`: A list of lists, where each `queries[i]` contains `[index, val]`, representing an update to set `nums[index] = val`.

**Return value**

- An integer representing the sum of the maximum non-adjacent subsequence sums after each query, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [3, 5, 9], queries = [[1, -2], [0, -3]]`
- Output: `21`
- Explanation: After [1, -2], nums is [3, -2, 9], max sum is 12. After [0, -3], nums is [-3, -2, 9], max sum is 9. 12 + 9 = 21.

**Example 2**

- Input: `nums = [0, -1], queries = [[0, -5]]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 1, 4, 9], queries = [[3, 0], [1, 0]]`
- Output: `16`

---

## Solution
### Approach
The problem is solved using a **Segment Tree**. Each node in the tree stores four values representing the maximum non-adjacent subsequence sum for its range:
1. `v00`: Neither the first nor the last element of the range is included.
2. `v01`: The last element is included, but the first is not.
3. `v10`: The first element is included, but the last is not.
4. `v11`: Both the first and last elements are included.
Merging two nodes involves combining these states while ensuring the non-adjacency constraint is maintained at the boundary.

### Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`, where N is the length of the array and Q is the number of queries. Each update takes logarithmic time to traverse the segment tree.
- **Space Complexity**: `O(N)` to store the segment tree nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums, queries):
    MOD = 10**9 + 7
    n = len(nums)

    # Each node stores: (v00, v01, v10, v11)
    # v00: max sum excluding both ends
    # v01: max sum excluding start, including end
    # v10: max sum including start, excluding end
    # v11: max sum including both ends
    tree = [(0, 0, 0, 0)] * (4 * n)

    def merge(left, right):
        l00, l01, l10, l11 = left
        r00, r01, r10, r11 = right

        return (
            max(l00 + r10, l01 + r00),
            max(l00 + r11, l01 + r01),
            max(l10 + r10, l11 + r00),
            max(l10 + r11, l11 + r01)
        )

    def build(node, start, end):
        if start == end:
            val = max(0, nums[start])
            tree[node] = (0, 0, 0, val)
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = merge(tree[2 * node], tree[2 * node + 1])

    def update(node, start, end, idx, val):
        if start == end:
            v = max(0, val)
            tree[node] = (0, 0, 0, v)
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = merge(tree[2 * node], tree[2 * node + 1])

    build(1, 0, n - 1)

    total_sum = 0
    for idx, val in queries:
        update(1, 0, n - 1, idx, val)
        res = tree[1]
        total_sum = (total_sum + max(res)) % MOD

    return total_sum
```
</details>
