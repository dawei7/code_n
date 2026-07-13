# Maximum Number of Operations With the Same Score II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3040 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-operations-with-the-same-score-ii](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/).

### Goal
Given an array of integers, perform a series of operations where each operation involves removing two elements from either the beginning, the end, or one from each end. The constraint is that every operation must result in the same sum as the first operation. The objective is to maximize the total number of operations performed.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to be processed.

**Return value**

- An integer representing the maximum number of operations possible under the constraint that all operations must yield the same sum as the initial operation.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 2, 3, 4]`
- Output: `3`
- Explanation: The first operation can remove the first two elements (3+2=5). Subsequent operations must also sum to 5.

**Example 2**

- Input: `nums = [3, 2, 6, 1, 4]`
- Output: `2`
- Explanation: The first operation can remove the first and last elements (3+4=7). Subsequent operations must also sum to 7.

**Example 3**

- Input: `nums = [2, 2, 2, 2]`
- Output: `2`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with Memoization. Since we need to explore different ways to remove elements (front-front, back-back, or front-back) while maintaining a fixed target sum, we define a recursive function `dp(i, j, target)` that returns the maximum operations possible for the subarray `nums[i...j]` given a required `target` sum.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the array. There are `O(n^2)` possible states for the subarray boundaries `(i, j)`, and each state takes constant time to compute.
- **Space Complexity**: `O(n^2)` to store the memoization table for the states.

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache
import sys

def solve(nums: list[int]) -> int:
    n = len(nums)
    sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 50))

    @lru_cache(None)
    def get_max_ops(i, j, target):
        if i >= j:
            return 0

        res = 0
        # Option 1: Remove two from the front
        if i + 1 <= j and nums[i] + nums[i + 1] == target:
            res = max(res, 1 + get_max_ops(i + 2, j, target))

        # Option 2: Remove two from the back
        if j - 1 >= i and nums[j] + nums[j - 1] == target:
            res = max(res, 1 + get_max_ops(i, j - 2, target))

        # Option 3: Remove one from front and one from back
        if i < j and nums[i] + nums[j] == target:
            res = max(res, 1 + get_max_ops(i + 1, j - 1, target))

        return res

    # The first operation determines the target sum.
    # There are three possible first operations:
    # 1. First two elements
    # 2. Last two elements
    # 3. First and last element

    ans1 = 1 + get_max_ops(2, n - 1, nums[0] + nums[1])
    ans2 = 1 + get_max_ops(0, n - 3, nums[n - 1] + nums[n - 2])
    ans3 = 1 + get_max_ops(1, n - 2, nums[0] + nums[n - 1])

    return max(ans1, ans2, ans3)
```
</details>
