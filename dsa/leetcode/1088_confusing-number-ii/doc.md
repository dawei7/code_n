# Confusing Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1088 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [confusing-number-ii](https://leetcode.com/problems/confusing-number-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/confusing-number-ii/).

### Goal
Count the positive integers from `1` through `n` that remain valid after a 180-degree digit rotation and become a different number.

### Function Contract
**Inputs**

- `n`: Positive integer upper bound.

**Return value**

Number of confusing numbers in `[1, n]`.

### Examples
**Example 1**

- Input: `n = 20`
- Output: `6`

**Example 2**

- Input: `n = 100`
- Output: `19`

**Example 3**

- Input: `n = 1`
- Output: `0`

---

## Solution
### Approach
Only digits `0`, `1`, `6`, `8`, and `9` can appear in a valid rotated number. Use DFS to generate numbers from these digits without leading zeros, stopping when the value exceeds `n`. For each generated number, compute its rotated value by reversing digit order and mapping `6` to `9` and `9` to `6`.

Count the number when the rotated value differs from the original value.

### Complexity Analysis
- **Time Complexity**: `O(5^d * d)`, where `d` is the number of digits in `n`; only valid-digit candidates are generated.
- **Space Complexity**: `O(d)` for recursion depth.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
