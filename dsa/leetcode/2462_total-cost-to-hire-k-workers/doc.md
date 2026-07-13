# Total Cost to Hire K Workers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2462 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [total-cost-to-hire-k-workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/total-cost-to-hire-k-workers/).

### Goal
Given an array of worker costs, you must hire exactly `k` workers. In each of the `k` sessions, you choose the worker with the lowest cost from either the first `candidates` elements or the last `candidates` elements of the current array. If there is a tie in cost, the worker with the smaller index is chosen. Once a worker is hired, they are removed from the pool, and the remaining workers shift to fill the gap. Calculate the total cost of hiring `k` workers.

### Function Contract
**Inputs**

- `costs`: A list of integers representing the hiring cost of each worker.
- `k`: An integer representing the total number of workers to hire.
- `candidates`: An integer representing the number of workers to consider from the front and back ends of the array.

**Return value**

- An integer representing the total cost incurred after hiring `k` workers.

### Examples
**Example 1**

- Input: `costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4`
- Output: `11`

**Example 2**

- Input: `costs = [1,2,4,1], k = 3, candidates = 3`
- Output: `4`

**Example 3**

- Input: `costs = [1,2,4,1], k = 3, candidates = 1`
- Output: `4`

---

## Solution
### Approach
The problem is solved using a **Two-Pointer** approach combined with two **Min-Heaps** (Priority Queues). We maintain two heaps: one for the `candidates` workers at the front and one for the `candidates` workers at the back. By comparing the minimums of both heaps, we greedily select the cheapest worker. If the heaps overlap or are exhausted, we replenish them using the two pointers until all `k` workers are selected.

### Complexity Analysis
- **Time Complexity**: `O(k * log(candidates))`. Each of the `k` hiring sessions involves heap operations (pop and potentially push) which take logarithmic time relative to the number of candidates.
- **Space Complexity**: `O(candidates)`. We store at most `2 * candidates` elements in the two heaps at any given time.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(costs: list[int], k: int, candidates: int) -> int:
    n = len(costs)
    left_heap = []
    right_heap = []

    left_ptr = 0
    right_ptr = n - 1

    # Fill the heaps initially
    # We use (cost, index) to handle tie-breaking by index automatically
    while len(left_heap) < candidates and left_ptr <= right_ptr:
        heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
        left_ptr += 1

    while len(right_heap) < candidates and left_ptr <= right_ptr:
        heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
        right_ptr -= 1

    total_cost = 0
    for _ in range(k):
        # Determine which heap has the smaller minimum
        # If one heap is empty, we must pick from the other
        if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
            cost, idx = heapq.heappop(left_heap)
            total_cost += cost
            # Replenish left heap if possible
            if left_ptr <= right_ptr:
                heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                left_ptr += 1
        else:
            cost, idx = heapq.heappop(right_heap)
            total_cost += cost
            # Replenish right heap if possible
            if left_ptr <= right_ptr:
                heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                right_ptr -= 1

    return total_cost
```
</details>
