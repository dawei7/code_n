# Add Minimum Number of Rungs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1936 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/add-minimum-number-of-rungs/) |

## Problem Description
### Goal
A ladder's existing rung heights are given by the strictly increasing integer
array `rungs`. You begin on the floor at height zero and want to reach the
highest existing rung. From the floor or a rung, you may climb to the next
higher rung only when the height difference is at most `dist`.

You may add rungs at positive integer heights that do not already contain a
rung. Insert as few new rungs as possible so that every successive climb from
height zero through the final existing rung respects the distance limit.
Return the minimum number inserted.

### Function Contract
**Inputs**

- `rungs`: a strictly increasing list of $N$ positive integer heights, where
  $1 \le N \le 10^5$ and every height is at most $10^9$.
- `dist`: the maximum permitted height difference in one climb, where
  $1 \le \texttt{dist} \le 10^9$.

**Return value**

- The minimum number of positive-integer rung heights that must be inserted to
  make the last existing rung reachable from height zero.

### Examples
**Example 1**

- Input: `rungs = [1, 3, 5, 10], dist = 2`
- Output: `2`

For example, adding rungs at heights `7` and `8` makes every climb at most two.

**Example 2**

- Input: `rungs = [3, 6, 8, 10], dist = 3`
- Output: `0`

**Example 3**

- Input: `rungs = [3, 4, 6, 7], dist = 2`
- Output: `1`
