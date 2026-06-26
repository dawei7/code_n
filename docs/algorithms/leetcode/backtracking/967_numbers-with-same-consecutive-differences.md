# Numbers With Same Consecutive Differences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 967 |
| Difficulty | Medium |
| Topics | Backtracking, Breadth-First Search |
| Official Link | [numbers-with-same-consecutive-differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) |

## Problem Description & Examples
### Goal
Return all `n`-digit positive integers where the absolute difference between every pair of adjacent digits is exactly `k`.

### Function Contract
**Inputs**

- `n`: int number of digits
- `k`: int required adjacent digit difference

**Return value**

List[int] - all valid numbers

### Examples
**Example 1**

- Input: `n = 3, k = 7`
- Output: `[181, 292, 707, 818, 929]`

**Example 2**

- Input: `n = 2, k = 1`
- Output: `[10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]`

**Example 3**

- Input: `n = 2, k = 0`
- Output: `[11, 22, 33, 44, 55, 66, 77, 88, 99]`

---

## Underlying Base Algorithm(s)
Digit-by-digit backtracking or breadth-first expansion.

---

## Complexity Analysis
- **Time Complexity**: `O(2^n)` worst case
- **Space Complexity**: `O(2^n)` for the frontier/output
