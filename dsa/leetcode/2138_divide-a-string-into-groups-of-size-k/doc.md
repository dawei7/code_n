# Divide a String Into Groups of Size k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2138 |
| Difficulty | Easy |
| Topics | String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/) |

## Problem Description

### Goal

Partition a lowercase string from left to right into consecutive groups of
exactly $k$ characters. The first group receives the first $k$ characters, the
second receives the next $k$, and each original character belongs to exactly
one group.

If fewer than $k$ original characters remain for the final group, append
enough copies of `fill` to complete it. No padding is added when the string
length is already divisible by $k$. Return all groups in their original order,
so removing only the added final padding and concatenating the groups recovers
the input string.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length from $1$ through $100$.
- `k`: The group size, from $1$ through $100$.
- `fill`: A single lowercase English letter used only for final padding.

**Return value**

The ordered list of length-$k$ groups.

### Examples

#### Example 1

- **Input:** `s = "abcdefghi"`, `k = 3`, `fill = "x"`
- **Output:** `["abc","def","ghi"]`

#### Example 2

- **Input:** `s = "abcdefghij"`, `k = 3`, `fill = "x"`
- **Output:** `["abc","def","ghi","jxx"]`
