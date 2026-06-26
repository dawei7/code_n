# Divide Players Into Teams of Equal Skill

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2491 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Official Link | [divide-players-into-teams-of-equal-skill](https://leetcode.com/problems/divide-ports-into-teams-of-equal-skill/) |

## Problem Description & Examples
### Goal
Given an array of player skill levels, partition the players into teams of exactly two people such that every team has the same total skill sum. If such a partition is possible, return the sum of the products of the skill levels of each team (the "chemistry"). If it is impossible to form teams with equal skill sums, return -1.

### Function Contract
**Inputs**

- `skill`: A list of integers representing the skill level of each player. The length of the array is guaranteed to be even.

**Return value**

- An integer representing the total chemistry of the teams, or -1 if a valid partition cannot be formed.

### Examples
**Example 1**

- Input: `skill = [3,2,5,1,3,4]`
- Output: `22`
- Explanation: Teams are (1,5), (2,4), (3,3). Each sum is 6. Chemistry = (1*5) + (2*4) + (3*3) = 5 + 8 + 9 = 22.

**Example 2**

- Input: `skill = [3,4]`
- Output: `12`
- Explanation: Only one team (3,4). Sum is 7. Chemistry = 3*4 = 12.

**Example 3**

- Input: `skill = [1,1,2,3]`
- Output: `-1`
- Explanation: No way to pair players to get equal sums.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sorting + Two Pointers** approach. By sorting the skill levels, we can pair the smallest skill with the largest skill to maintain a constant sum across all pairs. If the sum of any pair deviates from the target sum (the sum of the first and last elements), the partition is invalid.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where N is the number of players. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements (Python's Timsort is `O(N)`).
