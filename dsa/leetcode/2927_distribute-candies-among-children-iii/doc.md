# Distribute Candies Among Children III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2927 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-candies-among-children-iii/) |

## Problem Description

### Goal

Given positive integers `n` and `limit`, distribute all `n` identical candies
among three distinct children. A distribution is an ordered triple of
non-negative candy counts whose sum is `n`, so assigning different counts to
different children creates a different distribution.

No child may receive more than `limit` candies. Return the exact total number of
ordered distributions satisfying that upper bound.

### Function Contract

**Inputs**

- `n`: The positive total number of candies to distribute.
- `limit`: The inclusive maximum number of candies any one child may receive.

The constraints are $1\le\texttt{n}\le10^8$ and
$1\le\texttt{limit}\le10^8$.

**Return value**

- The number of ordered triples $(x,y,z)$ with $x+y+z=\texttt{n}$ and
  $0\le x,y,z\le\texttt{limit}$.

### Examples

**Example 1**

- Input: `n = 5, limit = 2`
- Output: `3`
- Explanation: The valid triples are `(1, 2, 2)`, `(2, 1, 2)`, and `(2, 2, 1)`.

**Example 2**

- Input: `n = 3, limit = 3`
- Output: `10`
- Explanation: The upper bound excludes nothing, so all ten non-negative ordered triples summing to 3 are valid.
