# Maximum Matching of Players With Trainers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2410 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [maximum-matching-of-players-with-trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/) |

## Problem Description & Examples
### Goal
Given two lists representing the skill levels of players and the capacity levels of trainers, determine the maximum number of pairs that can be formed such that each player is assigned to at most one trainer, and each trainer is assigned to at most one player. A player can be matched with a trainer only if the trainer's capacity is greater than or equal to the player's skill level.

### Function Contract
**Inputs**

- `players`: A list of integers where each element represents a player's skill level.
- `trainers`: A list of integers where each element represents a trainer's capacity.

**Return value**

- An integer representing the maximum number of valid player-trainer matches possible.

### Examples
**Example 1**

- Input: `players = [4,7,9]`, `trainers = [8,2,5,8]`
- Output: `2`

**Example 2**

- Input: `players = [1,1,1]`, `trainers = [10]`
- Output: `1`

**Example 3**

- Input: `players = [2,2,3]`, `trainers = [1,1,1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach** combined with **Sorting** and **Two Pointers**. By sorting both arrays, we can iterate through the players and trainers linearly. For each player, we attempt to match them with the smallest available trainer who meets their skill requirement. This ensures we "save" larger capacity trainers for potentially more skilled players later in the sequence.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + M log M)`, where `N` is the number of players and `M` is the number of trainers, due to the sorting step. The subsequent two-pointer traversal takes `O(N + M)`.
- **Space Complexity**: `O(1)` or `O(N + M)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(N)` space).
