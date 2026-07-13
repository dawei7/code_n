# Find First Palindromic String in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2108 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-first-palindromic-string-in-the-array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/).

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

## Solution
### Approach
Scan words in order and compare each with its reverse, or use two pointers from both ends. Return immediately on the first match.

### Complexity Analysis
- **Time Complexity**: `O(total characters)`
- **Space Complexity**: `O(1)` with two-pointer checks.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
