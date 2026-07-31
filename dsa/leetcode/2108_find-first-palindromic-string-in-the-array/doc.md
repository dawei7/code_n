# Find First Palindromic String in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2108 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-first-palindromic-string-in-the-array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) |

## Problem Description

### Goal

You are given an array `words` containing lowercase English strings. A string is palindromic when reading its characters from left to right produces exactly the same sequence as reading them from right to left.

Inspect the strings in their existing array order and return the first one that is palindromic. A later palindrome must not replace an earlier qualifying word. If no element satisfies the definition, return the empty string `""`.

### Function Contract

**Inputs**

- `words`: An array of $n$ lowercase English strings, where $1 \le n \le 100$ and every string has length between $1$ and $100$.

Define the total number of input characters as

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

Return the first palindromic string in `words`, or `""` if no palindrome exists.

### Examples

**Example 1**

- Input: `words = ["abc", "car", "ada", "racecar", "cool"]`
- Output: `"ada"`
- Explanation: Both `"ada"` and `"racecar"` are palindromes, but `"ada"` occurs first.

**Example 2**

- Input: `words = ["notapalindrome", "racecar"]`
- Output: `"racecar"`

**Example 3**

- Input: `words = ["def", "ghi"]`
- Output: `""`
- Explanation: Neither string is palindromic.
