## Problem Description & Examples
### Goal
There are a total of `num_courses` courses you have to take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

Return `True` if you can finish all courses. Otherwise, return `False`.

### Function Contract
**Inputs**

- `num_courses`: int
- `prerequisites`: List[List[int]]

**Return value**

bool - True if possible to finish courses

### Examples
**Example 1**

- Input: `num_courses = 2, prerequisites = [[1, 0]]`
- Output: `True`

**Example 2**

- Input: `num_courses = 2, prerequisites = []`
- Output: `True`

**Example 3**

- Input: `num_courses = 2, prerequisites = [[0, 1]]`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
