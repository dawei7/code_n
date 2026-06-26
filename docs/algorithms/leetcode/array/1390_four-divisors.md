# Four Divisors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1390 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [four-divisors](https://leetcode.com/problems/four-divisors/) |

## Problem Description & Examples
### Goal
For each input number, determine whether it has exactly four positive divisors. If it does, add the sum of those divisors to the answer.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

The total sum of divisors across numbers that have exactly four divisors.

### Examples
**Example 1**

- Input: `nums = [21,4,7]`
- Output: `32`

**Example 2**

- Input: `nums = [10,12]`
- Output: `18`

**Example 3**

- Input: `nums = [16,25]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Divisor enumeration up to the square root. Track found divisor pairs and stop early once more than four divisors are discovered.

---

## Complexity Analysis
- **Time Complexity**: `O(n * sqrt(M))`, where `M` is the largest number.
- **Space Complexity**: `O(1)` besides a small divisor counter/sum.
