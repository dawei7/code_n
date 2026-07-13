# Find All Good Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2420 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-all-good-indices](https://leetcode.com/problems/find-all-good-indices/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-all-good-indices/).

### Goal
Identify all indices `i` in an array `nums` such that the `k` elements immediately preceding `i` are in non-increasing order, and the `k` elements immediately following `i` are in non-decreasing order. The index `i` itself is excluded from these checks.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to analyze.
- `k`: An integer representing the required length of the non-increasing and non-decreasing subarrays.

**Return value**

- A list of integers representing all valid "good" indices in ascending order.

### Examples
**Example 1**

- Input: `nums = [2,1,1,1,3,4,1], k = 2`
- Output: `[2, 3]`

**Example 2**

- Input: `nums = [2,1,1,2], k = 2`
- Output: `[]`

**Example 3**

- Input: `nums = [1,2,3,4,5], k = 1`
- Output: `[1, 2, 3]`

---

## Solution
### Approach
The problem is solved using Dynamic Programming (or Prefix/Suffix arrays). We precompute two boolean arrays: `non_increasing` and `non_decreasing`. `non_increasing[i]` tracks how many consecutive elements ending at `i` are non-increasing, and `non_decreasing[i]` tracks how many consecutive elements starting at `i` are non-decreasing. An index `i` is "good" if `non_increasing[i-1] >= k` and `non_decreasing[i+1] >= k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a constant number of linear passes over the data.
- **Space Complexity**: `O(n)` to store the precomputed prefix and suffix counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if k == 0:
        return list(range(n))

    # inc[i] stores the length of the non-increasing sequence ending at i
    inc = [1] * n
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            inc[i] = inc[i - 1] + 1

    # dec[i] stores the length of the non-decreasing sequence starting at i
    dec = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            dec[i] = dec[i + 1] + 1

    result = []
    # A good index i must have k elements before it non-increasing
    # and k elements after it non-decreasing.
    # Valid range for i is [k, n - k - 1]
    for i in range(k, n - k):
        if inc[i - 1] >= k and dec[i + 1] >= k:
            result.append(i)

    return result
```
</details>
