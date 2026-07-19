# Minimum Suffix Flips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1529 |
| Difficulty | Medium |
| Topics | String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-suffix-flips/) |

## Problem Description
### Goal

Let `s` be a length-$n$ binary string initially containing only `0` bits. The goal is to make `s` equal a given 0-indexed binary string `target`.

One operation chooses an index `i` from 0 through $n-1$ and flips every bit in the inclusive suffix from `i` to $n-1$: each `0` becomes `1`, and each `1` becomes `0`. Return the minimum number of suffix-flip operations needed to obtain `target`.

### Function Contract
**Inputs**

- `target`: A binary string of length $n$, where $1 \leq n \leq 10^5$.

**Return value**

Return the smallest number of suffix flips that transforms the all-zero string into `target`.

### Examples
**Example 1**

- Input: `target = "10111"`
- Output: `3`
- Explanation: The required bit changes occur at the start, between `1` and `0`, and between `0` and `1`.

**Example 2**

- Input: `target = "101"`
- Output: `3`
- Explanation: Each adjacent boundary changes the bit that the constructed string must show.

**Example 3**

- Input: `target = "00000"`
- Output: `0`
- Explanation: The initial all-zero string already equals the target.
