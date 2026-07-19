# Evaluate Division

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 399 |
| Difficulty | Medium |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/evaluate-division/) |

## Problem Description
### Goal
Each equation `[a, b]` supplies a positive ratio `a / b = value` between named variables. Ratios may be chained or inverted to infer relationships between other variables in the same connected component, and the supplied equations are consistent.

For every query `[x, y]`, return the inferred floating-point value of $x / y$. Return `-1.0` when either variable is unknown or no relationship path connects them. A known variable divided by itself equals `1.0`, but an entirely unknown $x / x$ still returns `-1.0`. Preserve query order and do not let one disconnected variable component influence another.

### Function Contract
**Inputs**

- `equations`: pairs `[a, b]` representing known divisions $a / b$
- `values`: the positive ratio corresponding to each equation
- `queries`: variable pairs whose division results are requested

**Return value**

- Return one floating-point result per query. Unknown variables or variables in disconnected relationship components produce `-1.0`.

### Examples
**Example 1**

- Input: `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`
- Output: `[6.0,0.5,-1.0,1.0,-1.0]`

**Example 2**

- Input: `equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]`
- Output: `[3.75,0.4,5.0,0.2]`

**Example 3**

- Input: `equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","a"]]`
- Output: `[0.5,2.0,1.0]`
