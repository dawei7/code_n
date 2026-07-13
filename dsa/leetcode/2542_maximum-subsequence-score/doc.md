# Maximum Subsequence Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2542 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-subsequence-score](https://leetcode.com/problems/maximum-subsequence-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-subsequence-score/).

### Goal
Given two integer arrays of equal length, `nums1` and `nums2`, select a subsequence of length `k`. The score of this subsequence is calculated as the sum of elements from `nums1` at the chosen indices multiplied by the minimum value among the elements from `nums2` at those same indices. The objective is to maximize this score.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the primary values.
- `nums2`: A list of integers representing the values used to determine the multiplier.
- `k`: An integer representing the required length of the subsequence.

**Return value**

- An integer representing the maximum possible score achievable.

### Examples
**Example 1**

- Input: `nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3`
- Output: `12`
- Explanation: Select indices 0, 2, and 3. Sum of `nums1` is 1+3+2=6. Min of `nums2` is min(2,3,4)=2. Score = 6 * 2 = 12.

**Example 2**

- Input: `nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1`
- Output: `30`
- Explanation: Select index 2. Sum of `nums1` is 3. Min of `nums2` is 10. Score = 3 * 10 = 30.

**Example 3**

- Input: `nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3`
- Output: `168`

---

## Solution
### Approach
The problem is solved using a **Greedy approach combined with a Min-Heap**. By sorting the pairs based on `nums2` in descending order, we can iterate through the array and treat each `nums2[i]` as the potential minimum of the subsequence. For each step, we maintain a running sum of the largest `k` elements from `nums1` encountered so far using a min-heap. This ensures that for every possible minimum from `nums2`, we have the largest possible sum from `nums1`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` due to sorting the pairs, where `n` is the length of the arrays. The heap operations take `O(n log k)`.
- **Space Complexity**: `O(n)` to store the pairs and `O(k)` for the min-heap.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    # Pair elements and sort by nums2 in descending order
    # This allows us to treat the current nums2 value as the minimum
    pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

    min_heap = []
    current_sum = 0
    max_score = 0

    for i in range(len(pairs)):
        val1, val2 = pairs[i]

        # Add current val1 to the heap and update the running sum
        heapq.heappush(min_heap, val1)
        current_sum += val1

        # If we have more than k elements, remove the smallest val1
        if len(min_heap) > k:
            smallest = heapq.heappop(min_heap)
            current_sum -= smallest

        # If we have exactly k elements, calculate the score
        if len(min_heap) == k:
            # The current val2 is the minimum because we sorted descending
            max_score = max(max_score, current_sum * val2)

    return max_score
```
</details>
