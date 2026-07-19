# Maximum Number of Occurrences of a Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1297 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) |

## Problem Description
### Goal
Given a lowercase English string `s`, consider every substring whose length is between `minSize` and `maxSize`, inclusive. A candidate is valid only when it contains at most `maxLetters` distinct characters. Occurrences are identified by their positions in `s`, so equal substrings may overlap and each starting position contributes separately.

Among all valid substring values, return the greatest number of occurrences of one value. If no substring satisfies the distinct-character limit, return zero. The requested result is a frequency, not the substring itself.

### Function Contract
**Inputs**

- `s`: a string of length $n$ containing only lowercase English letters, where $1 \le n \le 10^5$.
- `maxLetters`: the maximum permitted number of distinct characters, where $1 \le \texttt{maxLetters} \le 26$.
- `minSize` and `maxSize`: inclusive substring-length bounds satisfying $1 \le \texttt{minSize} \le \texttt{maxSize} \le \min(26,n)$.

**Return value**

The maximum occurrence count among valid substrings, or $0$ when none is valid.

### Examples
**Example 1**

- Input: `s = "aababcaab"`, `maxLetters = 2`, `minSize = 3`, `maxSize = 4`
- Output: `2`
- Explanation: `"aab"` occurs twice and uses only two distinct letters.

**Example 2**

- Input: `s = "aaaa"`, `maxLetters = 1`, `minSize = 3`, `maxSize = 3`
- Output: `2`
- Explanation: The two occurrences of `"aaa"` overlap.

**Example 3**

- Input: `s = "abcde"`, `maxLetters = 2`, `minSize = 3`, `maxSize = 3`
- Output: `0`
- Explanation: Every length-three substring contains three distinct letters.
