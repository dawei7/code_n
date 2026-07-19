# Graph Connectivity With Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1627 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/graph-connectivity-with-threshold/) |

## Problem Description
### Goal
There are $n$ cities labeled from 1 through $n$. Two distinct cities `x` and `y` have a direct bidirectional road exactly when they share some divisor $z$ that is strictly greater than `threshold`: both `x % z == 0` and `y % z == 0` must hold.

For every pair in `queries`, determine whether its two cities are connected either by one such road or indirectly through a path of roads. Return the answers in query order. Duplicate queries are allowed, and reversing a pair does not change its answer.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2 \le n \le 10^4$.
- `threshold`: the exclusive lower bound for a usable common divisor, where $0 \le \texttt{threshold} \le n$.
- `queries`: an array of $q$ distinct-city pairs, where $1 \le q \le 10^5$ and every city label lies from 1 through $n$.

**Return value**

Return a length-$q$ boolean array whose entry is `true` exactly when the corresponding two cities lie in the same connected component of the road graph.

### Examples
**Example 1**

- Input: `n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]`
- Output: `[false,false,true]`

Only cities 3 and 6 share a divisor greater than 2.

**Example 2**

- Input: `n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]`
- Output: `[true,true,true,true,true]`

Divisor 1 is usable, so all cities belong to one component.

**Example 3**

- Input: `n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]`
- Output: `[false,false,false,false,false]`

Cities 2 and 4 have a road, but none of the queried pairs lies within that component.
