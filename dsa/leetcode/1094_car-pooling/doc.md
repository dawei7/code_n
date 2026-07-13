# Car Pooling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1094 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [car-pooling](https://leetcode.com/problems/car-pooling/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/car-pooling/).

### Goal
A vehicle can carry at most `capacity` passengers. Given `trips = [[numPassengers, from, to], ...]`, return `True` if all trips can be completed without exceeding capacity.

### Function Contract
**Inputs**

- `trips`: List[List[int]] - [passengers, from, to]
- `capacity`: int

**Return value**

bool - True if all trips can be completed

### Examples
**Example 1**

- Input: `trips = [[2, 1, 5], [3, 3, 7]], capacity = 4`
- Output: `False`

**Example 2**

- Input: `trips = [[5, 16, 20]], capacity = 8`
- Output: `True`

**Example 3**

- Input: `trips = [[3, 18, 30]], capacity = 9`
- Output: `True`

---

## Solution
### Approach
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1094: Car Pooling."""


def solve(trips: list[list[int]], capacity: int) -> bool:
    changes: dict[int, int] = {}
    for passengers, start, end in trips:
        changes[start] = changes.get(start, 0) + passengers
        changes[end] = changes.get(end, 0) - passengers

    current = 0
    for location in sorted(changes):
        current += changes[location]
        if current > capacity:
            return False
    return True
```
</details>
