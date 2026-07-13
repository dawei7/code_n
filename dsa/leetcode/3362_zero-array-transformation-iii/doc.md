# Zero Array Transformation III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3362 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [zero-array-transformation-iii](https://leetcode.com/problems/zero-array-transformation-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/zero-array-transformation-iii/).

### Goal
Given an array `nums` and a collection of range queries `[l, r]`, each remaining query can decrement each index in its range by at most `1`, independently per index. Remove as many queries as possible while still being able to reduce `nums` to all zeroes. If even using every query is insufficient, return `-1`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the target values to be reduced to zero.
- `queries`: A list of intervals `[l, r]`.

**Return value**

- The maximum number of queries that can be removed, or `-1` if the zero array transformation is impossible.

### Examples
**Example 1**

- Input: `nums = [2, 0, 2]`, `queries = [[0, 2], [0, 2], [1, 1]]`
- Output: `1`

**Example 2**

- Input: `nums = [1, 1, 1, 1]`, `queries = [[1, 3], [0, 2], [1, 3], [1, 2]]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 3, 4]`, `queries = [[0, 3]]`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using a **Greedy approach combined with a Max-Heap**. We iterate through the array indices, maintaining a set of "active" queries that cover the current index. We use a difference array (or a sweep-line technique) to track the current reduction applied to each index. If the current value is still greater than zero, we greedily pick the available queries that extend the furthest to the right to satisfy the requirement, as these are most likely to help with future indices.

### Complexity Analysis
- **Time Complexity**: `O(N log N + Q log Q)`, where `N` is the length of `nums` and `Q` is the number of queries. This accounts for sorting the queries and heap operations.
- **Space Complexity**: `O(N + Q)` to store the difference array and the query structures.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
from collections import defaultdict

def solve(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)
    # Group queries by their start index
    starts = defaultdict(list)
    for l, r in queries:
        starts[l].append(r)

    # Max-heap to store the end indices of active queries
    # We want to pick queries that end as far as possible
    active_queries = []

    # Difference array to track current reduction applied to nums[i]
    diff = [0] * (n + 1)
    current_reduction = 0
    count = 0

    for i in range(n):
        # Add all queries starting at i to the heap
        for r in starts[i]:
            heapq.heappush(active_queries, -r)

        # Update current reduction using difference array
        current_reduction += diff[i]

        # While current value is not satisfied, use queries
        while nums[i] + current_reduction > 0:
            if not active_queries:
                return -1

            # Pick the query that ends furthest to the right
            r = -heapq.heappop(active_queries)

            # If the query ends before current index, it's useless
            if r < i:
                continue

            # Apply the query
            count += 1
            current_reduction -= 1
            # The effect of this query ends at r
            diff[r + 1] += 1

    return len(queries) - count
```
</details>
