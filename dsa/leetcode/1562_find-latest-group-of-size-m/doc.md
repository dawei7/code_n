# Find Latest Group of Size M

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1562 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/find-latest-group-of-size-m/) |

## Problem Description
### Goal

Start with a binary string of length $N$ whose bits are all `0`. The array `arr` is a permutation of the positions from `1` through $N$. At step $i$, change the bit at the 1-based position `arr[i]` to `1`.

A group of ones is a maximal contiguous substring of `1` bits: it cannot be extended by another `1` on either side. Given a target length `m`, return the latest step at which at least one group has length exactly `m`. Return `-1` if no such step occurs.

### Function Contract
**Inputs**

- `arr`: A permutation of all integers from `1` through $N$, where $1 \le N \le 10^5$.
- `m`: The required maximal-group length, with $1 \le m \le N$.

**Return value**

Return the greatest 1-based activation step containing at least one maximal one-group of exactly length `m`, or `-1` when no step qualifies.

### Examples
**Example 1**

- Input: `arr = [3,5,1,2,4], m = 1`
- Output: `4`

**Example 2**

- Input: `arr = [3,1,5,4,2], m = 2`
- Output: `-1`

**Example 3**

- Input: `arr = [1,2,3], m = 3`
- Output: `3`
