# Detect Capital

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 520 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-capital/) |

## Problem Description
### Goal
Given a nonempty English word, its use of capitals is correct in exactly three forms: every letter is uppercase, every letter is lowercase, or only the first letter is uppercase while all later letters are lowercase.

Return `True` when the complete word matches one of those forms and `False` otherwise. A one-letter word is valid whether its sole letter is uppercase or lowercase. Mixed patterns such as a lowercase first letter followed by an uppercase letter, or several capitals after the first position, do not qualify; the function does not modify the word's spelling.

### Function Contract
**Inputs**

- `word`: a nonempty string of English letters

**Return value**

- `True` when the capitalization matches an accepted form; otherwise `False`

### Examples
**Example 1**

- Input: `word = "USA"`
- Output: `True`

**Example 2**

- Input: `word = "FlaG"`
- Output: `False`

**Example 3**

- Input: `word = "Google"`
- Output: `True`
