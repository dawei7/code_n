# Minimum Number of Taps to Open to Water a Garden

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1326 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [minimum-number-of-taps-to-open-to-water-a-garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) |

## Problem Description & Examples
### Goal
A garden spans positions `0` through `n`. Tap `i` waters an interval centered at `i` with radius `ranges[i]`. Open the fewest taps needed to cover the whole garden.

### Function Contract
**Inputs**

- `n`: garden endpoint.
- `ranges`: watering radius for each tap index from `0` to `n`.

**Return value**

The minimum number of taps to open, or `-1` if full coverage is impossible.

### Examples
**Example 1**

- Input: `n = 5`, `ranges = [3,4,1,1,0,0]`
- Output: `1`

**Example 2**

- Input: `n = 3`, `ranges = [0,0,0,0]`
- Output: `-1`

**Example 3**

- Input: `n = 7`, `ranges = [1,2,1,0,2,1,0,1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Greedy interval covering, same shape as Jump Game II.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
