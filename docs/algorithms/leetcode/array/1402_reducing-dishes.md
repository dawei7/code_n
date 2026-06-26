# Reducing Dishes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1402 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Official Link | [reducing-dishes](https://leetcode.com/problems/reducing-dishes/) |

## Problem Description & Examples
### Goal
Choose and order some dishes to maximize the total like-time coefficient, where the first cooked chosen dish is multiplied by `1`, the next by `2`, and so on.

### Function Contract
**Inputs**

- `satisfaction`: a list of integer satisfaction values.

**Return value**

The maximum possible total like-time coefficient.

### Examples
**Example 1**

- Input: `satisfaction = [-1,-8,0,5,-9]`
- Output: `14`

**Example 2**

- Input: `satisfaction = [4,3,2]`
- Output: `20`

**Example 3**

- Input: `satisfaction = [-1,-4,-5]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Greedy sorting from high to low. Sort satisfaction values and prepend dishes while the running sum remains positive; adding a dish to the front increases all previously chosen dishes by its value contribution.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` extra if sorting in place.
