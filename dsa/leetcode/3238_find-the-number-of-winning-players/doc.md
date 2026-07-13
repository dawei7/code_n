# Find the Number of Winning Players

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3238 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-winning-players](https://leetcode.com/problems/find-the-number-of-winning-players/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-winning-players/).

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

## Solution
### Approach
The problem is solved using a Frequency Map (or Hash Table) approach. We maintain a nested data structure (an array of dictionaries) where the outer index represents the player ID and the inner dictionary maps color IDs to their respective counts. By iterating through the `pick` list once, we populate these counts and then perform a single pass over the players to check if any color count exceeds the player's index.

### Complexity Analysis
- **Time Complexity**: `O(P + N)`, where `P` is the number of picks and `N` is the number of players. We iterate through the picks once to build the frequency map and then iterate through the players to verify the winning condition.
- **Space Complexity**: `O(P)`, as in the worst case, we store every pick in the frequency map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(n: int, pick: list[list[int]]) -> int:
    # counts[player_id][color] = frequency
    counts = [defaultdict(int) for _ in range(n)]

    for player, color in pick:
        counts[player][color] += 1

    winning_players = 0
    for i in range(n):
        # A player i wins if they have picked more than i balls of any color
        for color in counts[i]:
            if counts[i][color] > i:
                winning_players += 1
                break

    return winning_players
```
</details>
