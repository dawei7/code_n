# Course Schedule IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1462 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/course-schedule-iv/) |

## Problem Description
### Goal

There are `num_courses` courses labeled from `0` through
`num_courses - 1`. Each pair `[a, b]` in `prerequisites` means course
`a` must be completed before course `b`. All prerequisite pairs are unique,
and together they form a directed acyclic graph.

A prerequisite may be direct or indirect. If `a` precedes `b` and `b`
precedes `c`, then `a` is also a prerequisite of `c`, even when
`[a, c]` is not listed explicitly.

For every pair `[u, v]` in `queries`, determine whether `u` is a
prerequisite of `v`. Return the answers in exactly the same order as the
queries.

### Function Contract
**Inputs**

- `num_courses`: the number $C$ of courses, where $2 \le C \le 100$.
- `prerequisites`: $E$ unique directed pairs `[a, b]`, where
  $0\le E\le C(C-1)/2$, endpoints differ, and the graph has no cycle.
- `queries`: $Q$ directed pairs `[u, v]`, where $1\le Q\le10^4$,
  endpoints are valid course labels, and $u\ne v$.

**Return value**

Return a list of $Q$ booleans. Position $j$ is `true` exactly when a directed
path of one or more prerequisite edges exists from `queries[j][0]` to
`queries[j][1]`.

### Examples
**Example 1**

- Input: `num_courses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]`
- Output: `[false,true]`

**Example 2**

- Input: `num_courses = 2, prerequisites = [], queries = [[1,0],[0,1]]`
- Output: `[false,false]`

**Example 3**

- Input: `num_courses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]`
- Output: `[true,true]`
