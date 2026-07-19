# Palindrome Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 266 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-permutation/) |

## Problem Description
### Goal
Given a string `s`, determine whether all of its characters can be rearranged to form a palindrome. Reordering may place characters anywhere, but every original occurrence must be used exactly once and no new character may be introduced.

Return `True` when at least one palindromic permutation exists and `False` otherwise. Character identity is exact, so case, spaces, and other supported characters retain their distinctions. An even-length palindrome requires every character count to be even, while an odd-length palindrome may have exactly one odd count. The empty string and any one-character string are valid.

### Function Contract
**Inputs**

- `s`: a string whose character multiplicities may be rearranged

**Return value**

`True` exactly when some permutation of `s` reads the same forward and backward.

### Examples
**Example 1**

- Input: `s = "code"`
- Output: `false`

**Example 2**

- Input: `s = "aab"`
- Output: `true`

**Example 3**

- Input: `s = "carerac"`
- Output: `true`
