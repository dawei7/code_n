# Watering Plants

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2079 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [watering-plants](https://leetcode.com/problems/watering-plants/) |

## Problem Description & Examples
### Goal
Walk from the river to plants in order, watering each plant. If the can does not have enough water for the next plant, return to the river to refill before continuing.

### Function Contract
**Inputs**

- `plants`: water needed by each plant.
- `capacity`: watering can capacity.

**Return value**

Return the total number of steps walked.

### Examples
**Example 1**

- Input: `plants = [2,2,3,3], capacity = 5`
- Output: `14`

**Example 2**

- Input: `plants = [1,1,1,4,2,3], capacity = 4`
- Output: `30`

**Example 3**

- Input: `plants = [7,7,7,7,7,7,7], capacity = 8`
- Output: `49`

---

## Underlying Base Algorithm(s)
Simulate the walk. Moving from plant `i - 1` to plant `i` costs one step. If current water is insufficient before watering plant `i`, add `2 * i` steps to return to the river and come back, then refill.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
