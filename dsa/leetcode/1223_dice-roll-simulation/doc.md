# Dice Roll Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1223 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [dice-roll-simulation](https://leetcode.com/problems/dice-roll-simulation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/dice-roll-simulation/).

### Goal
Count length-`n` dice roll sequences where face `i` is not rolled more than `rollMax[i]` times consecutively.

### Function Contract
**Inputs**

- `n`: sequence length.
- `rollMax`: six limits for consecutive occurrences of faces `1` through `6`.

**Return value**

The number of valid sequences modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `n = 2`, `rollMax = [1,1,2,2,2,3]`
- Output: `34`

**Example 2**

- Input: `n = 2`, `rollMax = [1,1,1,1,1,1]`
- Output: `30`

**Example 3**

- Input: `n = 3`, `rollMax = [1,1,1,2,2,3]`
- Output: `181`

---

## Solution
### Approach
Dynamic programming over last face and run length.

### Complexity Analysis
- **Time Complexity**: `O(n * 6 * max(rollMax) * 6)`
- **Space Complexity**: `O(6 * max(rollMax))`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n, roll_max):
    mod = 1_000_000_007
    dp = [[0] * (roll_max[i] + 1) for i in range(6)]
    for face in range(6):
        dp[face][1] = 1

    for _ in range(1, n):
        next_dp = [[0] * (roll_max[i] + 1) for i in range(6)]
        totals = [sum(row) % mod for row in dp]
        all_total = sum(totals) % mod
        for face in range(6):
            next_dp[face][1] = (all_total - totals[face]) % mod
            for count in range(1, roll_max[face]):
                next_dp[face][count + 1] = dp[face][count]
        dp = next_dp

    return sum(sum(row) for row in dp) % mod
```
</details>
