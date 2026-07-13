# Maximum Energy Boost From Two Drinks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3259 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-energy-boost-from-two-drinks](https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/).

### Goal
Given two arrays representing energy boosts from two different drinks over a series of hours, determine the maximum total energy you can accumulate. You can consume one drink per hour, but switching drinks requires skipping the current hour (i.e., you cannot consume a drink in the hour immediately following a switch).

### Function Contract
**Inputs**

- `energyA`: A list of integers representing energy gains from drink A at each hour.
- `energyB`: A list of integers representing energy gains from drink B at each hour.

**Return value**

- An integer representing the maximum total energy boost achievable.

### Examples
**Example 1**

- Input: `energyA = [1, 3, 1], energyB = [3, 1, 1]`
- Output: `5`

**Example 2**

- Input: `energyA = [4, 1, 1], energyB = [1, 1, 3]`
- Output: `7`

---

## Solution
### Approach
Dynamic Programming. We maintain two state arrays (or variables) representing the maximum energy accumulated up to hour `i` ending with drink A or drink B. The transition depends on whether we continue the same drink (from `i-1`) or switch (from `i-2`).

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of hours, as we iterate through the arrays once.
- **Space Complexity**: `O(1)` if we optimize the DP state to only track the last two hours, or `O(n)` if using full DP tables.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(energyA: List[int], energyB: List[int]) -> int:
    n = len(energyA)
    if n == 1:
        return max(energyA[0], energyB[0])

    # dpA[i] is the max energy ending at hour i with drink A
    # dpB[i] is the max energy ending at hour i with drink B
    # To save space, we only need the previous two states.

    # Base cases for hour 0
    prev_a = energyA[0]
    prev_b = energyB[0]

    # Base cases for hour 1
    curr_a = energyA[0] + energyA[1]
    curr_b = energyB[0] + energyB[1]

    # We track the last two states to handle the "skip" rule
    # dpA[i] = max(dpA[i-1] + energyA[i], dpB[i-2] + energyA[i])
    # dpB[i] = max(dpB[i-1] + energyB[i], dpA[i-2] + energyB[i])

    # state_a_minus_2, state_a_minus_1
    # state_b_minus_2, state_b_minus_1
    a_2, a_1 = energyA[0], energyA[0] + energyA[1]
    b_2, b_1 = energyB[0], energyB[0] + energyB[1]

    for i in range(2, n):
        new_a = max(a_1 + energyA[i], b_2 + energyA[i])
        new_b = max(b_1 + energyB[i], a_2 + energyB[i])

        a_2, a_1 = a_1, new_a
        b_2, b_1 = b_1, new_b

    return max(a_1, b_1)
```
</details>
