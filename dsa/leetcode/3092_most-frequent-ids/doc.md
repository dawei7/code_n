# Most Frequent IDs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3092 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [most-frequent-ids](https://leetcode.com/problems/most-frequent-ids/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/most-frequent-ids/).

### Goal
Given two arrays representing IDs and their corresponding frequency changes over time, track the maximum frequency of any ID after each update. An update consists of adding a specific value (positive or negative) to the frequency count of a given ID. After every update, return the current highest frequency among all IDs present in the system.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the IDs being updated.
- `freq`: A list of integers representing the change in frequency for the corresponding ID at the same index.

**Return value**

- A list of integers where each element corresponds to the maximum frequency observed after the update at that index.

### Examples
**Example 1**

- Input: `nums = [2,3,2,1], freq = [3,2,-3,1]`
- Output: `[3,3,2,2]`

**Example 2**

- Input: `nums = [5,5,3], freq = [2,-2,1]`
- Output: `[2,0,1]`

**Example 3**

- Input: `nums = [1,1,1], freq = [1,1,1]`
- Output: `[1,2,3]`

---

## Solution
### Approach
The problem is solved using a Hash Map (to store the current frequency of each ID) combined with a Max-Heap (to track the maximum frequency). Since Python's `heapq` does not support arbitrary deletions, we use "lazy removal": we store `(-frequency, id)` tuples in the heap. When querying the top, we verify if the frequency at the top of the heap matches the current frequency stored in our Hash Map. If it does not, the entry is stale and is discarded.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of updates. Each update involves a heap push and potentially multiple heap pops (lazy removal), both of which are logarithmic.
- **Space Complexity**: `O(N)`, required to store the frequency map and the heap, which can grow up to the size of the number of updates.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
from collections import defaultdict

def solve(nums: list[int], freq: list[int]) -> list[int]:
    # Map to store the current frequency of each ID
    counts = defaultdict(int)
    # Max-heap to store (-frequency, id)
    # We use negative frequency because heapq is a min-heap by default
    max_heap = []
    results = []

    for i in range(len(nums)):
        id_val = nums[i]
        change = freq[i]

        # Update the frequency in the hash map
        counts[id_val] += change

        # Push the new frequency into the heap
        heapq.heappush(max_heap, (-counts[id_val], id_val))

        # Lazy removal: check if the top of the heap is stale
        # The top is stale if the frequency in the heap doesn't match the current map
        while max_heap and -max_heap[0][0] != counts[max_heap[0][1]]:
            heapq.heappop(max_heap)

        # The current max frequency is at the top of the heap
        if max_heap:
            results.append(-max_heap[0][0])
        else:
            results.append(0)

    return results
```
</details>
