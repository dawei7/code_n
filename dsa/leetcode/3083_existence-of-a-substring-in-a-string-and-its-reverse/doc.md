# Existence of a Substring in a String and Its Reverse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3083 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [existence-of-a-substring-in-a-string-and-its-reverse](https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/) |

## Problem Description

### Goal

You are given a string `s`. Form its reverse by reading the characters from right to left. A substring is a contiguous portion of a string, and this problem considers only substrings whose length is exactly $2$; selecting two characters from separated positions does not create a candidate.

Determine whether at least one length-two substring taken from `s` also occurs contiguously somewhere in the reversed string. The two occurrences do not need to have corresponding positions. Return `true` when any qualifying substring exists in both strings, and return `false` when none does.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters, where $1 \le \lvert s \rvert \le 100$.

Only contiguous length-two substrings count; the two characters cannot be selected from non-adjacent positions.

**Return value**

- `true` if some length-two substring of `s` is also a substring of `s[::-1]`; otherwise, `false`.

### Examples

**Example 1**

- Input: `s = "leetcode"`
- Output: `true`
- Explanation: The substring `"ee"` also occurs in `"edocteel"`, the reverse of `s`.

**Example 2**

- Input: `s = "abcba"`
- Output: `true`
- Explanation: Reversing this palindrome leaves it unchanged, so each of its length-two substrings remains present.

**Example 3**

- Input: `s = "abcd"`
- Output: `false`
- Explanation: None of `"ab"`, `"bc"`, or `"cd"` occurs in `"dcba"`.
