# Count Array Pairs Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2183 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [count-array-pairs-divisible-by-k](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) |

## Problem Description & Examples
### Goal
Count index pairs whose value product is divisible by `k`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: a positive integer.

**Return value**

The number of pairs `(i, j)` with `i < j` and `(nums[i] * nums[j]) mod k == 0`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`, `k = 2`
- Output: `7`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`, `k = 5`
- Output: `0`

**Example 3**

- Input: `nums = [2, 2, 2]`, `k = 4`
- Output: `3`

---

## Underlying Base Algorithm(s)
Only `gcd(value, k)` matters. Maintain counts of gcd classes seen so far. For each value with class `g`, add the counts of every prior class `h` for which `(g * h) mod k == 0`, then increment class `g`. Iterating over divisors of `k` keeps the state much smaller than the values themselves.

---

## Complexity Analysis
- **Time Complexity**: `O(n * d)`, where `d` is the number of divisors of `k`
- **Space Complexity**: `O(d)`
