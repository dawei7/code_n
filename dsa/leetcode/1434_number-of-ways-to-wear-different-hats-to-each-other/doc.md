# Number of Ways to Wear Different Hats to Each Other

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1434 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-to-wear-different-hats-to-each-other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/).

### Goal
Count how many ways to assign hats so every person gets exactly one hat they like and no two people wear the same hat.

### Function Contract
**Inputs**

- `hats`: `hats[i]` lists the hat numbers liked by person `i`.

**Return value**

The number of valid assignments modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `hats = [[3,4],[4,5],[5]]`
- Output: `1`

**Example 2**

- Input: `hats = [[3,5,1],[3,5]]`
- Output: `4`

**Example 3**

- Input: `hats = [[1,2,3],[2,3,5],[1,3,5]]`
- Output: `8`

---

## Solution
### Approach
Bitmask dynamic programming over hats. Process hat numbers and update masks of people already assigned; for each hat, either skip it or assign it to one compatible unassigned person.

### Complexity Analysis
- **Time Complexity**: `O(H * 2^p * p)`, where `H` is the number of possible hats and `p` is the number of people.
- **Space Complexity**: `O(2^p)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(hats):
    mod = 1_000_000_007
    people = len(hats)
    if people == 0:
        return 1
    by_hat = defaultdict(list)
    for person, choices in enumerate(hats):
        if not isinstance(choices, list):
            choices = [choices]
        for hat in choices:
            by_hat[int(hat)].append(person)
    if people > len(by_hat):
        return 0
    dp = {0: 1}
    full = (1 << people) - 1
    for hat in sorted(by_hat):
        next_dp = dict(dp)
        for mask, count in dp.items():
            for person in by_hat[hat]:
                bit = 1 << person
                if not mask & bit:
                    next_dp[mask | bit] = (next_dp.get(mask | bit, 0) + count) % mod
        dp = next_dp
    return dp.get(full, 0)
```
</details>
