# Minimum Unlocked Indices to Sort Nums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3431 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/) |

## Problem Description

### Goal

You receive an array `nums` whose entries are only `1`, `2`, or `3`, together with a same-length binary array `locked`. The array is considered sortable when it can be put into non-decreasing order using a restricted adjacent swap.

Indices `i` and `i + 1` may be swapped only when `nums[i] - nums[i + 1] = 1` and `locked[i] = 0`. In one operation, any index may be permanently unlocked by setting its lock value to zero. Find the minimum number of unlock operations that make sorting possible, or return `-1` when even unlocking every index cannot suffice.

### Function Contract

**Inputs**

- `nums`: An array of length $n$ containing only `1`, `2`, and `3`, where $1\le n\le10^5$.
- `locked`: A binary array of length $n$; `locked[i] = 1` means index `i` initially prevents a swap whose left endpoint is there.

**Return value**

Return the minimum number of indices to unlock, or `-1` if the array cannot be sorted under the swap rule.

### Examples

#### Example 1

- **Input:** `nums = [1,2,1,2,3,2], locked = [1,0,1,1,0,1]`
- **Output:** `0`

#### Example 2

- **Input:** `nums = [1,2,1,1,3,2,2], locked = [1,0,1,1,0,1,0]`
- **Output:** `2`

#### Example 3

- **Input:** `nums = [1,2,1,2,3,2,1], locked = [0,0,0,0,0,0,0]`
- **Output:** `-1`
