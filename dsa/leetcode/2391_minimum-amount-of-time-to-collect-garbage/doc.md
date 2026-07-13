# Minimum Amount of Time to Collect Garbage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2391 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-amount-of-time-to-collect-garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/).

### Goal
Calculate the total time required for three distinct garbage trucks (Metal, Paper, and Glass) to collect all garbage units distributed across a series of houses. Each truck takes 1 minute to pick up a unit of its specific type and a variable amount of time to travel between houses based on the provided travel distances. Each truck only travels as far as the last house containing its specific type of garbage.

### Function Contract
**Inputs**

- `garbage`: A list of strings where each string represents the garbage units at a specific house (e.g., "MP" means one Metal and one Paper unit).
- `travel`: A list of integers where `travel[i]` represents the time taken to travel from house `i` to house `i + 1`.

**Return value**

- An integer representing the total time (pickup time + travel time) spent by all three trucks.

### Examples
**Example 1**

- Input: `garbage = ["G","P","GP","GG"], travel = [2,4,3]`
- Output: `21`

**Example 2**

- Input: `garbage = ["MMM","PGM","GP"], travel = [3,10]`
- Output: `37`

---

## Solution
### Approach
The problem is solved using a linear scan combined with prefix sums. We track the total count of each garbage type (pickup time) and identify the index of the last house containing each type (travel time). The travel time for a specific truck is the sum of the `travel` array up to the index of the last house containing that truck's garbage.

### Complexity Analysis
- **Time Complexity**: `O(N + M)`, where `N` is the number of houses and `M` is the total number of garbage units across all houses, as we iterate through the houses and the characters within them.
- **Space Complexity**: `O(1)`, as we only store a constant number of variables to track counts and last indices, regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(garbage: List[str], travel: List[int]) -> int:
    # Total time = (sum of all garbage units) + (sum of travel times)
    # Each truck only travels up to the last house containing its specific type.

    total_pickup_time = 0
    last_house_indices = {'M': 0, 'P': 0, 'G': 0}

    # Calculate total pickup time and find the last house for each type
    for i, house in enumerate(garbage):
        total_pickup_time += len(house)
        for char in house:
            last_house_indices[char] = i

    # Calculate prefix sums for travel times to quickly get travel duration
    # travel_prefix[i] is the time to reach house i from house 0
    travel_prefix = [0] * len(garbage)
    for i in range(len(travel)):
        travel_prefix[i + 1] = travel_prefix[i] + travel[i]

    total_travel_time = 0
    for char in ['M', 'P', 'G']:
        last_idx = last_house_indices[char]
        total_travel_time += travel_prefix[last_idx]

    return total_pickup_time + total_travel_time
```
</details>
