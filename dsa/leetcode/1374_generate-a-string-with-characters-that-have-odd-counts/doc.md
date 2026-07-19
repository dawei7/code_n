# Generate a String With Characters That Have Odd Counts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1374 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) |

## Problem Description

### Goal

Given a positive integer `n`, construct any string of length `n` using lowercase English letters such that every distinct character appearing in the string occurs an odd number of times.

More than one answer may satisfy the requirement. Return any valid construction.

The same letter may be used in many positions, and letters that do not appear have no frequency requirement. Only the final length, the lowercase alphabet restriction, and the odd count of each used character determine whether the result is valid.

### Function Contract

**Inputs**

- `n`: an integer with $1 \le n \le 500$ specifying the required string length.

**Return value**

- A lowercase English string of length `n` in which the frequency of every character that appears is odd.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `"aaab"`

**Example 2**

- Input: `n = 2`
- Output: `"ab"`

**Example 3**

- Input: `n = 7`
- Output: `"aaaaaaa"`
