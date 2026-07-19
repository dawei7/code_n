# Count Binary Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 696 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/count-binary-substrings/) |

## Problem Description
### Goal
Given a binary string `s`, count its nonempty substrings that contain the same number of `0` characters and `1` characters. Within a valid substring, all zeroes must form one consecutive group and all ones must form one consecutive group.

Count occurrences by their index ranges, so equal substring text appearing in different positions contributes more than once. A candidate containing another change back to the first character is invalid even when its total numbers of zeroes and ones are equal. Return the total number of valid substrings.

### Function Contract
**Inputs**

- `s`: a nonempty binary string

**Return value**

- The number of qualifying substrings, including overlapping occurrences

### Examples
**Example 1**

- Input: `s = "00110011"`
- Output: `6`

**Example 2**

- Input: `s = "10101"`
- Output: `4`

**Example 3**

- Input: `s = "000111"`
- Output: `3`
