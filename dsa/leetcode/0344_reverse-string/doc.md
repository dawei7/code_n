# Reverse String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 344 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-string/) |

## Problem Description
### Goal
Given a mutable array of single-character strings, reverse the complete sequence. The original last character must become first, the original first must become last, and every other pair of mirrored positions must exchange contents.

Modify the supplied array in place and return nothing, using $O(1)$ extra memory rather than allocating another character array or returning a reversed copy. Preserve every character occurrence exactly once, including duplicates, spaces, and symbols. An array of length one remains unchanged, while an odd-length array keeps its middle character at the same index.

### Function Contract
**Inputs**

- `s`: the mutable list of single-character strings

**Return value**

- Returns `None`; after the call, `s` contains its original characters in reverse order.

### Examples
**Example 1**

- Input: `s = ["h", "e", "l", "l", "o"]`
- Output: `["o", "l", "l", "e", "h"]`

**Example 2**

- Input: `s = ["H", "a", "n", "n", "a", "h"]`
- Output: `["h", "a", "n", "n", "a", "H"]`

**Example 3**

- Input: `s = ["x"]`
- Output: `["x"]`
