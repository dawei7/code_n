# Tallest Billboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 956 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [tallest-billboard](https://leetcode.com/problems/tallest-billboard/) |

## Problem Description

### Goal

You are installing a billboard that needs two steel supports of equal height, one on each side. The supplied `rods` may be welded end to end, so a support's height is the sum of the rods assigned to it.

Assign any disjoint subsets of rods to the two supports; rods may also remain unused. Among all assignments whose two support sums are equal, return the greatest common height. If no positive equal supports can be built, return `0`.

### Function Contract

Let $N$ be the number of rods and define

$$
S = \sum_{r \in \texttt{rods}} r.
$$

**Inputs**

- `rods`: a list of $N$ positive lengths, where $1 \le N \le 20$, `1 <= rods[i] <= 1000`, and $S \le 5000$.

**Return value**

Return the maximum equal height of two supports formed from disjoint rod subsets, or `0` when no positive equal construction exists.

### Examples

**Example 1**

- Input: `rods = [1,2,3,6]`
- Output: `6`
- Explanation: Weld `1`, `2`, and `3` for one support and use `6` for the other.

**Example 2**

- Input: `rods = [1,2,3,4,5,6]`
- Output: `10`
- Explanation: The subsets `{2,3,5}` and `{4,6}` both total 10.

**Example 3**

- Input: `rods = [1,2]`
- Output: `0`
