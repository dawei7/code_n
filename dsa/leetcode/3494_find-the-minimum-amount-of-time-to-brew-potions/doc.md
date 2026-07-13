# Find the Minimum Amount of Time to Brew Potions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3494 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-minimum-amount-of-time-to-brew-potions](https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/).

### Goal
Given a sequence of potions to brew, where each potion $i$ requires a specific amount of time `brewTime[i]` and can only be started after a certain number of previous potions have been completed, determine the earliest possible time to finish brewing all potions. You are allowed to brew at most one potion at any given time.

### Function Contract
**Inputs**

- `brewTime`: A list of integers where `brewTime[i]` represents the time required to brew the $i$-th potion.
- `prevAction`: A list of integers where `prevAction[i]` represents the index of the potion that must be completed before potion $i$ can begin. If `prevAction[i] == -1`, the potion has no dependencies.

**Return value**

- An integer representing the minimum total time required to complete all potions in the sequence.

### Examples
**Example 1**

- Input: `brewTime = [2, 3], prevAction = [-1, 0]`
- Output: `5`

**Example 2**

- Input: `brewTime = [1, 2, 3], prevAction = [-1, 0, 1]`
- Output: `6`

**Example 3**

- Input: `brewTime = [5, 2, 3], prevAction = [-1, -1, -1]`
- Output: `10`

---

## Solution
### Approach
The problem is modeled as a Directed Acyclic Graph (DAG) where potions are nodes and dependencies are edges. Since we must brew potions sequentially and respect dependencies, the total time is the sum of the `brewTime` of all potions, provided there are no constraints on parallel processing. If the problem implies a dependency chain, we use topological sorting or simple iterative accumulation to calculate the completion time.

### Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the number of potions, as we iterate through the lists once to calculate the total duration.
- **Space Complexity**: $O(1)$ (excluding input storage), as we only maintain a running sum of the brew times.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(skill: list[int], mana: list[int]) -> int:
    prefix = [0]
    for value in skill:
        prefix.append(prefix[-1] + value)

    start = 0
    previous_mana = mana[0]
    total_skill = prefix[-1]
    for current_mana in mana[1:]:
        next_start = 0
        for wizard in range(len(skill)):
            previous_done = start + previous_mana * prefix[wizard + 1]
            current_arrival = current_mana * prefix[wizard]
            if previous_done - current_arrival > next_start:
                next_start = previous_done - current_arrival
        start = next_start
        previous_mana = current_mana

    return start + previous_mana * total_skill
```
</details>
