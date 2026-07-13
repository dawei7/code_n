# Longest Well-Performing Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1124 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-well-performing-interval](https://leetcode.com/problems/longest-well-performing-interval/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-well-performing-interval/).

### Goal
Given daily work hours, find the longest contiguous interval where the number of tiring days is greater than the number of non-tiring days. A tiring day has more than `8` hours.

### Function Contract
**Inputs**

- `hours`: list of daily hour counts.

**Return value**

The maximum length of a well-performing interval.

### Examples
**Example 1**

- Input: `hours = [9,9,6,0,6,6,9]`
- Output: `3`

**Example 2**

- Input: `hours = [6,6,6]`
- Output: `0`

**Example 3**

- Input: `hours = [9,6,9,6,9]`
- Output: `5`

---

## Solution
### Approach
Prefix sum with earliest-index lookup.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1124: Longest Well-Performing Interval."""


def solve(hours: list[int]) -> int:
    score = 0
    first_seen: dict[int, int] = {}
    best = 0
    for i, hour in enumerate(hours):
        score += 1 if hour > 8 else -1
        if score > 0:
            best = i + 1
        else:
            first_seen.setdefault(score, i)
            if score - 1 in first_seen:
                best = max(best, i - first_seen[score - 1])
    return best
```
</details>
