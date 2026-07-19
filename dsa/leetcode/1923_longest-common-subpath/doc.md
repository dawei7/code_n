# Longest Common Subpath

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/longest-common-subpath/) |
| Frontend ID | 1923 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A country has `n` cities numbered from `0` through `n - 1`, with travel possible between every pair. Each of `m` friends records the cities visited along one path in their exact traversal order. A city may occur more than once in a path, although equal cities never appear consecutively.

A subpath is a contiguous sequence of cities from one recorded path. Find the greatest length of a subpath that occurs, with the same city order, in every friend's path. The occurrence may begin at a different index in each path. Return zero when the paths do not even share a single city.

### Function Contract

**Inputs**

- `n`: the number of cities, with $1 \le n \le 10^5$.
- `paths`: an array of $m$ city sequences, where $2 \le m \le 10^5$.
- Every city is in $[0,n-1]$, and the total number of path entries is at most $10^5$.

Let

$$
T = \sum_{p \in \texttt{paths}} \lvert p \rvert
$$

and let $L$ be the length of the shortest path.

**Return value**

- Return the maximum length of a contiguous city sequence appearing in every path.

### Examples

**Example 1**

- Input: `n = 5, paths = [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]`
- Output: `2`

The sequence `[2,3]` occurs contiguously in all three paths.

**Example 2**

- Input: `n = 3, paths = [[0], [1], [2]]`
- Output: `0`

No city is shared by every path.

**Example 3**

- Input: `n = 5, paths = [[0,1,2,3,4], [4,3,2,1,0]]`
- Output: `1`

The paths share cities, but no ordered adjacent pair.
