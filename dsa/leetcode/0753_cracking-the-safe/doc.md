# Cracking the Safe

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 753 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Depth-First Search, Graph Theory, Eulerian Circuit |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cracking-the-safe/) |

## Problem Description

### Goal

A safe password consists of `n` digits, each chosen from `0` through $k - 1$. After each typed digit, the safe tests the most recent `n` entered digits as a password candidate.

Return a shortest string that is guaranteed to try every one of the $k^{n}$ possible passwords as a contiguous length-`n` substring. Overlapping candidates may share typed digits, and any minimum-length string with complete coverage is acceptable. The entered alphabet must use only the allowed `k` digits.

### Function Contract

**Inputs**

- `n`: the positive password length.
- `k`: the alphabet size, using digit characters from `0` through $k - 1$.

**Return value**

- Any minimum-length string containing each of the $k^{n}$ possible passwords at least once.

### Examples

**Example 1**

- Input: `n = 1`, `k = 2`
- Output: `"10"`
- Explanation: Both one-digit passwords occur once; `"01"` would be equally valid.

**Example 2**

- Input: `n = 2`, `k = 2`
- Output: `"01100"`
- Explanation: Its length-two windows are `01`, `11`, `10`, and `00`, covering all four passwords.
