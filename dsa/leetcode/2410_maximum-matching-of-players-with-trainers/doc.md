# Maximum Matching of Players With Trainers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2410 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/) |

## Problem Description

### Goal

Two 0-indexed arrays describe a group of players and a group of trainers. `players[i]` is the ability required by the $i$th player, while `trainers[j]` is the training capacity offered by the $j$th trainer. A player may be assigned to a trainer only when the player's ability is less than or equal to that trainer's capacity.

Every player can participate in at most one assignment, and every trainer can train at most one player. Choose the pairings rather than following the original array order, and return the maximum number of valid player-trainer matchings.

### Function Contract

**Inputs**

- `players`: An integer array of player abilities.
- `trainers`: An integer array of trainer capacities.

Let $n = \lvert\texttt{players}\rvert$ and $m = \lvert\texttt{trainers}\rvert$. Both lengths are between 1 and $10^5$, and every value is between 1 and $10^9$.

**Return value**

Return the largest possible number of one-to-one matches satisfying ability $\le$ capacity.

### Examples

#### Example 1

- **Input:** `players = [4,7,9]`, `trainers = [8,2,5,8]`
- **Output:** `2`

#### Example 2

- **Input:** `players = [1,1,1]`, `trainers = [10]`
- **Output:** `1`

#### Example 3

- **Input:** `players = [2,2,3]`, `trainers = [1,1,1]`
- **Output:** `0`
