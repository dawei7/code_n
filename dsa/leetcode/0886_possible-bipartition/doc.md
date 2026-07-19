# Possible Bipartition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 886 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/possible-bipartition/) |

## Problem Description
### Goal
A group contains `n` people labeled from `1` through `n`. Each pair `[a, b]` in `dislikes` states that person `a` dislikes person `b`, so those two people must not be placed together.

Determine whether everyone can be split into two groups of any size such that the endpoints of every dislike pair belong to different groups. Every person must be assigned to one of the two groups; return `true` when such a bipartition exists and `false` otherwise.

### Function Contract
Let $m = \lvert \texttt{dislikes} \rvert$.

**Inputs**

- `n`: the number of people, where $1 \leq n \leq 2000$.
- `dislikes`: $m$ unique pairs `[a, b]`, where $0 \leq m \leq 10^4$ and $1 \leq a < b \leq n$.

**Return value**

Return `true` if all people can be assigned to two groups while separating every dislike pair; otherwise return `false`.

### Examples
**Example 1**

- Input: `n = 4, dislikes = [[1,2],[1,3],[2,4]]`
- Output: `true`

One valid split is `[1,4]` and `[2,3]`.

**Example 2**

- Input: `n = 3, dislikes = [[1,2],[1,3],[2,3]]`
- Output: `false`

All three people dislike one another, so two groups cannot separate every pair.

**Example 3**

- Input: `n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]`
- Output: `false`
