# Dice Roll Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1223 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [dice-roll-simulation](https://leetcode.com/problems/dice-roll-simulation/) |

## Problem Description & Examples
### Goal
Count length-`n` dice roll sequences where face `i` is not rolled more than `rollMax[i]` times consecutively.

### Function Contract
**Inputs**

- `n`: sequence length.
- `rollMax`: six limits for consecutive occurrences of faces `1` through `6`.

**Return value**

The number of valid sequences modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `n = 2`, `rollMax = [1,1,2,2,2,3]`
- Output: `34`

**Example 2**

- Input: `n = 2`, `rollMax = [1,1,1,1,1,1]`
- Output: `30`

**Example 3**

- Input: `n = 3`, `rollMax = [1,1,1,2,2,3]`
- Output: `181`

---

## Underlying Base Algorithm(s)
Dynamic programming over last face and run length.

---

## Complexity Analysis
- **Time Complexity**: `O(n * 6 * max(rollMax) * 6)`
- **Space Complexity**: `O(6 * max(rollMax))`
