# Handling Sum Queries After Update

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2569 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [handling-sum-queries-after-update](https://leetcode.com/problems/handling-sum-queries-after-update/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/handling-sum-queries-after-update/).

### Goal
You are given two binary arrays of equal length and a series of queries. The queries involve either flipping the bits in a range of the first array or calculating the total sum of the first array. The second array acts as a multiplier for the first array's values during sum calculations. Specifically, the sum is defined as the sum of `nums1[i] * nums2[i]` for all indices `i`.

### Function Contract
**Inputs**

- `nums1`: List[int] (Initial binary array)
- `nums2`: List[int] (Binary array used for weighted sum)
- `queries`: List[List[int]] (List of queries where each query is `[type, l, r]`)

**Return value**

- List[int]: A list containing the results of all type-3 (sum) queries.

### Examples
**Example 1**

- Input: `nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]`
- Output: `[3]`

**Example 2**

- Input: `nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]`
- Output: `[5]`

---

## Solution
### Approach
The problem requires efficient range updates (flipping bits) and range sum queries. A **Segment Tree with Lazy Propagation** is the optimal data structure. Each node in the tree stores the count of `1`s in its range. When a flip operation occurs, the count of `1`s becomes `(range_length - current_count_of_1s)`. The weighted sum is calculated by maintaining the sum of `nums2` for indices where `nums1` is `1`.

### Complexity Analysis
- **Time Complexity**: `O((n + q) log n)`, where `n` is the length of the arrays and `q` is the number of queries. Each segment tree operation takes logarithmic time.
- **Space Complexity**: `O(n)`, required to store the segment tree nodes (typically 4n nodes).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1, nums2, queries):
    n = len(nums1)
    tree = [0] * (4 * n)
    lazy = [False] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = nums1[start]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def push(node, start, end):
        if not lazy[node] or start == end:
            return
        mid = (start + end) // 2
        left = 2 * node
        right = left + 1
        tree[left] = (mid - start + 1) - tree[left]
        lazy[left] = not lazy[left]
        tree[right] = (end - mid) - tree[right]
        lazy[right] = not lazy[right]
        lazy[node] = False

    def update(node, start, end, l, r):
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            tree[node] = (end - start + 1) - tree[node]
            lazy[node] = not lazy[node]
            return
        push(node, start, end)
        mid = (start + end) // 2
        update(2 * node, start, mid, l, r)
        update(2 * node + 1, mid + 1, end, l, r)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    build(1, 0, n - 1)
    total = sum(nums2)
    results = []
    for q in queries:
        if q[0] == 1:
            update(1, 0, n - 1, q[1], q[2])
        elif q[0] == 2:
            total += q[1] * tree[1]
        elif q[0] == 3:
            results.append(total)
    return results
```
</details>
