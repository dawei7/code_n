## Problem Description & Examples
### Goal
You are given a 0-indexed integer array `nums`. You are allowed to traverse between index `i` and index `j` (where `i != j`) if and only if `gcd(nums[i], nums[j]) > 1`.

Return `True` if it is possible to traverse between all pairs of indices in `nums`. Otherwise, return `False`.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

bool - True if traversal exists for all pairs

### Examples
**Example 1**

- Input: `nums = [2, 3, 6]`
- Output: `True`

**Example 2**

- Input: `nums = [26, 3]`
- Output: `False`

**Example 3**

- Input: `nums = [10, 49]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
