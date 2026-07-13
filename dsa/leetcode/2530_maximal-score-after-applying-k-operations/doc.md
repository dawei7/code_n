# Maximal Score After Applying K Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2530 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximal-score-after-applying-k-operations](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximal-score-after-applying-k-operations/).

### Goal
Given an array of integers and an integer `k`, perform exactly `k` operations. In each operation, select an element from the array, add its value to your total score, and replace the selected element with its ceiling division by 3 (i.e., `ceil(value / 3)`). The objective is to maximize the total score accumulated after `k` operations.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available values.
- `k`: An integer representing the number of operations to perform.

**Return value**

- An integer representing the maximum possible total score after performing exactly `k` operations.

### Examples
**Example 1**

- Input: `nums = [10, 10, 10, 10, 10], k = 5`
- Output: `50`

**Example 2**

- Input: `nums = [1, 10, 3, 3, 3], k = 3`
- Output: `17`

**Example 3**

- Input: `nums = [1000000000], k = 3`
- Output: `1444444446`

---

## Solution
### Approach
The problem requires a greedy approach. To maximize the score, we must always pick the largest available number in the array. A **Max-Heap** (Priority Queue) is the optimal data structure to efficiently retrieve the maximum element and re-insert the modified value in $O(\log n)$ time.

### Complexity Analysis
- **Time Complexity**: $O(k \log n + n)$, where $n$ is the number of elements in `nums`. Building the heap takes $O(n)$, and performing $k$ operations, each involving a heap pop and push, takes $O(k \log n)$.
- **Space Complexity**: $O(n)$ to store the elements in the heap.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
import math

def solve(nums: list[int], k: int) -> int:
    """
    Maximizes the score by repeatedly picking the largest element,
    adding it to the score, and replacing it with ceil(val / 3).
    Uses a max-heap (simulated with negative values in Python's min-heap).
    """
    # Python's heapq is a min-heap. To simulate a max-heap,
    # we store the negative of each number.
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    total_score = 0

    for _ in range(k):
        # Extract the largest element
        largest = -heapq.heappop(max_heap)
        total_score += largest

        # Calculate ceil(largest / 3)
        # Using integer arithmetic: (largest + 2) // 3 is equivalent to ceil(largest / 3)
        new_val = (largest + 2) // 3

        # Push the new value back into the heap
        heapq.heappush(max_heap, -new_val)

    return total_score
```
</details>
