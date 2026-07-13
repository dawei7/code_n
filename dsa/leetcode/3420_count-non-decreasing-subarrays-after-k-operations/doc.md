# Count Non-Decreasing Subarrays After K Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3420 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Segment Tree, Queue, Sliding Window, Monotonic Stack, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-non-decreasing-subarrays-after-k-operations](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/).

### Goal
Given an array of integers and an integer `k`, determine the total number of subarrays that can be transformed into a non-decreasing sequence using at most `k` operations. An operation consists of decreasing any element in the subarray by 1. A subarray is valid if there exists a sequence of operations such that the resulting subarray is non-decreasing.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the maximum number of operations allowed.

**Return value**

- An integer representing the total count of valid subarrays.

### Examples
**Example 1**

- Input: `nums = [5, 4, 3, 2, 1], k = 1`
- Output: `5`

**Example 2**

- Input: `nums = [1, 2, 3], k = 0`
- Output: `6`

**Example 3**

- Input: `nums = [6, 3, 1], k = 20`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a sliding window approach combined with a monotonic stack. To maintain the non-decreasing property with minimum operations, we observe that for a subarray `nums[i...j]`, the cost to make it non-decreasing is the sum of `max(0, nums[p] - nums[p+1])` after adjustments. We maintain a monotonic stack to track the "peaks" of the current window. As the right pointer `j` expands, we calculate the cost to maintain the non-decreasing property using the stack to efficiently compute the prefix sums of the required decreases.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array. Each element is pushed and popped from the monotonic stack at most once.
- **Space Complexity**: `O(n)` to store the monotonic stack and auxiliary arrays for prefix sums.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    right = n - 1
    cost = 0
    answer = 0
    blocks = deque()

    for left in range(n - 1, -1, -1):
        while blocks and nums[left] > nums[blocks[-1]]:
            index = blocks.pop()
            next_index = blocks[-1] if blocks else right + 1
            cost += (next_index - index) * (nums[left] - nums[index])
        blocks.append(left)

        while cost > k:
            cost -= nums[blocks[0]] - nums[right]
            if blocks[0] == right:
                blocks.popleft()
            right -= 1

        answer += right - left + 1

    return answer
```
</details>
