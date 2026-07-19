# Rearrange Spaces Between Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1592 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-spaces-between-words/) |

## Problem Description
### Goal

Given a string containing lowercase words and space characters, redistribute all existing spaces. Words are non-empty, appear in their original order, and are initially separated by at least one space; leading and trailing spaces may also be present.

Place the same number of spaces between every adjacent pair of words, maximizing that common number. If the spaces cannot be divided evenly among the gaps, put every leftover space at the end. The result must therefore have exactly the same length as the input.

The input always contains at least one word.

### Function Contract
**Inputs**

- `text`: A string of length $L$, where $1 \le L \le 100$, containing only lowercase English letters and spaces and at least one word.

**Return value**

Return the words in their original order with the maximum equal spacing between adjacent words and any remainder appended after the last word.

### Examples
**Example 1**

- Input: `text = "  this   is  a sentence "`
- Output: `"this   is   a   sentence"`

**Example 2**

- Input: `text = " practice   makes   perfect"`
- Output: `"practice   makes   perfect "`

**Example 3**

- Input: `text = "  hello"`
- Output: `"hello  "`
