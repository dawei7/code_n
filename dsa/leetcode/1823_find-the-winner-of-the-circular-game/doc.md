# Find the Winner of the Circular Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1823 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Recursion, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-winner-of-the-circular-game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-winner-of-the-circular-game/).

### Goal
Players numbered `1` through `n` stand in a circle. Starting at player `1`, count `k` players and remove that player, then continue from the next player. Find the final remaining player.

### Function Contract
**Inputs**

- `n`: the number of players.
- `k`: the counting step.

**Return value**

Return the winning player's 1-based label.

### Examples
**Example 1**

- Input: `n = 5, k = 2`
- Output: `3`

**Example 2**

- Input: `n = 6, k = 5`
- Output: `1`

**Example 3**

- Input: `n = 1, k = 3`
- Output: `1`

---

## Solution
### Approach
This is the Josephus problem. Either simulate with a queue, rotating `k - 1` players before removing one, or use the recurrence `winner(size) = (winner(size - 1) + k) % size` in zero-based indexing and convert back to one-based at the end.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` with the recurrence, `O(n)` with queue simulation

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
