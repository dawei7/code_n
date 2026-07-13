# Fruits Into Baskets III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3479 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [fruits-into-baskets-iii](https://leetcode.com/problems/fruits-into-baskets-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/fruits-into-baskets-iii/).

### Goal
You are given a list of fruits with specific sizes and a list of baskets, each with a maximum capacity. Each fruit must be placed into a basket sequentially. A fruit can only be placed in a basket if the basket's capacity is greater than or equal to the fruit's size, and the basket is currently empty. Among all valid baskets that satisfy the capacity requirement, you must choose the one with the smallest index. If no such basket exists for a fruit, the fruit is discarded. The goal is to determine the total number of fruits that are successfully placed into baskets.

### Function Contract
**Inputs**

- `fruits`: A list of integers representing the sizes of the fruits in the order they arrive.
- `baskets`: A list of integers representing the maximum capacity of each basket.

**Return value**

- An integer representing the total count of fruits that were successfully placed into a basket.

### Examples
**Example 1**

- Input: `fruits = [4, 2, 5, 3], baskets = [3, 5, 4, 7]`
- Output: `3`

**Example 2**

- Input: `fruits = [1, 1, 1], baskets = [1, 1, 1]`
- Output: `3`

**Example 3**

- Input: `fruits = [5, 1, 2, 3, 4], baskets = [4, 3, 2, 1, 5]`
- Output: `2`

---

## Solution
### Approach
The problem requires efficient range queries to find the first index `i` such that `baskets[i] >= fruit_size`. A Segment Tree is the optimal data structure here, where each node stores the maximum capacity in its range. By traversing the tree, we can perform a "find first" operation in O(log N) time. Once a basket is used, its capacity is updated to -1 to mark it as unavailable.

### Complexity Analysis
- **Time Complexity**: O(F log B), where F is the number of fruits and B is the number of baskets. Each fruit requires a O(log B) segment tree search and update.
- **Space Complexity**: O(B) to store the segment tree nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(fruits: list[int], baskets: list[int]) -> int:
    n = len(baskets)
    # Segment tree to store the maximum capacity in a range
    tree = [-1] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = baskets[start]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

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

    def query(node, start, end, fruit_size):
        # If the max in this range is less than fruit_size, no basket here
        if tree[node] < fruit_size:
            return -1
        if start == end:
            return start

        mid = (start + end) // 2
        # Try left child first to find the smallest index
        res = query(2 * node, start, mid, fruit_size)
        if res == -1:
            res = query(2 * node + 1, mid + 1, end, fruit_size)
        return res

    build(1, 0, n - 1)

    placed = 0
    for fruit in fruits:
        idx = query(1, 0, n - 1, fruit)
        if idx != -1:
            placed += 1
            update(1, 0, n - 1, idx, -1)

    return n - placed
```
</details>
