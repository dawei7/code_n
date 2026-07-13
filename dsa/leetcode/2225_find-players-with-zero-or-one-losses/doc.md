# Find Players With Zero or One Losses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2225 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-players-with-zero-or-one-losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-players-with-zero-or-one-losses/).

### Goal
From match results, list all participating players who never lost and all participating players who lost exactly once. Sort both lists increasingly.

### Function Contract
**Inputs**

- `matches`: pairs `[winner, loser]`.

**Return value**

`[zero_loss_players, one_loss_players]`, with each inner list sorted.

### Examples
**Example 1**

- Input: `matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]`
- Output: `[[1, 2, 10], [4, 5, 7, 8]]`

**Example 2**

- Input: `matches = [[2, 3], [1, 3], [5, 4], [6, 4]]`
- Output: `[[1, 2, 5, 6], []]`

**Example 3**

- Input: `matches = [[1, 2]]`
- Output: `[[1], [2]]`

---

## Solution
### Approach
Record every participant and count losses for each loser. Players absent from the loss map have zero losses; players with loss count one form the second group. Sort both selected groups before returning them.

### Complexity Analysis
- **Time Complexity**: `O(m + p log p)`, where `p` is the number of distinct players
- **Space Complexity**: `O(p)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
