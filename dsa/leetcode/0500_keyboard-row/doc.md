# Keyboard Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 500 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/keyboard-row/) |

## Problem Description
### Goal
Given an array of English words, classify letters by the three rows of an American keyboard: `qwertyuiop`, `asdfghjkl`, and `zxcvbnm`. Letter-row membership is case-insensitive, so uppercase and lowercase forms of one letter belong to the same row.

Return the words whose every character can be typed using letters from only one keyboard row. A word may use repeated letters but cannot mix rows, and qualifying words retain their original spelling and case. Return the supplied word values rather than normalized lowercase copies or row numbers; words that require two or three rows are excluded.

### Function Contract
**Inputs**

- `words`: an array of words containing English letters

**Return value**

- The words whose letters all belong to one keyboard row

### Examples
**Example 1**

- Input: `words = ["Hello", "Alaska", "Dad", "Peace"]`
- Output: `["Alaska", "Dad"]`

**Example 2**

- Input: `words = ["omk"]`
- Output: `[]`

**Example 3**

- Input: `words = ["adsdf", "sfd"]`
- Output: `["adsdf", "sfd"]`
