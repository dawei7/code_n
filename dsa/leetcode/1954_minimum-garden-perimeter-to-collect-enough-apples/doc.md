# Minimum Garden Perimeter to Collect Enough Apples

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1954 |
| Difficulty | Medium |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/) |

## Problem Description
### Goal
An infinite two-dimensional garden has an apple tree at every integer
coordinate $(i,j)$. The tree at that coordinate bears
$\lvert i\rvert+\lvert j\rvert$ apples.

Choose an axis-aligned square plot centered at the origin. Trees on the
boundary count as part of the plot, as do all trees in its interior. Given the
number of apples that must be collected, return the smallest possible
perimeter of such a square whose included trees bear at least that many
apples.

### Function Contract
**Inputs**

- `neededApples`: the required number of apples $A$, where
  $1 \le A \le 10^{15}$.

**Return value**

- The minimum perimeter of an axis-aligned square centered at $(0,0)$ that
  contains at least $A$ apples.

### Examples
**Example 1**

- Input: `neededApples = 1`
- Output: `8`

**Example 2**

- Input: `neededApples = 13`
- Output: `16`

**Example 3**

- Input: `neededApples = 1000000000`
- Output: `5040`
