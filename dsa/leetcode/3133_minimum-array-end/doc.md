# Minimum Array End

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3133 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-array-end](https://leetcode.com/problems/minimum-array-end/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-array-end/).

### Goal
You are given two integers `n` and `x`. You want to construct an array of positive integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1] > nums[i]`, and the bitwise AND of all elements in `nums` is `x`.

Return the minimum possible value of `nums[n - 1]`.

### Function Contract
**Inputs**

- `n`: int
- `x`: int

**Return value**

int - minimum possible value of nums[n - 1]

### Examples
**Example 1**

- Input: `n = 3, x = 4`
- Output: `6`

**Example 2**

- Input: `n = 2, x = 7`
- Output: `15`

**Example 3**

- Input: `n = 4, x = 1`
- Output: `7`

---

## Solution
### Approach
- [Count set bits](bit_01_count-set-bits.md)
- [Single number XOR](bit_03_single-number-xor.md)
- [Missing number](bit_10_missing-number.md)
- [Reverse bits](bit_12_reverse-bits.md)

### Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
