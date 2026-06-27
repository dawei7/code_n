# Find the Number of Winning Players

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3238 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [find-the-number-of-winning-players](https://leetcode.com/problems/find-the-number-of-winning-players/) |

## Problem Description & Examples
### Goal
Given a total number of players `n` and a list of `pick` events where each event `[player_i, color_i]` indicates that player `i` picked a ball of color `color_i`, determine how many players are "winning." A player `i` is considered a winner if they have picked more than `i` balls of the same color.

### Function Contract
**Inputs**

- `n` (int): The total number of players, indexed from 0 to n-1.
- `pick` (List[List[int]]): A list of pairs where each pair `[x, y]` represents player `x` picking a ball of color `y`.

**Return value**

- `int`: The total count of players who satisfy the winning condition.

### Examples
**Example 1**

- Input: `n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,1]]`
- Output: `2`
- Explanation: Player 0 needs > 0 balls of one color (picked 1 color 0, wins). Player 1 needs > 1 balls of one color (picked 2 color 0, wins). Player 2 needs > 2 balls of one color (picked 3 color 1, wins). Wait, player 0, 1, and 2 win.

**Example 2**

- Input: `n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]`
- Output: `0`

**Example 3**

- Input: `n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a Frequency Map (or Hash Table) approach. We maintain a nested data structure (an array of dictionaries) where the outer index represents the player ID and the inner dictionary maps color IDs to their respective counts. By iterating through the `pick` list once, we populate these counts and then perform a single pass over the players to check if any color count exceeds the player's index.

---

## Complexity Analysis
- **Time Complexity**: `O(P + N)`, where `P` is the number of picks and `N` is the number of players. We iterate through the picks once to build the frequency map and then iterate through the players to verify the winning condition.
- **Space Complexity**: `O(P)`, as in the worst case, we store every pick in the frequency map.
