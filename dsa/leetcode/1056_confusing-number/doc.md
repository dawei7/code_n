# Confusing Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1056 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [confusing-number](https://leetcode.com/problems/confusing-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/confusing-number/).

### Goal
Determine whether rotating every digit of a number by 180 degrees creates a valid number that is different from the original number.

### Function Contract
**Inputs**

- `n`: Non-negative integer.

**Return value**

Boolean indicating whether `n` becomes a different valid number after rotation.

### Examples
**Example 1**

- Input: `n = 6`
- Output: `true`

**Example 2**

- Input: `n = 89`
- Output: `true`

**Example 3**

- Input: `n = 11`
- Output: `false`

---

## Solution
### Approach
Only digits `0`, `1`, `6`, `8`, and `9` remain valid after rotation. Read the digits of `n` from right to left, mapping each digit to its rotated counterpart and building the rotated number in forward order. If any digit is invalid, return `false`.

At the end, the number is confusing exactly when the rotated value is different from the original value.

### Complexity Analysis
- **Time Complexity**: `O(log n)`, proportional to the number of decimal digits.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
