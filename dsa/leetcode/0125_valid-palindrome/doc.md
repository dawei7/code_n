# Valid Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 125 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-palindrome/) |

## Problem Description
### Goal
Given a string containing letters, digits, spaces, and punctuation, form its comparison sequence by retaining only alphanumeric characters. Treat uppercase and lowercase forms of the same letter as equal, while retaining digits as meaningful characters.

Return `True` when this normalized sequence reads the same from left to right as from right to left; otherwise return `False`. Character order must remain unchanged during normalization. A string containing no letters or digits reduces to the empty sequence and is therefore a palindrome, as is any normalized sequence containing just one character.

### Function Contract
**Inputs**

- `s`: the original string containing letters, digits, spaces, or punctuation

**Return value**

`True` when the normalized alphanumeric sequence is a palindrome; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `True`

**Example 2**

- Input: `s = "race a car"`
- Output: `False`

**Example 3**

- Input: `s = " "`
- Output: `True`
