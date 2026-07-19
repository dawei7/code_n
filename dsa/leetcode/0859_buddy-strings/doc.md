# Buddy Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 859 |
| Difficulty | Easy |
| Topics | Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/buddy-strings/) |

## Problem Description
### Goal
Given two lowercase strings `s` and `goal`, decide whether exactly one swap within `s` can make it equal to `goal`. A swap chooses two distinct, zero-indexed positions `i` and `j` and exchanges `s[i]` with `s[j]`; for example, swapping positions `0` and `2` in `"abcd"` produces `"cbad"`.

The two chosen letters are allowed to be equal. Consequently, an already matching pair of strings is valid only when `s` contains a repeated letter whose two occurrences can be swapped without changing the string. Return whether a valid pair of swap positions exists.

### Function Contract
**Inputs**

- `s`: a lowercase English string.
- `goal`: another lowercase English string, where $1 \leq \lvert\texttt{s}\rvert, \lvert\texttt{goal}\rvert \leq 2\cdot 10^4$.

Let $n=\lvert\texttt{s}\rvert$.

**Return value**

Return `true` if swapping the letters at exactly two distinct positions in `s` can produce `goal`; otherwise, return `false`.

### Examples
**Example 1**

- Input: `s = "ab", goal = "ba"`
- Output: `true`

Swapping `s[0]` and `s[1]` produces `goal`.

**Example 2**

- Input: `s = "ab", goal = "ab"`
- Output: `false`

The only possible swap changes the string.

**Example 3**

- Input: `s = "aa", goal = "aa"`
- Output: `true`

The two equal letters can be swapped while leaving `s` unchanged.
