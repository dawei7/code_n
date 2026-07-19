# Zigzag Conversion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 6 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zigzag-conversion/) |

## Problem Description
### Goal
Write the characters of `s` along a zigzag with `numRows` horizontal rows. Starting in the top row, place successive characters while moving straight downward to the bottom row, then diagonally upward one row at a time, repeating that down-and-up path until the string is exhausted.

Read the completed arrangement row by row from top to bottom and concatenate those row contents into the returned string. Placement preserves the original character order along the zigzag path. With one row, or when the string is shorter than the row count, no effective rearrangement occurs.

### Function Contract
**Inputs**

- `s`: `str`
- `numRows`: positive `int`

**Return value**

A `str` containing the row-by-row reading of the zigzag arrangement.

### Examples
**Example 1**

- Input: `s = "PAYPALISHIRING", numRows = 3`
- Output: `"PAHNAPLSIIGYIR"`

**Example 2**

- Input: `s = "PAYPALISHIRING", numRows = 4`
- Output: `"PINALSIGYAHRPI"`

**Example 3**

- Input: `s = "A", numRows = 1`
- Output: `"A"`
