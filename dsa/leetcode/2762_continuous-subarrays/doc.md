# Continuous Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2762 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [continuous-subarrays](https://leetcode.com/problems/continuous-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/continuous-subarrays/).

### Goal
Given an integer array, identify the total count of contiguous subarrays where the absolute difference between any two elements within that subarray is at most 2.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 10^5 and 1 <= nums[i] <= 10^9.

**Return value**

- An integer representing the total number of valid continuous subarrays.

### Examples
**Example 1**

- Input: `nums = [5, 4, 2, 4]`
- Output: `8`

**Example 2**

- Input: `nums = [1, 2, 3]`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a **Sliding Window** approach combined with two **Monotonic Deques**. The deques maintain the indices of the maximum and minimum elements within the current window `[left, right]`. As we expand the window by moving `right`, we check if the condition `max_val - min_val <= 2` is violated. If it is, we increment `left` until the condition is restored. The number of valid subarrays ending at `right` is simply `right - left + 1`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is added and removed from the deques at most once.
- **Space Complexity**: `O(n)` in the worst case to store the indices in the deques, though practically `O(1)` since the window size is constrained by the value difference condition.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque

def solve(nums: list[int]) -> int:
    n = len(nums)
    left = 0
    count = 0

    # Monotonic deques to store indices
    # max_dq stores indices of elements in decreasing order
    # min_dq stores indices of elements in increasing order
    max_dq = deque()
    min_dq = deque()

    for right in range(n):
        # Maintain max_dq
        while max_dq and nums[max_dq[-1]] <= nums[right]:
            max_dq.pop()
        max_dq.append(right)

        # Maintain min_dq
        while min_dq and nums[min_dq[-1]] >= nums[right]:
            min_dq.pop()
        min_dq.append(right)

        # If condition is violated, shrink window from left
        while nums[max_dq[0]] - nums[min_dq[0]] > 2:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        # All subarrays ending at 'right' and starting from any index
        # between 'left' and 'right' are valid
        count += (right - left + 1)

    return count
```
</details>
