# Longest Common Prefix After at Most One Removal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3460 |
| Difficulty | Medium |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/) |

## Problem Description

### Goal

Given lowercase strings `s` and `t`, choose whether to remove one character from `s`. No character may be removed from `t`, and removing a character from `s` closes the gap between its remaining prefix and suffix in the usual way.

After this optional operation, measure how many initial characters the two strings share before one string ends or the first unequal pair appears. Return the greatest common-prefix length obtainable by either leaving `s` unchanged or deleting exactly one of its characters. The removed character may be at the beginning, middle, or end of `s`.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string from which at most one character may be removed.
- `t`: A nonempty lowercase English string that remains unchanged.

Let $n=\lvert s\rvert$ and $m=\lvert t\rvert$. The constraints are $1 \le n,m \le 10^5$.

**Return value**

Return the maximum possible length of a common prefix of the resulting `s` and `t`.

### Examples

#### Example 1

- **Input:** `s = "madxa", t = "madam"`
- **Output:** `4`

Deleting `s[3]`, the `x`, produces `"mada"`, whose entire length matches the beginning of `t`.

#### Example 2

- **Input:** `s = "leetcode", t = "eetcode"`
- **Output:** `7`

Removing the initial `l` makes `s` equal to `t`.

#### Example 3

- **Input:** `s = "one", t = "one"`
- **Output:** `3`

Leaving `s` unchanged preserves the complete match.

#### Example 4

- **Input:** `s = "a", t = "b"`
- **Output:** `0`

Removing the only character leaves an empty string, while keeping it leaves a mismatch at the first position.
