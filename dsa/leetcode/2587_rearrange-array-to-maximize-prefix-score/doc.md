# Rearrange Array to Maximize Prefix Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2587 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [rearrange-array-to-maximize-prefix-score](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/).

### Goal
Given an array of integers, reorder its elements to maximize the number of positive prefix sums. A prefix sum at index `i` is defined as the sum of all elements from index `0` to `i`. The objective is to return the count of indices where the prefix sum is strictly greater than zero.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum possible count of positive prefix sums achievable by reordering the input array.

### Examples
**Example 1**

- Input: `nums = [2, -1, 0, 1, -3, 3, -3]`
- Output: `6`

**Example 2**

- Input: `nums = [-2, -3, 0]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a **Greedy** approach combined with **Sorting**. To maximize the number of positive prefix sums, we should prioritize adding larger positive numbers first to build a "buffer" that can offset subsequent negative numbers. By sorting the array in descending order, we ensure that the prefix sum grows as quickly as possible, allowing us to include as many negative numbers as possible while keeping the running total above zero.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the length of the input array, due to the sorting step. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation (Python's Timsort uses `O(N)` space).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Maximizes the number of positive prefix sums by sorting the array
    in descending order and calculating the prefix sums.
    """
    # Sort in descending order to maximize the prefix sum growth
    nums.sort(reverse=True)

    count = 0
    current_prefix_sum = 0

    for num in nums:
        current_prefix_sum += num
        if current_prefix_sum > 0:
            count += 1
        else:
            # Since the array is sorted descending, if the current sum
            # is <= 0, all subsequent sums will also be <= 0.
            break

    return count
```
</details>
