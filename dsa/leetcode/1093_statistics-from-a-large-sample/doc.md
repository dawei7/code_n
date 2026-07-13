# Statistics from a Large Sample

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1093 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [statistics-from-a-large-sample](https://leetcode.com/problems/statistics-from-a-large-sample/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/statistics-from-a-large-sample/).

### Goal
Given a frequency table for values `0` through `255`, compute the minimum, maximum, mean, median, and mode of the represented sample.

### Function Contract
**Inputs**

- `count`: length-256 array where `count[i]` is how many times value `i` appears.

**Return value**

A five-element list `[minimum, maximum, mean, median, mode]` as floating-point values where appropriate.

### Examples
**Example 1**

- Input: `count = [0,1,3,4] + [0]*252`
- Output: `[1,3,2.375,2.5,3]`

**Example 2**

- Input: `count = [2,0,0,1] + [0]*252`
- Output: `[0,3,1.0,0.0,0]`

**Example 3**

- Input: `count = [0,0,5] + [0]*253`
- Output: `[2,2,2.0,2.0,2]`

---

## Solution
### Approach
Frequency-table scanning and order statistics.

### Complexity Analysis
- **Time Complexity**: `O(256)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1093: Statistics from a Large Sample."""


def solve(count: list[int]) -> list[float]:
    total_count = sum(count)
    minimum = next(i for i, freq in enumerate(count) if freq)
    maximum = next(i for i in range(255, -1, -1) if count[i])
    mean = sum(i * freq for i, freq in enumerate(count)) / total_count
    mode = max(range(256), key=lambda i: count[i])

    def kth(k: int) -> int:
        seen = 0
        for value, freq in enumerate(count):
            seen += freq
            if seen >= k:
                return value
        return 255

    if total_count % 2:
        median = float(kth(total_count // 2 + 1))
    else:
        median = (kth(total_count // 2) + kth(total_count // 2 + 1)) / 2
    return [float(minimum), float(maximum), mean, median, float(mode)]
```
</details>
