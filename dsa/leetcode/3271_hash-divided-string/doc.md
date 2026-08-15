# Hash Divided String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3271 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/hash-divided-string/) |

## Problem Description

### Goal

Given a lowercase string `s` whose length is divisible by `k`, split it from left to right into consecutive, non-overlapping substrings of exactly `k` characters.

Assign each lowercase letter its zero-based alphabet index: `a` has value 0 through `z` with value 25. For each substring, sum its character values, reduce the sum modulo 26, and convert that remainder back to a lowercase letter. Concatenate the generated letters in group order and return the resulting string.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \le n \le 1000$.
- `k`: A group length from 1 through 100 such that $k$ divides $n$.

**Return value**

- A lowercase string of length $n/k$ containing one hash character for each consecutive group.

### Examples

#### Example 1

- **Input:** `s = "abcd", k = 2`
- **Output:** `"bf"`

The groups `"ab"` and `"cd"` have sums 1 and 5.

#### Example 2

- **Input:** `s = "mxz", k = 3`
- **Output:** `"i"`

The only sum is $12 + 23 + 25 = 60$, whose remainder modulo 26 is 8.

#### Example 3

- **Input:** `s = "azby", k = 1`
- **Output:** `"azby"`

Every one-character group hashes to the same character.
