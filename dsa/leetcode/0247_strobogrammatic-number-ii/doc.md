# Strobogrammatic Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 247 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strobogrammatic-number-ii/) |

## Problem Description
### Goal
Given a positive integer `n`, generate every decimal string of exactly that length that looks unchanged after a 180-degree rotation. Mirrored positions must use compatible pairs `00`, `11`, `69`, `88`, or `96`, and a middle position in an odd-length numeral must rotate to itself.

Return all valid strobogrammatic strings in any order. Multi-digit results cannot begin with `0`, although the one-digit numeral `"0"` is valid. Include each numeral once and no string of a different length. The task returns textual numerals so their exact digit positions are preserved rather than parsed and reformatted as integers.

### Function Contract
**Inputs**

- `n`: the positive required number of digits

**Return value**

All length-`n` strobogrammatic strings in any order, without leading zeros unless $n = 1$.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `["11","69","88","96"]`

**Example 2**

- Input: `n = 1`
- Output: `["0","1","8"]`

**Example 3**

- Input: `n = 3`
- Output: `["101","111","181","609","619","689","808","818","888","906","916","986"]`
