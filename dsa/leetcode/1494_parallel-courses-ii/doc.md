# Parallel Courses II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1494 |
| Difficulty | Hard |
| Topics | Dynamic Programming, Bit Manipulation, Graph Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/parallel-courses-ii/) |

## Problem Description
### Goal

There are `n` courses labeled from `1` through `n`. Each pair `[previous, next]` in `relations` means that `previous` must be completed in an earlier semester before `next` may be taken. The prerequisite graph is a directed acyclic graph, so every course can eventually be completed.

In one semester, choose at most `k` courses whose complete prerequisite sets were finished before that semester began. Courses taken together cannot satisfy prerequisites for one another during the same semester. Return the minimum number of semesters needed to finish all `n` courses.

### Function Contract
**Inputs**

Let $N$ be the number of courses and $R$ the number of prerequisite relations.

- `n`: the course count, with $1 \le N \le 15$.
- `relations`: a list of distinct directed pairs `[previous, next]`, with $0 \le R \le N(N-1)/2$.
- Every course label lies from `1` through `n`, and no relation is a self-edge.
- The directed graph described by `relations` is acyclic.
- `k`: the per-semester course limit, with $1 \le k \le N$.

**Return value**

Return the minimum number of semesters required to complete every course while respecting all prerequisites and taking at most `k` courses per semester.

### Examples
**Example 1**

- Input: `n = 4, relations = [[2,1],[3,1],[1,4]], k = 2`
- Output: `3`
- Explanation: Take courses `2` and `3`, then course `1`, then course `4`.

**Example 2**

- Input: `n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2`
- Output: `4`
- Explanation: Only two of courses `2`, `3`, and `4` fit in the first semester, so the remaining prerequisite delays courses `1` and `5`.

**Example 3**

- Input: `n = 11, relations = [], k = 2`
- Output: `6`
- Explanation: With no prerequisites, capacity alone requires $\lceil 11/2 \rceil = 6$ semesters.
