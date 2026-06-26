# Form Largest Integer With Digits That Add up to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1449 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [form-largest-integer-with-digits-that-add-up-to-target](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) |

## Problem Description & Examples
### Goal
Build the numerically largest possible positive integer whose digit costs sum exactly to `target`. Each digit `1..9` can be used any number of times.

### Function Contract
**Inputs**

- `cost`: `cost[i]` is the cost of digit `i + 1`.
- `target`: the required total cost.

**Return value**

The largest integer as a string, or `"0"` if no exact-cost integer can be formed.

### Examples
**Example 1**

- Input: `cost = [4,3,2,5,6,7,2,5,5], target = 9`
- Output: `"7772"`

**Example 2**

- Input: `cost = [7,6,5,5,5,6,8,7,8], target = 12`
- Output: `"85"`

**Example 3**

- Input: `cost = [2,4,6,2,4,6,4,4,4], target = 5`
- Output: `"0"`

---

## Underlying Base Algorithm(s)
Unbounded knapsack DP. Maximize digit count for each cost, then greedily reconstruct from digit `9` down to `1` while preserving the optimal length.

---

## Complexity Analysis
- **Time Complexity**: `O(9 * target)`
- **Space Complexity**: `O(target)`
