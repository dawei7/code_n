# Number of Equal Count Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2067 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-equal-count-substrings/) |

## Problem Description

### Goal

An equal count substring is a nonempty contiguous part of a lowercase English string in which every distinct letter that appears has the same prescribed frequency `count`. Letters absent from that substring impose no requirement.

Given `s` and the positive integer `count`, return the number of index ranges that form equal count substrings. Count ranges separately even when they contain identical text, and reject any range where at least one present letter occurs either fewer or more than `count` times.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 3\cdot 10^4$.
- `count`: the exact required frequency for every distinct letter in a valid substring, where $1 \le \texttt{count} \le 3\cdot 10^4$.

**Return value**

- Return the number of nonempty contiguous substrings whose every present letter occurs exactly `count` times.

### Examples

**Example 1**

- Input: `s = "aaabcbbcc", count = 3`
- Output: `3`
- Explanation: `"aaa"`, `"bcbbcc"`, and the complete string have one, two, and three distinct letters, respectively, each occurring three times.

**Example 2**

- Input: `s = "abcd", count = 2`
- Output: `0`
- Explanation: No letter occurs twice inside any candidate range.

**Example 3**

- Input: `s = "a", count = 5`
- Output: `0`
- Explanation: The string is shorter than the required frequency.
