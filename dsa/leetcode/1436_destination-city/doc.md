# Destination City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1436 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [destination-city](https://leetcode.com/problems/destination-city/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/destination-city/).

### Goal
Given directed travel paths, find the city that never appears as a starting city. The path chain has exactly one such destination.

### Function Contract
**Inputs**

- `paths`: a list of `[fromCity, toCity]` directed paths.

**Return value**

The final destination city name.

### Examples
**Example 1**

- Input: `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`
- Output: `"Sao Paulo"`

**Example 2**

- Input: `paths = [["B","C"],["D","B"],["C","A"]]`
- Output: `"A"`

**Example 3**

- Input: `paths = [["A","Z"]]`
- Output: `"Z"`

---

## Solution
### Approach
Set difference. Collect all starting cities, then return the destination city that is not in that set.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(paths):
    starts = {path[0] for path in paths if len(path) >= 2}
    for path in paths:
        if len(path) >= 2 and path[1] not in starts:
            return path[1]
    return ""
```
</details>
