# Minimum Time to Make Rope Colorful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1578 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-make-rope-colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/).

### Goal
Remove balloons so no two adjacent balloons have the same color, minimizing the
total removal time.

### Function Contract
**Inputs**

- `colors`: a string of balloon colors.
- `neededTime`: removal time for each corresponding balloon.

**Return value**

The minimum total time needed to make adjacent colors different.

### Examples
**Example 1**

- Input: `colors = "abaac", neededTime = [1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input: `colors = "abc", neededTime = [1, 2, 3]`
- Output: `0`

**Example 3**

- Input: `colors = "aabaa", neededTime = [1, 2, 3, 4, 1]`
- Output: `2`

---

## Solution
### Approach
Process each maximal group of equal adjacent colors. Within a group, all but one
balloon must be removed, so pay the group's total time minus its largest single
removal time.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(colors, needed_time):
    if not colors:
        return 0
    times = list(needed_time) + [0] * max(0, len(colors) - len(needed_time))
    total = 0
    group_sum = times[0]
    group_max = times[0]
    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]:
            group_sum += times[i]
            group_max = max(group_max, times[i])
        else:
            total += group_sum - group_max
            group_sum = times[i]
            group_max = times[i]
    total += group_sum - group_max
    return total
```
</details>
