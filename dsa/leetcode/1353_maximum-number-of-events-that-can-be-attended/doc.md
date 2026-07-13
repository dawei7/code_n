# Maximum Number of Events That Can Be Attended

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1353 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-events-that-can-be-attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/).

### Goal
Given a list of events where each event has a starting day and an ending day, attend at most one event per day and choose days so the total number of attended events is as large as possible.

### Function Contract
**Inputs**

- `events`: a list of `[startDay, endDay]` pairs.

**Return value**

The maximum number of events that can be attended.

### Examples
**Example 1**

- Input: `events = [[1,2],[2,3],[3,4]]`
- Output: `3`

**Example 2**

- Input: `events = [[1,2],[2,2],[3,3],[3,4]]`
- Output: `4`

**Example 3**

- Input: `events = [[1,4],[1,4],[1,4],[2,2]]`
- Output: `2`

---

## Solution
### Approach
Greedy scheduling with sorting and a min-heap. Sweep days in increasing order, add events that have started, discard expired events, and attend the event with the earliest ending day.

### Complexity Analysis
- **Time Complexity**: `O(n log n + D log n)`, where `n` is the number of events and `D` is the swept day range; an implementation that jumps between active days is commonly summarized as `O(n log n)`.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1353: Maximum Number of Events That Can Be Attended."""

from heapq import heappop, heappush


def solve(events: list[list[int]]) -> int:
    events.sort()
    heap: list[int] = []
    day = 0
    i = 0
    attended = 0
    n = len(events)

    while i < n or heap:
        if not heap:
            day = max(day, events[i][0])
        while i < n and events[i][0] <= day:
            heappush(heap, events[i][1])
            i += 1
        while heap and heap[0] < day:
            heappop(heap)
        if heap:
            heappop(heap)
            attended += 1
            day += 1
    return attended
```
</details>
