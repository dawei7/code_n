# Complement of Base 10 Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1009 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [complement-of-base-10-integer](https://leetcode.com/problems/complement-of-base-10-integer/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/complement-of-base-10-integer/).

### Goal
Return the integer represented by flipping every bit in the standard binary representation of `n`. Leading zeros are not part of the representation, so only the bits actually needed to write `n` are flipped.

### Function Contract
**Inputs**

- `n`: Non-negative integer.

**Return value**

Integer value of the bitwise complement over `n`'s significant binary bits.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `2`

**Example 2**

- Input: `n = 7`
- Output: `0`

**Example 3**

- Input: `n = 10`
- Output: `5`

---

## Solution
### Approach
Build a mask containing exactly as many `1` bits as `n` has significant binary bits. For example, `n = 10` is `1010`, so the mask is `1111`. The complement is then `mask XOR n`.

Handle `n = 0` separately, because its complement over the single displayed bit `0` is `1`.

### Complexity Analysis
- **Time Complexity**: `O(log n)`, proportional to the number of bits in `n`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
