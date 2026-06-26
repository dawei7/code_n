# Maximize Score After N Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1799 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Backtracking, Bit Manipulation, Number Theory, Bitmask |
| Official Link | [maximize-score-after-n-operations](https://leetcode.com/problems/maximize-score-after-n-operations/) |

## Problem Description & Examples
### Goal
There are `2n` numbers. On operation `i`, choose two remaining numbers, gain `i * gcd(a, b)`, and remove them. Maximize the total score.

### Function Contract
**Inputs**

- `nums`: an even-length list of positive integers.

**Return value**

Return the maximum total score.

### Examples
**Example 1**

- Input: `nums = [1,2]`
- Output: `1`

**Example 2**

- Input: `nums = [3,4,6,8]`
- Output: `11`

**Example 3**

- Input: `nums = [1,2,3,4,5,6]`
- Output: `14`

---

## Underlying Base Algorithm(s)
Precompute `gcd` for every pair. Use bitmask DP where a set bit means the number is already used. If `used` numbers are selected, the next operation index is `used / 2 + 1`. Try every unused pair, mark both bits, and maximize the score recursively or iteratively.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 * 2^n)` for `n = len(nums)`
- **Space Complexity**: `O(2^n)`
