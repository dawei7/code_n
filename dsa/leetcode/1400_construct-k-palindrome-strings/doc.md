# Construct K Palindrome Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1400 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/construct-k-palindrome-strings/) |

## Problem Description

### Goal

Given a lowercase English string `s` and an integer `k`, use every character of `s` exactly once to construct exactly `k` nonempty strings. Characters may be rearranged freely among and within the constructed strings.

Determine whether all `k` strings can be palindromes. A palindrome reads identically from left to right and right to left. The task asks only whether such a construction exists; the actual palindromes do not need to be returned.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `k`: the required number of nonempty palindrome strings, where $1 \le k \le 10^5$.

**Return value**

- `true` if all characters can be partitioned into exactly $k$ palindromes; otherwise `false`.

### Examples

**Example 1**

- Input: `s = "annabelle", k = 2`
- Output: `true`

**Example 2**

- Input: `s = "leetcode", k = 3`
- Output: `false`

**Example 3**

- Input: `s = "true", k = 4`
- Output: `true`
