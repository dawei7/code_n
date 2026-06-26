# Evaluate Division

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_161` |
| Frontend ID | 399 |
| Difficulty | Medium |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path |
| Official Link | [evaluate-division](https://leetcode.com/problems/evaluate-division/) |

## Problem Description & Examples
### Goal
You are given an array of variables `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the query to find the value of `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

### Function Contract
**Inputs**

- `equations`: List[List[str]]
- `values`: List[float]
- `queries`: List[List[str]]

**Return value**

List[float] - division results

### Examples
**Example 1**

- Input: `equations = [["a", "b"]], values = [2.0], queries = [["a", "b"]]`
- Output: `[2.0]`

**Example 2**

- Input: `equations = [['a', 'b'], ['b', 'c']], values = [2.0, 3.0], queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]`
- Output: `[6.0, 0.5, -1.0, 1.0, -1.0]`

**Example 3**

- Input: `custom_case_3`
- Output: `derive by applying the strategy above`

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
