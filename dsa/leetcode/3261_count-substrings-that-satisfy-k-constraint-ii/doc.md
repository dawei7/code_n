# Count Substrings That Satisfy K-Constraint II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3261 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/) |

## Problem Description

### Goal

Given a binary string `s`, an integer `k`, and distinct inclusive ranges `[l_i, r_i]`, answer each range independently. Count all non-empty substrings lying entirely inside `s[l_i..r_i]` that contain at most `k` zeroes or at most `k` ones.

The condition uses inclusive OR: exceeding the zero limit alone does not invalidate a substring if its one count remains within the limit, and vice versa. Return the counts in the same order as the queries. Substrings are identified by their positions, so equal text in different intervals is counted separately.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$, where $1 \le n \le 10^5$.
- `k`: A positive integer, where $1 \le k \le n$.
- `queries`: Between 1 and $10^5$ distinct pairs `[l, r]` satisfying $0 \le l \le r < n$.

Let $q$ be the number of queries.

**Return value**

- A list of $q$ counts; entry `i` counts valid substrings contained in the inclusive range from `queries[i][0]` through `queries[i][1]`.

### Examples

**Example 1**

- Input: `s = "0001111", k = 2, queries = [[0,6]]`
- Output: `[26]`

Only `"000111"` and `"0001111"` exceed both count limits.

**Example 2**

- Input: `s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]`
- Output: `[15,9,3]`

Within this alternating string, substrings longer than three fail the constraint.

**Example 3**

- Input: `s = "11111", k = 1, queries = [[0,4],[1,3],[2,2]]`
- Output: `[15,6,1]`

Every queried substring is valid because its zero count is zero.
