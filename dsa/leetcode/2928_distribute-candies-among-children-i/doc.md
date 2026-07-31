# Distribute Candies Among Children I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2928 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Combinatorics, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-candies-among-children-i/) |

## Problem Description

### Goal

You have `n` identical candies and three distinct children. Distribute every
candy among them, allowing a child to receive zero candies. Each assignment is
an ordered triple of non-negative counts, so exchanging the amounts received
by two children generally creates a different distribution.

Every child's count must be at most `limit`, including the boundary value
itself. Return the exact number of ordered distributions whose three counts
sum to `n` while all three respect this inclusive cap.

### Function Contract

**Inputs**

- `n`: The positive number of candies that must all be distributed.
- `limit`: The inclusive upper bound on one child's candy count.

Both inputs satisfy $1\le\texttt{n},\texttt{limit}\le50$.

**Return value**

- The number of ordered triples $(x,y,z)$ satisfying $x+y+z=\texttt{n}$ and
  $0\le x,y,z\le\texttt{limit}$.

### Examples

**Example 1**

- Input: `n = 5, limit = 2`
- Output: `3`
- Explanation: The valid triples are `(1, 2, 2)`, `(2, 1, 2)`, and `(2, 2, 1)`.

**Example 2**

- Input: `n = 3, limit = 3`
- Output: `10`
- Explanation: Since the cap equals the total, all ten non-negative ordered triples summing to 3 are valid.
