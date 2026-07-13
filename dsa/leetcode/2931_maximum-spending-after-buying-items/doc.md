# Maximum Spending After Buying Items

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2931 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-spending-after-buying-items](https://leetcode.com/problems/maximum-spending-after-buying-items/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-spending-after-buying-items/).

### Goal
You are given a 2D grid of prices where each row represents a shop's inventory, sorted in non-decreasing order. You must purchase every single item across all shops over a series of days. On day `d` (starting from 1), you buy one item. The cost of an item is multiplied by `d`. To maximize your total spending, you must strategically choose which item to buy each day, always picking from the available items at the end of each shop's row.

### Function Contract
**Inputs**

- `values`: A list of lists of integers (`List[List[int]]`), where `values[i][j]` represents the price of the `j`-th item in the `i`-th shop.

**Return value**

- An integer representing the maximum total cost accumulated after purchasing all items.

### Examples
**Example 1**

- Input: `values = [[8,5,2],[6,4,1],[9,7,3]]`
- Output: `285`

**Example 2**

- Input: `values = [[10,8,6,4,2],[9,7,5,3,1]]`
- Output: `386`

---

## Solution
### Approach
The problem is solved using a **Greedy approach** combined with a **Min-Heap (Priority Queue)**. Since we want to maximize the total sum and the multiplier `d` increases daily, we should prioritize buying the smallest available items first (to save the larger values for higher multipliers). Because each row is sorted, the smallest available item in any shop is always at the current end of the row. We maintain a min-heap of the last elements of all rows to efficiently extract the global minimum across all shops.

### Complexity Analysis
- **Time Complexity**: `O(N * M * log(N))`, where `N` is the number of shops and `M` is the number of items per shop. We perform `N * M` extractions from the heap, and each heap operation takes `O(log N)`.
- **Space Complexity**: `O(N)`, as the heap stores at most one element from each of the `N` shops.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
from typing import List

def solve(values: List[List[int]]) -> int:
    """
    Calculates the maximum spending by greedily picking the smallest available
    items across all shops using a min-heap.
    """
    m = len(values)
    n = len(values[0])

    # Min-heap stores tuples of (price, row_index)
    # We initialize it with the last element of each row.
    min_heap = []
    for i in range(m):
        heapq.heappush(min_heap, (values[i][n - 1], i))

    # Keep track of the current index being pointed to in each row
    row_pointers = [n - 1] * m

    total_spending = 0
    # We buy one item per day for m * n days
    for day in range(1, (m * n) + 1):
        price, row_idx = heapq.heappop(min_heap)

        # Add to total spending multiplied by the current day
        total_spending += price * day

        # Move the pointer for this row to the left
        row_pointers[row_idx] -= 1

        # If there are still items in this row, push the next one to the heap
        if row_pointers[row_idx] >= 0:
            next_price = values[row_idx][row_pointers[row_idx]]
            heapq.heappush(min_heap, (next_price, row_idx))

    return total_spending
```
</details>
