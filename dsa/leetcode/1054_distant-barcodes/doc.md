# Distant Barcodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1054 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [distant-barcodes](https://leetcode.com/problems/distant-barcodes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/distant-barcodes/).

### Goal
Rearrange the barcodes so equal values are never adjacent. A valid arrangement is guaranteed to exist.

### Function Contract
**Inputs**

- `barcodes`: List[int]

**Return value**

List[int] - any arrangement with no equal adjacent values

### Examples
**Example 1**

- Input: `barcodes = [1, 1, 1, 2, 2, 3]`
- Output: `[1, 2, 1, 2, 1, 3]`

**Example 2**

- Input: `barcodes = [1, 1, 1, 1, 2, 2, 3, 3]`
- Output: `[1, 2, 1, 3, 1, 2, 1, 3]`

**Example 3**

- Input: `barcodes = [7, 7, 8, 8]`
- Output: `[7, 8, 7, 8]`

---

## Solution
### Approach
Greedy max-heap rearrangement.

### Complexity Analysis
- **Time Complexity**: `O(n log u)` where `u` is the number of distinct barcodes
- **Space Complexity**: `O(u)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1054: Distant Barcodes."""

from collections import Counter
from heapq import heappop, heappush


def solve(barcodes: list[int]) -> list[int]:
    heap = [(-count, value) for value, count in Counter(barcodes).items()]
    result: list[int] = []
    import heapq

    heapq.heapify(heap)
    previous_count = 0
    previous_value = 0
    while heap:
        count, value = heappop(heap)
        result.append(value)
        if previous_count < 0:
            heappush(heap, (previous_count, previous_value))
        previous_count = count + 1
        previous_value = value
    return result
```
</details>
