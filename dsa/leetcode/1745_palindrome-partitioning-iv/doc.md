# Palindrome Partitioning IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1745 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iv/) |

## Problem Description

### Goal

Given a lowercase English string `s`, determine whether two cut positions can divide it into exactly three nonempty contiguous substrings such that every substring is a palindrome.

The characters must remain in their original order, every character must belong to exactly one of the three pieces, and a one-character piece counts as a palindrome. Return only whether such a partition exists.

### Function Contract

**Inputs**

- `s`: a lowercase English string with $3 \le n \le 2000$, where $n=\lvert s\rvert$.

**Return value**

- Return `true` if `s` can be partitioned into exactly three nonempty palindromic substrings; otherwise return `false`.

### Examples

**Example 1**

- Input: `s = "abcbdd"`
- Output: `true`
- Explanation: `"a"`, `"bcb"`, and `"dd"` are all palindromes.

**Example 2**

- Input: `s = "bcbddxy"`
- Output: `false`
- Explanation: No placement of two cuts makes all three resulting pieces palindromic.

**Example 3**

- Input: `s = "racecarannakayak"`
- Output: `true`
- Explanation: The string splits as `"racecar"`, `"anna"`, and `"kayak"`.
