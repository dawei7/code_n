# Minimum Amount of Damage Dealt to Bob

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3273 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-amount-of-damage-dealt-to-bob](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/) |

## Problem Description & Examples
### Goal
You are tasked with defeating a series of enemies, each having a specific amount of health and dealing a constant amount of damage per second. You can only attack one enemy at a time. Your goal is to determine the optimal order to defeat these enemies such that the total damage Bob receives from all enemies until they are all defeated is minimized.

### Function Contract
**Inputs**

- `damage`: A list of integers where `damage[i]` represents the damage per second dealt by the $i$-th enemy.
- `health`: A list of integers where `health[i]` represents the total health of the $i$-th enemy.

**Return value**

- An integer representing the minimum total damage Bob sustains.

### Examples
**Example 1**

- Input: `damage = [1, 2, 3, 4]`, `health = [4, 5, 6, 8]`
- Output: `39`

**Example 2**

- Input: `damage = [1]`, `health = [1]`
- Output: `1`

**Example 3**

- Input: `damage = [5, 1, 6, 4, 2]`, `health = [2, 3, 5, 6, 3]`
- Output: `28`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy**. To minimize damage, we must prioritize enemies based on the ratio of their damage output to their health. Specifically, we sort enemies by the ratio `damage[i] / health[i]` in descending order. Since we must deal damage in discrete units (assuming 1 damage per second), we calculate the time to kill an enemy as `ceil(health[i] / power)`. By sorting based on the ratio, we ensure that we eliminate the most "dangerous" enemies relative to the time it takes to kill them as quickly as possible.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of enemies, due to the sorting step.
- **Space Complexity**: $O(N)$ to store the enemy objects or tuples for sorting.
