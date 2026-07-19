# Letter Case Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 784 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/letter-case-permutation/) |

## Problem Description

### Goal

Given a string `s` containing English letters and decimal digits, independently choose the lowercase or uppercase form of every letter. Digits have no case and must remain unchanged at their original positions.

Return all distinct strings obtainable from those choices, in any order. Every letter position contributes its own binary choice regardless of the cases of other letters, while the character order and string length remain fixed.

### Function Contract

**Inputs**

- `s`: a nonempty string containing only English letters and decimal digits.

**Return value**

- A list containing all case permutations exactly once, in any order.

### Examples

**Example 1**

- Input: `s = "a1b2"`
- Output: `["a1b2","a1B2","A1b2","A1B2"]`
- Explanation: Each of the two letters has two independent case choices.

**Example 2**

- Input: `s = "3z4"`
- Output: `["3z4","3Z4"]`
- Explanation: Only `z` branches into two choices.

**Example 3**

- Input: `s = "12345"`
- Output: `["12345"]`
- Explanation: With no letters, the original digit string is the sole permutation.
