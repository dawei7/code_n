# Binary Prefix Divisible By 5

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1018 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [binary-prefix-divisible-by-5](https://leetcode.com/problems/binary-prefix-divisible-by-5/) |

## Problem Description & Examples
### Goal
For each prefix of a binary array, interpret that prefix as a binary number and report whether it is divisible by `5`.

### Function Contract
**Inputs**

- `nums`: List[int] containing only `0` and `1`

**Return value**

List[bool] - divisibility result for each prefix

### Examples
**Example 1**

- Input: `nums = [0, 1, 1]`
- Output: `[True, False, False]`

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `[False, False, False]`

**Example 3**

- Input: `nums = [1, 0, 1, 0]`
- Output: `[False, False, True, True]`

---

## Underlying Base Algorithm(s)
Rolling modulo arithmetic over binary prefixes.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space excluding the output
