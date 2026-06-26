# Find First Palindromic String in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2108 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, String |
| Official Link | [find-first-palindromic-string-in-the-array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) |

## Problem Description & Examples
### Goal
Return the first string in the array that reads the same forward and backward.

### Function Contract
**Inputs**

- `words`: a list of strings.

**Return value**

Return the first palindrome, or `""` if none exists.

### Examples
**Example 1**

- Input: `words = ["abc","car","ada","racecar","cool"]`
- Output: `"ada"`

**Example 2**

- Input: `words = ["notapalindrome","racecar"]`
- Output: `"racecar"`

**Example 3**

- Input: `words = ["def","ghi"]`
- Output: `""`

---

## Underlying Base Algorithm(s)
Scan words in order and compare each with its reverse, or use two pointers from both ends. Return immediately on the first match.

---

## Complexity Analysis
- **Time Complexity**: `O(total characters)`
- **Space Complexity**: `O(1)` with two-pointer checks.
