# Adjacent Increasing Subarrays Detection II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3350 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [adjacent-increasing-subarrays-detection-ii](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/).

### Goal
Determine the maximum integer `k` such that there exist two contiguous, non-overlapping subarrays of length `k` within the input array, where both subarrays are strictly increasing and positioned immediately adjacent to each other.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to analyze.

**Return value**

- An integer representing the largest possible value of `k` that satisfies the condition.

### Examples
**Example 1**

- Input: `nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]`
- Output: `3`
- Explanation: The subarrays `[2, 5, 7]` and `[8, 9, 2]` are not the answer, but `[5, 7, 8]` and `[9, 2, 3]` are not adjacent. The correct subarrays are `[2, 5, 7]` and `[8, 9, 2]` (length 3).

**Example 2**

- Input: `nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]`
- Output: `2`
- Explanation: The longest adjacent increasing subarrays are `[3, 4]` and `[4, 4]` (invalid) or `[5, 6]` and `[7]` (invalid). The max `k` is 2.

**Example 3**

- Input: `nums = [1, 1]`
- Output: `1`

---

## Solution
### Approach
The problem can be solved by pre-calculating the length of the strictly increasing subarray ending at each index. Once these lengths are computed, we can use binary search on the answer `k` or a linear scan to check if there exists an index `i` such that the increasing subarray ending at `i` has length at least `k`, and the increasing subarray starting at `i+1` also has length at least `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass to compute lengths and another pass to check for the condition.
- **Space Complexity**: `O(n)` to store the lengths of increasing subarrays ending at each index.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0

    # inc_len[i] stores the length of the strictly increasing subarray ending at i
    inc_len = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            inc_len[i] = inc_len[i - 1] + 1

    # To check if a k exists, we need two adjacent subarrays of length k.
    # This means there exists an index i such that:
    # 1. The subarray ending at i has length >= k
    # 2. The subarray starting at i+1 has length >= k
    # We can precompute the length of the increasing subarray starting at i
    start_len = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            start_len[i] = start_len[i + 1] + 1

    def check(k: int) -> bool:
        if k == 0:
            return True
        # We need two adjacent blocks of length k.
        # The first ends at i, the second starts at i+1.
        # So inc_len[i] >= k and start_len[i+1] >= k
        for i in range(n - k):
            if inc_len[i] >= k and start_len[i + 1] >= k:
                return True
        return False

    # Binary search for the maximum k
    low = 0
    high = n // 2
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
```
</details>
