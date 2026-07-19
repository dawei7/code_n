# Largest Time for Given Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 949 |
| Difficulty | Medium |
| Topics | Array, String, Backtracking, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-time-for-given-digits/) |

## Problem Description

### Goal

An array `arr` contains exactly four decimal digits. Rearrange those four supplied occurrences, using every digit exactly once, to form a time in the 24-hour string format `"HH:MM"`.

A valid hour ranges from `"00"` through `"23"`, and a valid minute ranges from `"00"` through `"59"`. Among all valid arrangements, return the latest time of day; `"00:00"` is the earliest possible time and `"23:59"` is the latest. If the digits cannot form any valid 24-hour time, return the empty string `""`.

### Function Contract

**Inputs**

- `arr`: a list of exactly four integers, each from $0$ through $9$. Repeated digits are allowed.

**Return value**

Return the latest valid time as a zero-padded `"HH:MM"` string, or `""` when no permutation is valid.

### Examples

**Example 1**

- Input: `arr = [1, 2, 3, 4]`
- Output: `"23:41"`

Several arrangements form valid times, and `"23:41"` is the latest among them.

**Example 2**

- Input: `arr = [5, 5, 5, 5]`
- Output: `""`

The only distinct arrangement is `"55:55"`, which is not a valid 24-hour time.
