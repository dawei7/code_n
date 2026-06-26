# Find the Town Judge

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_145` |
| Frontend ID | 997 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Graph Theory |
| Official Link | [find-the-town-judge](https://leetcode.com/problems/find-the-town-judge/) |

## Problem Description & Examples
### Goal
In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array `trust` where `trust[i] = [a, b]` representing that the person labeled `a` trusts the person labeled `b`.

Return the label of the town judge if the town judge exists and can be identified, or `-1` otherwise.

### Function Contract
**Inputs**

- `n`: int
- `trust`: List[List[int]]

**Return value**

int - judge label or -1

### Examples
**Example 1**

- Input: `n = 2, trust = [[1, 2]]`
- Output: `2`

**Example 2**

- Input: `n = 2, trust = []`
- Output: `-1`

**Example 3**

- Input: `n = 2, trust = [[2, 1]]`
- Output: `1`

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
