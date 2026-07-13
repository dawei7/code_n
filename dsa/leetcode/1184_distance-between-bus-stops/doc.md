# Distance Between Bus Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1184 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [distance-between-bus-stops](https://leetcode.com/problems/distance-between-bus-stops/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/distance-between-bus-stops/).

### Goal
Given clockwise distances between consecutive stops on a circular route, find the shorter travel distance between two stops.

### Function Contract
**Inputs**

- `distance`: `distance[i]` is the clockwise distance from stop `i` to stop `(i + 1) mod n`.
- `start`: starting stop index.
- `destination`: destination stop index.

**Return value**

The shorter of the clockwise and counterclockwise distances.

### Examples
**Example 1**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 1`
- Output: `1`

**Example 2**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 2`
- Output: `3`

**Example 3**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 3`
- Output: `4`

---

## Solution
### Approach
Prefix/range sum on a circular array.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    clockwise = sum(distance[start:destination])
    total = sum(distance)
    return min(clockwise, total - clockwise)
```
</details>
