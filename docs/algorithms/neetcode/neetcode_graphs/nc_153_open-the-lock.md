## Problem Description & Examples
### Goal
You have a lock with 4 circular wheels. Each wheel has 10 slots: `'0'` to `'9'`. The lock starts at `'0000'`. You are given a list of `deadends` keys. If the lock displays any of these keys, the wheels stop turning and you cannot open it.

Given a `target` key, return the minimum total number of turns required to open the lock, or `-1` if it is impossible.

### Function Contract
**Inputs**

- `deadends`: List[str]
- `target`: str

**Return value**

int - minimum turns or -1

### Examples
**Example 1**

- Input: `deadends = ["8888"], target = "0009"`
- Output: `1`

**Example 2**

- Input: `deadends = ['7647', '5938', '2421', '9489', '2411'], target = '6604'`
- Output: `12`

**Example 3**

- Input: `deadends = ['7776'], target = '2914'`
- Output: `8`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
