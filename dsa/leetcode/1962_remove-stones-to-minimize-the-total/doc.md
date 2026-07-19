# Remove Stones to Minimize the Total

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1962 |
| Difficulty | Medium |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-stones-to-minimize-the-total/) |

## Problem Description
### Goal
An array `piles` records the number of stones in each pile. Perform exactly
`k` operations. In one operation, choose any pile of current size $p$ and
remove $\lfloor p/2\rfloor$ stones, leaving
$p-\lfloor p/2\rfloor$ stones.

The same pile may be selected more than once. Choose the piles so that the sum
of all remaining stones after the `k` operations is as small as possible, and
return that minimum total.

### Function Contract
**Inputs**

- `piles`: a list of $N$ positive pile sizes, where $1\le N\le10^5$ and each
  size is at most $10^4$.
- `k`: the exact number of operations $K$, where $1\le K\le10^5$.

**Return value**

- The minimum possible total number of stones after exactly $K$ operations.

### Examples
**Example 1**

- Input: `piles = [5, 4, 9], k = 2`
- Output: `12`

**Example 2**

- Input: `piles = [4, 3, 6, 7], k = 3`
- Output: `12`

**Example 3**

- Input: `piles = [9], k = 2`
- Output: `3`
