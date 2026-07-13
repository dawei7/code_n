# Minimum Number of Taps to Open to Water a Garden

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1326 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-taps-to-open-to-water-a-garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/).

### Goal
A garden spans positions `0` through `n`. Tap `i` waters an interval centered at `i` with radius `ranges[i]`. Open the fewest taps needed to cover the whole garden.

### Function Contract
**Inputs**

- `n`: garden endpoint.
- `ranges`: watering radius for each tap index from `0` to `n`.

**Return value**

The minimum number of taps to open, or `-1` if full coverage is impossible.

### Examples
**Example 1**

- Input: `n = 5`, `ranges = [3,4,1,1,0,0]`
- Output: `1`

**Example 2**

- Input: `n = 3`, `ranges = [0,0,0,0]`
- Output: `-1`

**Example 3**

- Input: `n = 7`, `ranges = [1,2,1,0,2,1,0,1]`
- Output: `3`

---

## Solution
### Approach
Greedy interval covering, same shape as Jump Game II.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n, ranges):
    farthest = [0] * (n + 1)
    for i, radius in enumerate(ranges):
        left = max(0, i - radius)
        right = min(n, i + radius)
        farthest[left] = max(farthest[left], right)

    taps = 0
    current_end = 0
    next_end = 0
    for i in range(n):
        next_end = max(next_end, farthest[i])
        if i == current_end:
            if next_end <= i:
                return -1
            taps += 1
            current_end = next_end
    return taps
```
</details>
