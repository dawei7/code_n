# Stone Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1406 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [stone-game-iii](https://leetcode.com/problems/stone-game-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/stone-game-iii/).

### Goal
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array `stone_value`.

Alice and Bob take turns, with Alice starting first. On each turn, a player can take `1`, `2`, or `3` stones from the first remaining stones in the row.

The game ends when no more stones are left. The player with the highest score wins. The score of a player is the sum of the values of the stones taken by that player.

Return `"Alice"` if Alice wins, `"Bob"` if Bob wins, or `"Tie"` if they get the same score.

### Function Contract
**Inputs**

- `stone_value`: List[int]

**Return value**

str - 'Alice', 'Bob', or 'Tie'

### Examples
**Example 1**

- Input: `stone_value = [1, 2, 3, 7]`
- Output: `"Bob"`

**Example 2**

- Input: `stone_value = [2]`
- Output: `'Alice'`

**Example 3**

- Input: `stone_value = [-6, 8]`
- Output: `'Alice'`

---

## Solution
### Approach
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(stone_value):
    n = len(stone_value)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        take = 0
        dp[i] = float("-inf")
        for j in range(i, min(i + 3, n)):
            take += stone_value[j]
            dp[i] = max(dp[i], take - dp[j + 1])
    if dp[0] > 0:
        return "Alice"
    if dp[0] < 0:
        return "Bob"
    return "Tie"
```
</details>
