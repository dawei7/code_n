# Most Visited Sector in  a Circular Track

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1560 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [most-visited-sector-in-a-circular-track](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/).

### Goal
Given a sequence of race checkpoints on a circular track, return the sectors
visited the most often.

### Function Contract
**Inputs**

- `n`: the number of sectors labeled `1` through `n`.
- `rounds`: the visited checkpoint sequence.

**Return value**

The most visited sector labels in increasing order.

### Examples
**Example 1**

- Input: `n = 4, rounds = [1, 3, 1, 2]`
- Output: `[1, 2]`

**Example 2**

- Input: `n = 2, rounds = [2, 1, 2, 1, 2, 1, 2, 1, 2]`
- Output: `[2]`

**Example 3**

- Input: `n = 7, rounds = [1, 3, 5, 7]`
- Output: `[1, 2, 3, 4, 5, 6, 7]`

---

## Solution
### Approach
Only the start and final checkpoint determine which sectors receive one extra
visit after all full laps. If `start <= end`, return every sector from `start`
to `end`; otherwise return `1..end` followed by `start..n`.

### Complexity Analysis
- **Time Complexity**: `O(n)` for the output size.
- **Space Complexity**: `O(1)` extra space besides the result.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n, rounds):
    if n <= 0 or not rounds:
        return []
    start = ((rounds[0] - 1) % n) + 1
    end = ((rounds[-1] - 1) % n) + 1
    if start <= end:
        return list(range(start, end + 1))
    return list(range(1, end + 1)) + list(range(start, n + 1))
```
</details>
