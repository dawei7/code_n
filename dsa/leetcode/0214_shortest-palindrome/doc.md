# Shortest Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 214 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-palindrome/) |

## Problem Description
### Goal
Given a string `s`, create a palindrome by adding characters only before its existing first character. The original string must remain intact as a suffix of the result, with its characters in their original order.

Return the shortest palindrome obtainable under this restriction. When several added characters are considered, choose the construction using the fewest prefix characters; the required result is determined by the longest palindromic prefix already present in `s`. A string that is already a palindrome, including the empty string or a one-character string, must be returned unchanged rather than padded unnecessarily.

### Function Contract
**Inputs**

- `s`: a string

**Return value**

The shortest palindrome obtainable only by adding characters before `s`.

### Examples
**Example 1**

- Input: `aacecaaa`
- Output: `aaacecaaa`

**Example 2**

- Input: `abcd`
- Output: `dcbabcd`

**Example 3**

- Input: empty string
- Output: empty string
