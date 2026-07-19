# Find Smallest Letter Greater Than Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 744 |
| Difficulty | Easy |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) |

## Problem Description
### Goal
Given an array `letters` sorted in non-decreasing order and a character `target`, find the smallest character in the array that is lexicographically greater than `target`.

Return that character. If no stored character is strictly greater, wrap around and return the first character in `letters`. Duplicate letters may appear, equality does not qualify, and the input contains at least two different characters.

### Function Contract
**Inputs**

- `letters`: a nonempty nondecreasing list of lowercase English letters, possibly containing duplicates
- `target`: one lowercase English letter

**Return value**

- The first list value greater than `target`, or `letters[0]` when every value is less than or equal to `target`

### Examples
**Example 1**

- Input: `letters = ["c","f","j"], target = "a"`
- Output: `"c"`

**Example 2**

- Input: `letters = ["c","f","j"], target = "c"`
- Output: `"f"`

**Example 3**

- Input: `letters = ["x","x","y","y"], target = "z"`
- Output: `"x"`
