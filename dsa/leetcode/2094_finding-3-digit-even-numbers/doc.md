# Finding 3-Digit Even Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2094 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Recursion, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/finding-3-digit-even-numbers/) |

## Problem Description

### Goal

You are given an array `digits` whose elements are decimal digits and may repeat. Choose three distinct array positions and concatenate their digits in any order to form an integer. A valid result must have exactly three digits, so its hundreds digit cannot be zero, and its ones digit must make the number even.

Return every distinct valid integer in increasing order. A digit value may be used repeatedly only when at least that many copies occur in `digits`; different choices of equal-valued positions do not create duplicate output numbers.

### Function Contract

**Input**

- `digits`: an array of $n$ values, where $3 \le n \le 100$.
- Every element is an integer from $0$ through $9$.

**Return value**

Return the sorted list of unique three-digit even integers constructible from the available digit multiplicities.

### Examples

**Example 1**

- Input: `digits = [2, 1, 3, 0]`
- Output: `[102,120,130,132,210,230,302,310,312,320]`

**Example 2**

- Input: `digits = [2, 2, 8, 8, 2]`
- Output: `[222,228,282,288,822,828,882]`
- Explanation: A value may be reused up to its number of copies in the input.

**Example 3**

- Input: `digits = [3, 7, 5]`
- Output: `[]`
