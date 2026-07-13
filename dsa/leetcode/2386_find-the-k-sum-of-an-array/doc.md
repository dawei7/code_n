# Find the K-Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2386 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-k-sum-of-an-array](https://leetcode.com/problems/find-the-k-sum-of-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-k-sum-of-an-array/).

### Goal
Given an array of integers, calculate the k-th largest subsequence sum. A subsequence is formed by deleting zero or more elements from the original array. Note that the empty subsequence has a sum of 0.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the rank of the subsequence sum to find.

**Return value**

- An integer representing the k-th largest subsequence sum.

### Examples
**Example 1**

- Input: `nums = [2, 4, -2], k = 5`
- Output: `2`
- Explanation: The subsequence sums are: [4, 2, 2, 2, 0, 0, -2, -2]. The 5th largest is 2.

**Example 2**

- Input: `nums = [1, -2, 3, 4, -10, 12], k = 16`
- Output: `10`

**Example 3**

- Input: `nums = [10, -2, 10], k = 1`
- Output: `20`

---

## Solution
### Approach
The problem is solved by first calculating the maximum possible subsequence sum (the sum of all positive numbers). To find the subsequent k-1 sums, we treat the problem as finding the smallest "losses" from the maximum sum. We transform the array by taking the absolute values of all elements and sorting them. We then use a min-heap to explore combinations of these absolute values, which represent the subtractions from the maximum sum.

### Complexity Analysis
- **Time Complexity**: O(n log n + k log k), where n is the length of the array. Sorting takes O(n log n), and extracting k elements from the heap takes O(k log k).
- **Space Complexity**: O(n + k), to store the sorted array and the heap elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(nums: list[int], k: int) -> int:
    # The maximum subsequence sum is the sum of all positive numbers.
    max_sum = sum(x for x in nums if x > 0)

    # We want to find the (k-1)-th smallest "loss" from the max_sum.
    # A loss is created by either removing a positive number or adding a negative number.
    # Both operations are equivalent to subtracting abs(x) from the max_sum.
    abs_nums = sorted([abs(x) for x in nums])

    # If k=1, the answer is simply the max_sum.
    if k == 1:
        return max_sum

    # Min-heap stores (loss, index)
    # We explore the smallest losses using a heap.
    pq = [(abs_nums[0], 0)]
    current_loss = 0

    for _ in range(k - 1):
        current_loss, i = heapq.heappop(pq)

        if i + 1 < len(abs_nums):
            # Option 1: Add the next element to the current loss
            heapq.heappush(pq, (current_loss + abs_nums[i + 1], i + 1))
            # Option 2: Replace the current element with the next element
            heapq.heappush(pq, (current_loss - abs_nums[i] + abs_nums[i + 1], i + 1))

    return max_sum - current_loss
```
</details>
