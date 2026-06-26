# Distribute Repeating Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1655 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask |
| Official Link | [distribute-repeating-integers](https://leetcode.com/problems/distribute-repeating-integers/) |

## Problem Description & Examples
### Goal
Decide whether repeated integers in `nums` can be distributed so each customer
receives exactly their requested quantity of one repeated value.

### Function Contract
**Inputs**

- `nums`: available integers, possibly with duplicates.
- `quantity`: requested counts for each customer.

**Return value**

`true` if all customer quantities can be satisfied; otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], quantity = [2]`
- Output: `false`

**Example 2**

- Input: `nums = [1, 2, 3, 3], quantity = [2]`
- Output: `true`

**Example 3**

- Input: `nums = [1, 1, 2, 2], quantity = [2, 2]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Compress `nums` into frequencies. Use bitmask dynamic programming over
customers: precompute the total quantity for every customer subset, then try to
assign each number frequency to one still-unserved subset whose total demand
fits that frequency.

---

## Complexity Analysis
- **Time Complexity**: `O(f * 3^m)` or similar subset-DP bounds, where `f` is the number of distinct values and `m` is the number of customers.
- **Space Complexity**: `O(2^m)`.
