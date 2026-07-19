# Android Unlock Patterns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 351 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/android-unlock-patterns/) |

## Problem Description
### Goal
On the $3 x 3$ Android keypad, form unlock patterns containing between `m` and `n` keys, inclusive. A pattern can start at any key and may use each of the nine keys at most once.

A move is valid when it goes directly to an unused key without passing through another keypad key, or when any key lying exactly between the endpoints has already appeared earlier in the pattern. Count every distinct ordered pattern satisfying these rules and permitted lengths. Do not count prefixes shorter than `m`, extensions longer than `n`, or paths that jump over an unvisited intermediate key.

### Function Contract
**Inputs**

- `m`: the minimum pattern length
- `n`: the maximum pattern length, with $1 \le m \le n \le 9$

**Return value**

- The number of valid patterns whose lengths lie in the inclusive range `[m, n]`.

### Examples
**Example 1**

- Input: `m = 1, n = 1`
- Output: `9`

**Example 2**

- Input: `m = 1, n = 2`
- Output: `65`

**Example 3**

- Input: `m = 2, n = 2`
- Output: `56`
