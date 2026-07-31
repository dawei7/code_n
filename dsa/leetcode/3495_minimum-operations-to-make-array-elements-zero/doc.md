# Minimum Operations to Make Array Elements Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3495 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/) |

## Problem Description

### Goal

Each query `[l, r]` independently represents the complete integer array `[l, l + 1, ..., r]`. In one operation, select two entries `a` and `b` from that array and replace them simultaneously by $\lfloor a/4\rfloor$ and $\lfloor b/4\rfloor$. Entries that have already reached zero may still be selected when another entry needs further work.

For every query, find the minimum number of operations that reduces every represented integer to zero. Queries do not share state: each begins from its own inclusive interval. Return the sum of these minimum operation counts over the entire `queries` list.

### Function Contract

**Inputs**

- `queries`: A list of pairs `[l, r]`, each describing every integer from `l` through `r`, inclusive.

There are between $1$ and $10^5$ queries. Every pair satisfies $1\le l<r\le10^9$.

**Return value**

Return the sum of the minimum operation counts for all queries.

### Examples

**Example 1**

- Input: `queries = [[1,2],[2,4]]`
- Output: `3`
- Explanation: The interval `[1,2]` needs one paired operation. The interval `[2,4]` needs two, so their contribution is `1 + 2`.

**Example 2**

- Input: `queries = [[2,6]]`
- Output: `4`
- Explanation: Values `2` and `3` need one division step each, while `4`, `5`, and `6` need two each, for eight required steps that can be paired into four operations.
