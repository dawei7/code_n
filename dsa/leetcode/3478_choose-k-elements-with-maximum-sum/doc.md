# Choose K Elements With Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3478 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [choose-k-elements-with-maximum-sum](https://leetcode.com/problems/choose-k-elements-with-maximum-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/choose-k-elements-with-maximum-sum/).

### Goal
Given two arrays `nums1` and `nums2` of length `n` and an integer `k`, for each index `i`, calculate the sum of the `k` largest elements from `nums2` corresponding to indices `j` where `nums1[j] < nums1[i]`. If there are fewer than `k` such indices, the result for that index is -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the primary criteria for selection.
- `nums2`: A list of integers representing the values to be summed.
- `k`: An integer representing the number of elements to select.

**Return value**

- A list of integers where the $i$-th element is the maximum sum of $k$ elements from `nums2` associated with indices $j$ where `nums1[j] < nums1[i]`.

### Examples
**Example 1**

- Input: `nums1 = [4, 2, 1, 5, 3], nums2 = [10, 20, 30, 40, 50], k = 2`
- Output: `[60, 30, -1, 70, 50]`

**Example 2**

- Input: `nums1 = [2, 2], nums2 = [5, 5], k = 1`
- Output: `[-1, -1]`

**Example 3**

- Input: `nums1 = [1, 2, 3], nums2 = [1, 2, 3], k = 1`
- Output: `[-1, 1, 3]`

---

## Solution
### Approach
The problem is solved by sorting the indices based on `nums1` values. By processing indices in increasing order of `nums1[i]`, we can maintain a sliding window of `nums2` values that satisfy the condition `nums1[j] < nums1[i]`. A min-heap is used to keep track of the `k` largest values encountered so far, allowing for efficient updates and sum retrieval.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the input arrays, due to sorting the indices and heap operations.
- **Space Complexity**: $O(n)$, required to store the sorted indices, the heap, and the result array.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(nums1, nums2, k):
    n = len(nums1)
    # Create a list of indices and sort them based on nums1 values
    indices = sorted(range(n), key=lambda i: nums1[i])

    res = [0] * n
    min_heap = []
    current_sum = 0

    # We need to process indices such that we only consider j where nums1[j] < nums1[i]
    # Since multiple indices might have the same nums1 value, we group them
    i = 0
    while i < n:
        j = i
        # Find all indices with the same nums1 value
        while j < n and nums1[indices[j]] == nums1[indices[i]]:
            j += 1

        # For all indices in the current group, the valid j's are those processed before this group
        for idx in range(i, j):
            original_idx = indices[idx]
            res[original_idx] = current_sum

        # Now add the current group's nums2 values to the heap
        for idx in range(i, j):
            val = nums2[indices[idx]]
            heapq.heappush(min_heap, val)
            current_sum += val
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

        i = j

    return res
```
</details>
