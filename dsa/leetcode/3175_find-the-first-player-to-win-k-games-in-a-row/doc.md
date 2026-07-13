# Find The First Player to win K Games in a Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3175 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-first-player-to-win-k-games-in-a-row](https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/).

### Goal
Determine the index of the first player who achieves $k$ consecutive wins in a competitive queue. In each round, the first two players in the queue compete; the one with the higher skill value wins, stays at the front, and the loser moves to the back of the queue. If $k$ is very large, the player with the maximum skill value will eventually win indefinitely.

### Function Contract
**Inputs**

- `skills`: A list of integers representing the skill levels of players in their initial queue order.
- `k`: An integer representing the number of consecutive wins required to be declared the winner.

**Return value**

- An integer representing the index of the player who first achieves $k$ consecutive wins.

### Examples
**Example 1**

- Input: `skills = [4, 2, 6, 3, 9], k = 2`
- Output: `2`

**Example 2**

- Input: `skills = [2, 5, 4], k = 3`
- Output: `1`

**Example 3**

- Input: `skills = [16, 4, 7, 17], k = 562624757`
- Output: `3`

---

## Solution
### Approach
The problem can be solved using a linear scan (simulation). We maintain the current "winner" and their current streak count. As we iterate through the array, we compare the current winner's skill with the next player. If the current winner is stronger, their streak increments. If the challenger is stronger, the challenger becomes the new winner with a streak of 1. If any player's streak reaches $k$, or if we encounter the player with the maximum skill value (who will win all subsequent games), we return the result.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the number of players, as we iterate through the list at most once.
- **Space Complexity**: $O(1)$, as we only store a few variables to track the current winner, their index, and their streak.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(skills: list[int], k: int) -> int:
    n = len(skills)
    # If k is large, the player with the maximum skill will eventually win.
    # We only need to simulate until we find a winner or reach the max skill.

    current_winner_idx = 0
    current_streak = 0

    for i in range(1, n):
        # Compare current winner with the next player
        if skills[current_winner_idx] > skills[i]:
            current_streak += 1
        else:
            current_winner_idx = i
            current_streak = 1

        # Check if the current winner has reached k wins
        if current_streak >= k:
            return current_winner_idx

    # If we finish the loop, the current_winner_idx is the player with the
    # maximum skill, who will win all subsequent games.
    return current_winner_idx
```
</details>
