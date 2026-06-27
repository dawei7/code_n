# Maximum Points After Enemy Battles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3207 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [maximum-points-after-enemy-battles](https://leetcode.com/problems/maximum-points-after-enemy-battles/) |

## Problem Description & Examples
### Goal
Given a list of enemy energy values and an initial amount of energy, you aim to maximize your total points. You can defeat an enemy if your current energy is greater than or equal to their energy value, gaining 1 point per victory. Alternatively, if you have at least 1 point, you can spend it to gain energy equal to the defeated enemy's value. The goal is to determine the maximum points achievable by strategically choosing when to battle and when to convert points into energy.

### Function Contract
**Inputs**

- `enemyEnergies`: A list of integers representing the energy cost to defeat each enemy.
- `currentEnergy`: An integer representing your starting energy.

**Return value**

- An integer representing the maximum total points you can accumulate.

### Examples
**Example 1**

- Input: `enemyEnergies = [3, 2, 2]`, `currentEnergy = 2`
- Output: `3`

**Example 2**

- Input: `enemyEnergies = [2]`, `currentEnergy = 10`
- Output: `5`

**Example 3**

- Input: `enemyEnergies = [1]`, `currentEnergy = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy**. Since we want to maximize points, we should always defeat the weakest enemies first to gain points. Once we have at least one point, we can convert our points into energy using the strongest enemy's value to maximize our energy pool, allowing us to defeat the remaining enemies. The optimal approach is to defeat all enemies with energy less than or equal to our current energy, then use the minimum energy enemy to "farm" points by repeatedly converting points to energy and back to points using the largest available enemy value.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of enemies. We iterate through the list to find the minimum and calculate the sum.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the sum, minimum, and current points.
