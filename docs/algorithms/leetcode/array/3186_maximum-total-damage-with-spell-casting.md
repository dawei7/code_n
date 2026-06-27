# Maximum Total Damage With Spell Casting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3186 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Dynamic Programming, Sorting, Counting |
| Official Link | [maximum-total-damage-with-spell-casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/) |

## Problem Description & Examples
### Goal
Given a list of power values representing available spells, you must select a subset of these spells to maximize the total damage. The constraint is that if you choose a spell with power `x`, you cannot choose any other spells with power `x-1`, `x-2`, `x+1`, or `x+2`. You may use each instance of a spell power as many times as it appears in the input list.

### Function Contract
**Inputs**

- `power`: A list of integers representing the power levels of available spells.

**Return value**

- An integer representing the maximum total damage achievable under the given constraints.

### Examples
**Example 1**

- Input: `power = [1, 1, 3, 4]`
- Output: `6`
- Explanation: We can pick both spells of power 1 (total 2) and one spell of power 4 (total 4). Total = 6.

**Example 2**

- Input: `power = [7, 1, 6, 6]`
- Output: `13`
- Explanation: We can pick both spells of power 6 (total 12) and one spell of power 1 (total 1). Total = 13.

**Example 3**

- Input: `power = [5, 9, 5, 10, 5]`
- Output: `15`
- Explanation: We can pick all three spells of power 5. Total = 15.

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming combined with Frequency Counting and Binary Search. By grouping identical power levels, we transform the problem into a variation of the "House Robber" problem, where we decide whether to include a specific power level (and all its instances) or skip it based on the constraints of neighboring power levels.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of spells. This accounts for sorting the unique power levels and performing binary search for each unique power level.
- **Space Complexity**: `O(N)` to store the frequency map and the DP array.
