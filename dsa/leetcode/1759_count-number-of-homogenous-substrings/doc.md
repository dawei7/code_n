# Count Number of Homogenous Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1759 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-homogenous-substrings/) |

## Problem Description

### Goal

You are given a string `s` of lowercase English letters. A substring is homogenous when every character in that contiguous, nonempty segment is the same.

Count all homogenous substrings of `s`. Each occurrence is identified by its start and end positions, so occurrences at different positions count separately even when their text is identical. Because the count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: a lowercase English string with $1 \le n \le 10^5$, where $n=\lvert s\rvert$.

Let $M=10^9+7$.

**Return value**

- Return the number of nonempty contiguous substrings whose characters are all equal, reduced modulo $M$.

### Examples

**Example 1**

- Input: `s = "abbcccaa"`
- Output: `13`
- Explanation: Runs of lengths $1$, $2$, $3$, and $2$ contribute $1$, $3$, $6$, and $3$ homogenous substrings.

**Example 2**

- Input: `s = "xy"`
- Output: `2`
- Explanation: Only the two one-character substrings are homogenous.

**Example 3**

- Input: `s = "zzzzz"`
- Output: `15`
- Explanation: A length-five uniform run contains $5+4+3+2+1=15$ homogenous substrings.
