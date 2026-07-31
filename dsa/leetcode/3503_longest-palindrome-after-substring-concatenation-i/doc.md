# Longest Palindrome After Substring Concatenation I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3503 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/) |

## Problem Description

### Goal

Given lowercase strings `s` and `t`, choose one contiguous substring of `s` and one contiguous substring of `t`. Either chosen substring may be empty. Concatenate the substring from `s` first and the substring from `t` second; their order cannot be reversed.

Among all such choices whose concatenation is a palindrome, return the greatest possible length. A solution may use characters from both strings, or it may take a palindrome entirely from one string by choosing the other substring to be empty. Substrings must preserve consecutive characters and their original order.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string of length $n$.
- `t`: A nonempty lowercase English string of length $m$.

The constraints are $1 \le n,m \le 30$.

**Return value**

Return the maximum length of a palindrome obtainable as `s[i:j] + t[k:l]`, where either slice may be empty.

### Examples

**Example 1**

- Input: `s = "a", t = "a"`
- Output: `2`
- Explanation: Taking the single character from each string produces `"aa"`.

**Example 2**

- Input: `s = "abc", t = "def"`
- Output: `1`
- Explanation: No characters match across the two strings, but any single character is a palindrome.

**Example 3**

- Input: `s = "b", t = "aaaa"`
- Output: `4`
- Explanation: Choose an empty substring from `s` and all of `t`.

**Example 4**

- Input: `s = "abcde", t = "ecdba"`
- Output: `5`
- Explanation: `"abc"` from `s` followed by `"ba"` from `t` forms `"abcba"`.
