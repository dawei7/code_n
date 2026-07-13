# Watering Plants II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2105 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [watering-plants-ii](https://leetcode.com/problems/watering-plants-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/watering-plants-ii/).

### Goal
Two people water plants from opposite ends toward the center with separate cans. Count how many times they must refill before watering their next plant.

### Function Contract
**Inputs**

- `plants`: water required by each plant.
- `capacityA`, `capacityB`: initial capacities for the left and right gardener.

**Return value**

Return the total number of refills.

### Examples
**Example 1**

- Input: `plants = [2,2,3,3], capacityA = 5, capacityB = 5`
- Output: `1`

**Example 2**

- Input: `plants = [2,2,3,3], capacityA = 3, capacityB = 4`
- Output: `2`

**Example 3**

- Input: `plants = [5], capacityA = 10, capacityB = 8`
- Output: `0`

---

## Solution
### Approach
Use two pointers and track remaining water for both gardeners. Refill when the next assigned plant exceeds the corresponding remaining amount. If one middle plant remains, the gardener with more water handles it, with one refill if neither has enough.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
