# Maximum Number of Groups Getting Fresh Donuts

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/) |
| Frontend ID | 1815 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Memoization, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A donut shop bakes exactly `batchSize` donuts at a time. It must finish serving every donut from the current batch before using any donut from the next batch. The integer array `groups` gives the number of customers in each visiting group, and every customer receives exactly one donut. Once a group begins, all of its customers are served before the next group.

A group is happy when its first customer receives the first donut of a fresh batch rather than a donut left over after the preceding group. The groups may be reordered arbitrarily. Return the largest number of groups that can be made happy.

### Function Contract

**Inputs**

- `batchSize`: an integer $b$ satisfying $1 \le b \le 9$.
- `groups`: a list of $n$ positive group sizes, where $1 \le n \le 30$ and each size is at most $10^9$.
- After removing remainder-zero groups and complementary pairs, let $c_r$ be the remaining count with remainder $r$ for $1 \le r < b$, and define

$$
S = \prod_{r=1}^{b-1}(c_r+1).
$$

**Return value**

- Return the maximum number of groups whose first donut can come from a fresh batch after choosing the best ordering.

### Examples

**Example 1**

- Input: `batchSize = 3, groups = [1,2,3,4,5,6]`
- Output: `4`

One optimal ordering is `[6,2,4,5,1,3]`.

**Example 2**

- Input: `batchSize = 4, groups = [1,3,2,5,2,2,1,6]`
- Output: `4`

The best ordering aligns four group starts with batch boundaries.

**Example 3**

- Input: `batchSize = 2, groups = [1,1,1]`
- Output: `2`

The first and third groups start when no donuts are left over.
