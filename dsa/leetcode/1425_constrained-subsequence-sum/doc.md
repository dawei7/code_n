# Constrained Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1425 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [constrained-subsequence-sum](https://leetcode.com/problems/constrained-subsequence-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/constrained-subsequence-sum/).

### Goal
Choose a non-empty subsequence whose adjacent chosen indices differ by at most `k`, and maximize the sum of chosen values.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the maximum allowed gap between consecutive chosen indices.

**Return value**

The maximum constrained subsequence sum.

### Examples
**Example 1**

- Input: `nums = [10,2,-10,5,20], k = 2`
- Output: `37`

**Example 2**

- Input: `nums = [-1,-2,-3], k = 1`
- Output: `-1`

**Example 3**

- Input: `nums = [10,-2,-10,-5,20], k = 2`
- Output: `23`

---

## Solution
### Approach
Dynamic programming with a monotonic deque. Let `dp[i]` be the best valid subsequence ending at `i`; it uses the maximum positive `dp` from the previous `k` positions.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(k)` for the deque, or `O(n)` if all DP values are stored.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(nums, k):
    if not nums:
        return 0
    k = max(1, int(k))
    best = nums[:]
    queue = deque()
    answer = nums[0]
    for index, value in enumerate(nums):
        while queue and queue[0] < index - k:
            queue.popleft()
        if queue:
            best[index] = value + max(0, best[queue[0]])
        answer = max(answer, best[index])
        while queue and best[queue[-1]] <= best[index]:
            queue.pop()
        queue.append(index)
    return answer
```
</details>
