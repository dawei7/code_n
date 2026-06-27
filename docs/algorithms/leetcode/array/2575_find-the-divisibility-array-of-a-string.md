# Find the Divisibility Array of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2575 |
| Difficulty | Medium |
| Topics | Array, Math, String |
| Official Link | [find-the-divisibility-array-of-a-string](https://leetcode.com/problems/find-the-divisibility-array-of-a-string/) |

## Problem Description & Examples
### Goal
Given a numeric string `word` and an integer `m`, determine for every prefix of the string whether the number represented by that prefix is divisible by `m`. Return an array of integers where the value at each index is 1 if the prefix ending at that index is divisible by `m`, and 0 otherwise.

### Function Contract
**Inputs**

- `word`: A string consisting of digits '0' through '9'.
- `m`: An integer representing the divisor.

**Return value**

- A list of integers (0s and 1s) of the same length as `word`.

### Examples
**Example 1**

- Input: `word = "998244353", m = 3`
- Output: `[1, 1, 0, 0, 0, 1, 0, 1, 1]`

**Example 2**

- Input: `word = "1010", m = 10`
- Output: `[0, 1, 0, 1]`

**Example 3**

- Input: `word = "1", m = 1`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
Modular Arithmetic (specifically the property: `(a * 10 + b) % m = ((a % m) * 10 + b) % m`). This allows us to process the string digit by digit while keeping the running remainder small, preventing integer overflow.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the string, as we iterate through the string exactly once.
- **Space Complexity**: `O(n)` to store the resulting array of size `n`.
