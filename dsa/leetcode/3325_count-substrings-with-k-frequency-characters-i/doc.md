# Count Substrings With K-Frequency Characters I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3325 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/) |

## Problem Description

### Goal

Given a lowercase English string `s` and an integer `k`, examine every nonempty contiguous substring. A substring is valid when at least one character occurs at least `k` times within that substring. The qualifying character is not fixed in advance, and a substring needs only one character to reach the threshold.

Return the total number of valid substrings. Equal text appearing at different index ranges counts separately because substrings are identified by their start and end positions. A longer substring remains valid after extending a valid one, since extension cannot decrease any character frequency.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1\leq n\leq3000$.
- `k`: The required frequency threshold, where $1\leq k\leq n$.

**Return value**

Return the number of index pairs $(i,j)$ with $0\leq i\leq j<n$ such that some character occurs at least `k` times in `s[i..j]`.

### Examples

**Example 1**

- Input: `s = "abacb", k = 2`
- Output: `4`
- Explanation: `"aba"`, `"abac"`, and `"abacb"` qualify through `a`, while `"bacb"` qualifies through `b`.

**Example 2**

- Input: `s = "abcde", k = 1`
- Output: `15`
- Explanation: Every nonempty substring contains a character at least once, so all $5\cdot6/2$ substrings qualify.
