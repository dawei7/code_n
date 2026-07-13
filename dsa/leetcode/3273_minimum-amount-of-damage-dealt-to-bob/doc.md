# Minimum Amount of Damage Dealt to Bob

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3273 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-amount-of-damage-dealt-to-bob](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/).

### Goal
You are tasked with defeating a series of enemies, each having a specific amount of health and dealing a constant amount of damage per second. You can only attack one enemy at a time. Your goal is to determine the optimal order to defeat these enemies such that the total damage Bob receives from all enemies until they are all defeated is minimized.

### Function Contract
**Inputs**

- `damage`: A list of integers where `damage[i]` represents the damage per second dealt by the $i$-th enemy.
- `health`: A list of integers where `health[i]` represents the total health of the $i$-th enemy.

**Return value**

- An integer representing the minimum total damage Bob sustains.

### Examples
**Example 1**

- Input: `damage = [1, 2, 3, 4]`, `health = [4, 5, 6, 8]`
- Output: `39`

**Example 2**

- Input: `damage = [1]`, `health = [1]`
- Output: `1`

**Example 3**

- Input: `damage = [5, 1, 6, 4, 2]`, `health = [2, 3, 5, 6, 3]`
- Output: `28`

---

## Solution
### Approach
The problem is solved using a **Greedy Strategy**. To minimize damage, we must prioritize enemies based on the ratio of their damage output to their health. Specifically, we sort enemies by the ratio `damage[i] / health[i]` in descending order. Since we must deal damage in discrete units (assuming 1 damage per second), we calculate the time to kill an enemy as `ceil(health[i] / power)`. By sorting based on the ratio, we ensure that we eliminate the most "dangerous" enemies relative to the time it takes to kill them as quickly as possible.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of enemies, due to the sorting step.
- **Space Complexity**: $O(N)$ to store the enemy objects or tuples for sorting.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(damage: list[int], health: list[int], power: int) -> int:
    """
    Calculates the minimum damage Bob receives by greedily defeating enemies.

    The strategy is to sort enemies by the ratio of (damage / time_to_kill).
    Since time_to_kill = ceil(health / power), we compare enemies i and j
    by checking if damage[i] * time_to_kill[j] > damage[j] * time_to_kill[i].
    """
    n = len(damage)
    enemies = []
    for i in range(n):
        time_to_kill = (health[i] + power - 1) // power
        enemies.append((damage[i], time_to_kill))

    # Sort by damage/time ratio descending.
    # To avoid floating point issues, use cross-multiplication:
    # d1/t1 > d2/t2  <=>  d1 * t2 > d2 * t1
    from functools import cmp_to_key

    def compare(a, b):
        # a = (d1, t1), b = (d2, t2)
        val1 = a[0] * b[1]
        val2 = b[0] * a[1]
        if val1 > val2:
            return -1
        elif val1 < val2:
            return 1
        return 0

    enemies.sort(key=cmp_to_key(compare))

    total_damage = 0
    current_time = 0
    total_dps = sum(damage)

    for d, t in enemies:
        current_time += t
        total_damage += current_time * d

    return total_damage
```
</details>
