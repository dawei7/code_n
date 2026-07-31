# Count Odd Letters from Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3581 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Simulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-odd-letters-from-number/) |

## Problem Description

### Goal

Take the decimal digits of a positive integer `n` in their original order. Replace each digit with its lowercase English name—for example, `4` becomes `"four"` and `1` becomes `"one"`—and concatenate all of those names into one string.

Count how many distinct letters occur an odd number of times in the resulting string. Each qualifying letter contributes once to the answer regardless of how large its odd frequency is.

### Function Contract

**Inputs**

- `n`: An integer where $1\le n\le10^9$.

**Return value**

Return the number of distinct lowercase letters whose frequency in the concatenated digit names is odd.

### Examples

**Example 1**

- Input: `n = 41`
- Output: `5`
- Explanation: The text is `"fourone"`; `f`, `u`, `r`, `n`, and `e` have odd frequencies.

**Example 2**

- Input: `n = 20`
- Output: `5`
- Explanation: The text is `"twozero"`; `t`, `w`, `z`, `e`, and `r` have odd frequencies.

---
