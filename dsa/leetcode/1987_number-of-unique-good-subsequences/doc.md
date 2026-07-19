# Number of Unique Good Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1987 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-unique-good-subsequences/) |

## Problem Description
### Goal
You are given a binary string `binary`. Form a subsequence by deleting any
number of characters while preserving the relative order of the characters
that remain. A good subsequence must be nonempty and may not begin with `0`,
except that the one-character string `"0"` is explicitly allowed.

Count the distinct resulting strings that are good. Different choices of
indices producing the same binary string contribute only once. Return the
number of unique good subsequences modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `binary`: a string of length $N$ containing only `0` and `1`, where
  $1 \le N \le 10^5$.

**Return value**

- The number of distinct nonempty subsequence strings with no leading zero,
  including `"0"` when at least one zero occurs, modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `binary = "001"`
- Output: `2`

The unique good strings are `"0"` and `"1"`.

**Example 2**

- Input: `binary = "11"`
- Output: `2`

The unique good strings are `"1"` and `"11"`.

**Example 3**

- Input: `binary = "101"`
- Output: `5`

The unique good strings are `"0"`, `"1"`, `"10"`, `"11"`, and `"101"`.
