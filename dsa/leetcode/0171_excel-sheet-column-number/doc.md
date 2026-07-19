# Excel Sheet Column Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 171 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/excel-sheet-column-number/) |

## Problem Description
### Goal
Spreadsheet columns use titles `A` through `Z`, followed by `AA`, `AB`, and longer uppercase sequences. Given a nonempty valid `column_title`, convert that label to its positive one-based column number.

Interpret the letters as digits valued `1` through `26` in a positional alphabetic system: `A` is `1`, `Z` is `26`, and the next title `AA` is `27`. Letter order is significant, with the leftmost character carrying the greatest place value. Return the integer column number only, without normalizing, reordering, or treating the system as ordinary base 26 with a zero digit.

### Function Contract
**Inputs**

- `column_title`: a nonempty string of uppercase letters `A` through `Z`

**Return value**

The corresponding one-based Excel column number.

### Examples
**Example 1**

- Input: `column_title = "A"`
- Output: `1`

**Example 2**

- Input: `column_title = "AB"`
- Output: `28`

**Example 3**

- Input: `column_title = "ZY"`
- Output: `701`
