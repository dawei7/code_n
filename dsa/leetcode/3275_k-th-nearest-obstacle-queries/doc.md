# K-th Nearest Obstacle Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3275 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [k-th-nearest-obstacle-queries](https://leetcode.com/problems/k-th-nearest-obstacle-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/k-th-nearest-obstacle-queries/).

### Goal
Given a sequence of 2D coordinates representing obstacles appearing one by one, determine the distance of the k-th nearest obstacle from the origin (0, 0) after each new obstacle is added. The distance is defined as the Manhattan distance: |x| + |y|. If there are fewer than k obstacles currently present, the result for that step is -1.

### Function Contract
**Inputs**

- `queries`: A list of lists where each sub-list contains two integers `[x, y]` representing the coordinates of an obstacle.
- `k`: An integer representing the rank of the distance to track.

**Return value**

- A list of integers where the i-th element is the k-th smallest Manhattan distance after processing the first i+1 queries.

### Examples
**Example 1**

- Input: `queries = [[1,2],[3,4],[2,3],[-3,0]]`, `k = 2`
- Output: `[-1, 7, 5, 3]`

**Example 2**

- Input: `queries = [[5,5],[4,4],[3,3]]`, `k = 1`
- Output: `[10, 8, 6]`

**Example 3**

- Input: `queries = [[1,2],[3,4],[2,3],[-3,0]]`, `k = 3`
- Output: `[-1, -1, 6, 5]`

---

## Solution
### Approach
The problem is solved using a **Max-Heap**. By maintaining a max-heap of size `k`, we ensure that the root of the heap always represents the largest distance among the `k` closest obstacles found so far. When a new obstacle is added, if the heap size is less than `k`, we push the distance. If the heap size is `k` and the new distance is smaller than the current maximum in the heap, we pop the maximum and push the new distance.

### Complexity Analysis
- **Time Complexity**: `O(N log k)`, where `N` is the number of queries. Each insertion and deletion operation in the heap takes `O(log k)` time.
- **Space Complexity**: `O(k)`, as we only store at most `k` distances in the heap at any given time.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
from typing import List

def solve(queries: List[List[int]], k: int) -> List[int]:
    # We use a max-heap to keep track of the k smallest distances.
    # Since Python's heapq is a min-heap, we store negative values to simulate a max-heap.
    max_heap = []
    results = []

    for x, y in queries:
        dist = abs(x) + abs(y)

        if len(max_heap) < k:
            heapq.heappush(max_heap, -dist)
        elif dist < -max_heap[0]:
            heapq.heapreplace(max_heap, -dist)

        if len(max_heap) < k:
            results.append(-1)
        else:
            results.append(-max_heap[0])

    return results
```
</details>
