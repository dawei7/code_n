# Course Schedule IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_157` |
| Frontend ID | 1462 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Official Link | [course-schedule-iv](https://leetcode.com/problems/course-schedule-iv/) |

## Problem Description & Examples
### Goal
There are a total of `num_courses` courses you have to take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `a` first if you want to take course `b`.

You are also given an array `queries` where `queries[j] = [u, v]`. For each query, check if course `u` is a prerequisite of course `v` directly or indirectly.

Return a list of boolean values answering the queries.

### Function Contract
**Inputs**

- `num_courses`: int
- `prerequisites`: List[List[int]]
- `queries`: List[List[int]]

**Return value**

List[bool] - answers to queries

### Examples
**Example 1**

- Input: `num_courses = 2, prerequisites = [[1, 0]], queries = [[1, 0]]`
- Output: `[True]`

**Example 2**

- Input: `num_courses = 3, prerequisites = [[1, 2]], queries = [[1, 1], [1, 2]]`
- Output: `[False, False]`

**Example 3**

- Input: `num_courses = 3, prerequisites = [[0, 1], [1, 2]], queries = [[2, 1], [0, 0]]`
- Output: `[True, False]`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
