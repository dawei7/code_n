# Perform String Shifts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1427 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/perform-string-shifts/) |

## Problem Description

### Goal

Apply a sequence of cyclic shifts to the string `s`. Each operation is `[direction, amount]`: direction `0` moves the first `amount` characters to the end, while direction `1` moves the last `amount` characters to the front.

Process the operations in their given order and return the resulting string. Shift amounts wrap around the string length, and left and right shifts may partially or completely cancel one another.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 100$.
- `shift`: an array of $q$ operations, where $1 \le q \le 100$.
- Each operation is `[direction, amount]`, with `direction` equal to `0` or `1` and $1 \le \texttt{amount} \le 100$.

**Return value**

- The string obtained after applying every cyclic shift in order.

### Examples

**Example 1**

- Input: `s = "abc", shift = [[0,1],[1,2]]`
- Output: `"cab"`

**Example 2**

- Input: `s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]`
- Output: `"efgabcd"`

**Example 3**

- Input: `s = "abcd", shift = [[0,4],[1,8]]`
- Output: `"abcd"`
