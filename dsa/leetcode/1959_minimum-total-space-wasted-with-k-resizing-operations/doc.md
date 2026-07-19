# Minimum Total Space Wasted With K Resizing Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1959 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/) |

## Problem Description
### Goal
The value `nums[t]` is the number of elements stored in a dynamic array at
time `t`. Its allocated size at that time must be at least `nums[t]`, and the
difference between the allocated size and `nums[t]` is wasted space.

Choose any valid initial allocation without counting it as a resize. During
the remaining timeline, the allocation may be changed at most `k` times, to
any sizes that continue to fit the corresponding element counts. Return the
minimum sum of wasted space over every time index.

### Function Contract
**Inputs**

- `nums`: a list of $N$ required element counts, where $1\le N\le200$ and
  $1\le\texttt{nums[i]}\le10^6$.
- `k`: the maximum number of resizing operations, where $0\le k<N$. Define
  $K=k+1$, the maximum number of constant-capacity intervals.

**Return value**

- The minimum total wasted space obtainable with at most `k` resizes.

### Examples
**Example 1**

- Input: `nums = [10, 20], k = 0`
- Output: `10`

**Example 2**

- Input: `nums = [10, 20, 30], k = 1`
- Output: `10`

**Example 3**

- Input: `nums = [10, 20, 15, 30, 20], k = 2`
- Output: `15`
