# Once Twice

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3595 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/once-twice/) |

## Problem Description

### Goal

An integer array contains exactly one value that occurs once and exactly one different value that occurs twice. Every other distinct value occurs exactly three times.

Return a two-element array whose first entry is the once-occurring value and whose second entry is the twice-occurring value. The algorithm must process the input in $O(n)$ time while using $O(1)$ auxiliary space; storing a frequency table is therefore not permitted.

### Function Contract

**Inputs**

- `nums`: An integer array with $3 \leq \lvert\texttt{nums}\rvert \leq 10^5$. Its length is divisible by $3$, every value is a signed 32-bit integer, and the stated once/twice/thrice frequency structure is guaranteed.

**Return value**

Return `[once, twice]`, placing the value with frequency one before the value with frequency two.

### Examples

**Example 1**

- Input: `nums = [2, 2, 3, 2, 5, 5, 5, 7, 7]`
- Output: `[3, 7]`
- Explanation: `3` occurs once, `7` occurs twice, and both remaining values occur three times.

**Example 2**

- Input: `nums = [4, 4, 6, 4, 9, 9, 9, 6, 8]`
- Output: `[8, 6]`
- Explanation: `8` has frequency one and `6` has frequency two.
