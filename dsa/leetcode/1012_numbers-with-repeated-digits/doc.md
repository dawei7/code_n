# Numbers With Repeated Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1012 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [numbers-with-repeated-digits](https://leetcode.com/problems/numbers-with-repeated-digits/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/numbers-with-repeated-digits/).

### Goal
Count how many positive integers from `1` through `n` contain at least one digit that appears more than once.

### Function Contract
**Inputs**

- `n`: Positive integer upper bound.

**Return value**

Number of integers in the inclusive range `[1, n]` that have a repeated decimal digit.

### Examples
**Example 1**

- Input: `n = 20`
- Output: `1`

**Example 2**

- Input: `n = 100`
- Output: `10`

**Example 3**

- Input: `n = 1000`
- Output: `262`

---

## Solution
### Approach
It is easier to count the opposite set: numbers with all unique digits. First count all unique-digit numbers with fewer digits than `n`. Then scan the digits of `n` from left to right and count valid choices for the current position that are smaller than the digit in `n` and not already used.

If a repeated digit appears while scanning `n`, stop because no continuation with that exact prefix can remain unique. Finally subtract the number of unique-digit values from `n` to get the repeated-digit count.

### Complexity Analysis
- **Time Complexity**: `O(d^2)`, where `d` is the number of decimal digits in `n`.
- **Space Complexity**: `O(d)` for the set of used digits.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
