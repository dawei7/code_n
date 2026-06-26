# Minimum Average Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2256 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [minimum-average-difference](https://leetcode.com/problems/minimum-average-difference/) |

## Problem Description & Examples
### Goal
Split an array after each index and compare the integer-truncated average of the prefix with that of the remaining suffix. An empty suffix has average zero. Return the earliest index with minimum absolute difference.

### Function Contract
**Inputs**

- `nums`: a nonempty array of nonnegative integers.

**Return value**

The smallest index attaining the minimum average difference.

### Examples
**Example 1**

- Input: `nums = [2, 5, 3, 9, 5, 3]`
- Output: `3`

**Example 2**

- Input: `nums = [0]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Compute the total sum, then scan while maintaining a prefix sum. At index `i`, use integer division for `prefix / (i + 1)` and, when nonempty, `(total - prefix) / (n - i - 1)` for the suffix. Update the answer only on a strictly smaller difference so ties retain the earliest index.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
