# Excel Sheet Column Title

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 168 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/excel-sheet-column-title/) |

## Problem Description
### Goal
Spreadsheet columns are labeled `A` through `Z`, then `AA`, `AB`, and onward, using uppercase letters as a one-based alphabetic numeral system. Given a positive integer `column_number`, determine the label assigned to that numbered column.

Return the complete Excel-style title as a string. Each letter represents a value from `1` through `26`; there is no zero digit, so boundaries such as $26 \to Z$ and `27 -> AA` do not behave like ordinary zero-based base conversion. Preserve the most-significant-to-least-significant letter order and support titles containing as many characters as the input requires.

### Function Contract
**Inputs**

- `column_number`: positive integer column number

**Return value**

Its Excel-style column title.

### Examples
**Example 1**

- Input: `column_number = 1`
- Output: `"A"`

**Example 2**

- Input: `column_number = 28`
- Output: `"AB"`

**Example 3**

- Input: `column_number = 701`
- Output: `"ZY"`
