# Last Stone Weight

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1046 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [last-stone-weight](https://leetcode.com/problems/last-stone-weight/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/last-stone-weight/).

### Goal
You have a collection of `stones` with various weights. On each turn, take the two heaviest stones and smash them together. If equal, both are destroyed; otherwise the smaller is destroyed and the larger is reduced by the smaller weight. Return the weight of the last stone (or 0 if none remain).

### Function Contract
**Inputs**

- `stones`: List[int]

**Return value**

int - weight of last stone or 0

### Examples
**Example 1**

- Input: `stones = [2, 7, 4, 1, 8, 1]`
- Output: `1`

**Example 2**

- Input: `stones = [50, 98]`
- Output: `48`

**Example 3**

- Input: `stones = [18, 73]`
- Output: `55`

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
"""Optimal solution for LeetCode 1046: Last Stone Weight."""

from heapq import heapify, heappop, heappush


def solve(stones: list[int]) -> int:
    heap = [-stone for stone in stones]
    heapify(heap)
    while len(heap) > 1:
        first = -heappop(heap)
        second = -heappop(heap)
        if first != second:
            heappush(heap, -(first - second))
    return -heap[0] if heap else 0
```
</details>
