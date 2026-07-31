# Distribute Candies Among Children II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2929 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Combinatorics, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-candies-among-children-ii/) |

## Problem Description

### Goal

Distribute all `n` identical candies among three distinct children. A child is
allowed to receive none, and a distribution is determined by the ordered
triple of the three children's non-negative counts. Consequently, assigning
the same three unequal amounts to different children produces different ways.

Each child may receive at most `limit` candies. Count every ordered
distribution whose counts sum exactly to `n` and whose individual counts do
not exceed that inclusive upper bound, then return the total.

### Function Contract

**Inputs**

- `n`: The positive total number of candies to assign.
- `limit`: The inclusive maximum count allowed for each child.

Both values satisfy $1\le\texttt{n},\texttt{limit}\le10^6$.

**Return value**

- The number of ordered triples $(x,y,z)$ such that $x+y+z=\texttt{n}$ and
  $0\le x,y,z\le\texttt{limit}$.

### Examples

**Example 1**

- Input: `n = 5, limit = 2`
- Output: `3`
- Explanation: Exactly `(1, 2, 2)`, `(2, 1, 2)`, and `(2, 2, 1)` satisfy the cap.

**Example 2**

- Input: `n = 3, limit = 3`
- Output: `10`
- Explanation: Every non-negative ordered triple summing to 3 is within the cap.
