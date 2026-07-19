# Valid Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 408 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-word-abbreviation/) |

## Problem Description
### Goal
Given a lowercase `word` and an abbreviation `abbr`, read the abbreviation from left to right. Letter tokens must match the next word character exactly, while a positive decimal number skips that many consecutive characters of the word.

Return `True` only when all abbreviation tokens are valid and consume the entire word exactly. Numeric tokens may contain several digits but cannot begin with zero, cannot represent a zero-length skip, and cannot move past the word's end. Matching only a prefix is insufficient, and abbreviation letters do not stand for arbitrary characters; they remain literal positions in the represented word.

### Function Contract
**Inputs**

- `word`: the original lowercase word
- `abbr`: an abbreviation containing lowercase letters and decimal digits

**Return value**

- Return `True` only when consuming every abbreviation token consumes the entire word without a leading-zero number, mismatch, or overshoot.

### Examples
**Example 1**

- Input: `word = "internationalization", abbr = "i12iz4n"`
- Output: `True`

**Example 2**

- Input: `word = "apple", abbr = "a2e"`
- Output: `False`

**Example 3**

- Input: `word = "substitution", abbr = "s10n"`
- Output: `True`
