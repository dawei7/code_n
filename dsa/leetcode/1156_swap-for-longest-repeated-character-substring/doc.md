# Swap For Longest Repeated Character Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1156 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [swap-for-longest-repeated-character-substring](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/).

### Goal
Given a string, you may swap two characters at most once. Return the maximum possible length of a substring made of only one repeated character.

### Function Contract
**Inputs**

- `text`: Lowercase input string.

**Return value**

Maximum repeated-character substring length after at most one swap.

### Examples
**Example 1**

- Input: `text = "ababa"`
- Output: `3`

**Example 2**

- Input: `text = "aaabaaa"`
- Output: `6`

**Example 3**

- Input: `text = "aaabbaaa"`
- Output: `4`

---

## Solution
### Approach
Count total occurrences of every character and compress the string into runs `(char, length)`.

For each run, it can be extended by one if another copy of that character exists outside the run. Also check patterns where two runs of the same character are separated by exactly one different character; those two runs can be connected, again capped by the total count of that character.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the string length.
- **Space Complexity**: `O(n)` for the run list, or `O(1)` beyond runs because the alphabet is fixed.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
