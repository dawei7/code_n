# Minimum Operations to Exceed Threshold Value II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3066 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-exceed-threshold-value-ii](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/).

### Goal
Given an array of integers and a target threshold `k`, perform a repeated operation: remove the two smallest elements from the array, calculate their combined value as `(min1 * 2) + min2`, and insert this new value back into the array. Continue this process until all elements in the array are greater than or equal to `k`. Return the total number of operations required to satisfy this condition.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the current values.
- `k`: An integer representing the minimum threshold value.

**Return value**

- An integer representing the total count of operations performed.

### Examples
**Example 1**

- Input: `nums = [2, 11, 10, 1, 3], k = 10`
- Output: `2`

**Example 2**

- Input: `nums = [1, 1, 2, 4, 9], k = 20`
- Output: `4`

**Example 3**

- Input: `nums = [999999999, 999999999, 999999999], k = 1000000000`
- Output: `2`

---

## Solution
### Approach
The problem is solved using a **Min-Heap (Priority Queue)**. By maintaining the collection of numbers in a min-heap, we can efficiently extract the two smallest elements in $O(\log n)$ time and insert the new calculated value in $O(\log n)$ time. This greedy approach ensures that we always combine the smallest available values, which is optimal for reaching the threshold `k` in the fewest steps.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the number of elements in `nums`. Each operation involves heap extractions and insertions, and in the worst case, we perform $O(n)$ operations.
- **Space Complexity**: $O(n)$ to store the elements in the heap.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to make all elements >= k.
    Uses a min-heap to greedily combine the two smallest elements.
    """
    heap = list(nums)
    heapq.heapify(heap)

    operations = 0

    # Continue until the smallest element is at least k
    while len(heap) > 1 and heap[0] < k:
        # Extract the two smallest elements
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)

        # Calculate the new value and push it back
        new_val = x * 2 + y
        heapq.heappush(heap, new_val)

        operations += 1

    return operations
```
</details>
