# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1438 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/).

### Goal
Find the longest contiguous subarray where the difference between the largest and smallest values is at most `limit`.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `limit`: the maximum allowed absolute difference inside the window.

**Return value**

The maximum length of a valid contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [8,2,4,7], limit = 4`
- Output: `2`

**Example 2**

- Input: `nums = [10,1,2,4,7,2], limit = 5`
- Output: `4`

**Example 3**

- Input: `nums = [4,2,2,2,4,4,2,2], limit = 0`
- Output: `3`

---

## Solution
### Approach
Sliding window with two monotonic deques. One deque keeps candidate maximums and the other keeps candidate minimums; shrink the left side until their difference is within the limit.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the deques in the worst case.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(nums, limit):
    min_q = deque()
    max_q = deque()
    left = 0
    best = 0
    for right, value in enumerate(nums):
        while min_q and nums[min_q[-1]] >= value:
            min_q.pop()
        while max_q and nums[max_q[-1]] <= value:
            max_q.pop()
        min_q.append(right)
        max_q.append(right)
        while nums[max_q[0]] - nums[min_q[0]] > limit:
            if min_q[0] == left:
                min_q.popleft()
            if max_q[0] == left:
                max_q.popleft()
            left += 1
        best = max(best, right - left + 1)
    return best
```
</details>
