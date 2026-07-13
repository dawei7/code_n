# Maximum Total Damage With Spell Casting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Dynamic Programming, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-total-damage-with-spell-casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/).

### Goal
Given a list of power values representing available spells, you must select a subset of these spells to maximize the total damage. The constraint is that if you choose a spell with power `x`, you cannot choose any other spells with power `x-1`, `x-2`, `x+1`, or `x+2`. You may use each instance of a spell power as many times as it appears in the input list.

### Function Contract
**Inputs**

- `power`: A list of integers representing the power levels of available spells.

**Return value**

- An integer representing the maximum total damage achievable under the given constraints.

### Examples
**Example 1**

- Input: `power = [1, 1, 3, 4]`
- Output: `6`
- Explanation: We can pick both spells of power 1 (total 2) and one spell of power 4 (total 4). Total = 6.

**Example 2**

- Input: `power = [7, 1, 6, 6]`
- Output: `13`
- Explanation: We can pick both spells of power 6 (total 12) and one spell of power 1 (total 1). Total = 13.

**Example 3**

- Input: `power = [5, 9, 5, 10, 5]`
- Output: `15`
- Explanation: We can pick all three spells of power 5. Total = 15.

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with Frequency Counting and Binary Search. By grouping identical power levels, we transform the problem into a variation of the "House Robber" problem, where we decide whether to include a specific power level (and all its instances) or skip it based on the constraints of neighboring power levels.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of spells. This accounts for sorting the unique power levels and performing binary search for each unique power level.
- **Space Complexity**: `O(N)` to store the frequency map and the DP array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter
import bisect

def solve(power: list[int]) -> int:
    # Count occurrences of each spell power
    counts = Counter(power)
    # Sort unique power levels to process them in order
    unique_powers = sorted(counts.keys())
    n = len(unique_powers)

    # dp[i] will store the maximum damage using a subset of the first i unique powers
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current_power = unique_powers[i - 1]
        current_damage = current_power * counts[current_power]

        # Find the index of the largest power level that is < current_power - 2
        # This is the last index we can safely include without violating constraints
        idx = bisect.bisect_right(unique_powers, current_power - 3)

        # Option 1: Include current power level
        # We add current_damage to the max damage found up to the valid index
        include = current_damage + dp[idx]

        # Option 2: Exclude current power level
        # We take the max damage found up to the previous power level
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    return dp[n]
```
</details>
