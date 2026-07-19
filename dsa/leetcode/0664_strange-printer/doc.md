# Strange Printer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 664 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/strange-printer/) |

## Problem Description
### Goal
A strange printer can print only a sequence of one repeated character during each turn. In a turn, choose that character and any contiguous interval of positions; the new characters cover whatever the printer placed at those positions in earlier turns.

Given a target string `s`, return the minimum number of turns needed to produce it exactly. A turn may deliberately print beyond the positions that ultimately keep its character because later turns can overwrite part of the interval, and the printer begins with no required target characters on the output.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase string to produce on an initially blank strip

**Return value**

- The minimum number of printer turns needed to finish with exactly `s`

### Examples
**Example 1**

- Input: `s = "aaabbb"`
- Output: `2`

**Example 2**

- Input: `s = "aba"`
- Output: `2`

**Example 3**

- Input: `s = "abcabc"`
- Output: `5`
