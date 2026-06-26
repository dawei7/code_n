# Minimum Operations to Halve Array Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2208 |
| Difficulty | Medium |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Official Link | [minimum-operations-to-halve-array-sum](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) |

## Problem Description & Examples
### Goal
In one operation, choose an array value and replace it with half of its current value. Find the fewest operations needed to reduce the array's total sum by at least half.

### Function Contract
**Inputs**

- `nums`: a list of positive numbers.

**Return value**

The minimum number of halving operations.

### Examples
**Example 1**

- Input: `nums = [5, 19, 8, 1]`
- Output: `3`

**Example 2**

- Input: `nums = [3, 8, 20]`
- Output: `3`

**Example 3**

- Input: `nums = [10]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Keep current values in a max-heap. Repeatedly halve the largest value, add that reduction to a running total, and push the half back. Halving the current maximum gives the greatest possible immediate reduction, so this greedy choice reaches the target in the fewest steps.

---

## Complexity Analysis
- **Time Complexity**: `O((n + operations) log n)`
- **Space Complexity**: `O(n)`
