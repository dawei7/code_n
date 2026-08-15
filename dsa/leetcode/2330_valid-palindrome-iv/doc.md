# Valid Palindrome IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2330 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-palindrome-iv/) |

## Problem Description

### Goal

You are given a string of lowercase English letters. One operation chooses any position and changes its character to a different lowercase letter.

Determine whether the string can be made a palindrome using exactly one or exactly two operations. An already-palindromic string can still qualify: a center character can be changed once, or the two characters of a mirrored pair can both be changed to the same different letter. Return a Boolean answer.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length between $1$ and $10^5$.

**Return value**

Return `true` if exactly one or two character replacements can produce a palindrome; otherwise, return `false`.

### Examples

#### Example 1

- **Input:** `s = "abcdba"`
- **Output:** `true`

Only the mirrored pair `c` and `d` disagrees, so changing either character fixes the string in one operation.

#### Example 2

- **Input:** `s = "aa"`
- **Output:** `true`

Changing both characters to the same different letter uses two operations and preserves a palindrome.

#### Example 3

- **Input:** `s = "abcdef"`
- **Output:** `false`

All three mirrored pairs differ, and each pair requires at least one operation.
