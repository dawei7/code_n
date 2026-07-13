# Armstrong Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1134 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [armstrong-number](https://leetcode.com/problems/armstrong-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/armstrong-number/).

### Goal
Determine whether an integer is an Armstrong number. A number with `k` digits is Armstrong if the sum of each digit raised to the `k`th power equals the original number.

### Function Contract
**Inputs**

- `n`: Positive integer.

**Return value**

Boolean indicating whether `n` is an Armstrong number.

### Examples
**Example 1**

- Input: `n = 153`
- Output: `true`

**Example 2**

- Input: `n = 123`
- Output: `false`

**Example 3**

- Input: `n = 9474`
- Output: `true`

---

## Solution
### Approach
Convert the number to its decimal digits or repeatedly extract digits with modulo arithmetic. Let `k` be the number of digits, then sum `digit ** k` for every digit. The number is Armstrong exactly when this sum equals `n`.

### Complexity Analysis
- **Time Complexity**: `O(d)`, where `d` is the number of decimal digits.
- **Space Complexity**: `O(1)` if digits are processed arithmetically.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
