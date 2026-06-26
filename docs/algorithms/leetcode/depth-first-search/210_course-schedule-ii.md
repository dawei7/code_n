# Course Schedule II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_155` |
| Frontend ID | 210 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Official Link | [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii/) |

## Problem Description & Examples
### Goal
There are a total of `num_courses` courses you have to take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

### Function Contract
**Inputs**

- `num_courses`: int
- `prerequisites`: List[List[int]]

**Return value**

List[int] - valid courses order

### Examples
**Example 1**

- Input: `num_courses = 2, prerequisites = [[1, 0]]`
- Output: `[0, 1]`

**Example 2**

- Input: `num_courses = 2, prerequisites = []`
- Output: `[1, 0]`

**Example 3**

- Input: `num_courses = 2, prerequisites = [[0, 1]]`
- Output: `[1, 0]`

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
