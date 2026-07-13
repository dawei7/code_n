# Adjacent Increasing Subarrays Detection I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3349 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [adjacent-increasing-subarrays-detection-i](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/).

### Goal
Determine if there exist two contiguous, non-overlapping subarrays of length `k` that are both strictly increasing and positioned immediately adjacent to each other in the input array.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the required length of each subarray.

**Return value**

- A boolean: `True` if two adjacent strictly increasing subarrays of length `k` exist, `False` otherwise.

### Examples
**Example 1**

- Input: `nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k = 3`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k = 2`
- Output: `True`

**Example 3**

- Input: `nums = [1, 2, 1, 2], k = 2`
- Output: `False`

---

## Solution
### Approach
The problem can be solved using a sliding window or a linear scan approach. We pre-calculate the length of the strictly increasing sequence ending at each index. Then, we iterate through the array to check if there exists an index `i` such that the increasing sequence ending at `i` has length at least `k`, and the increasing sequence starting at `i + 1` also has length at least `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a constant number of linear passes.
- **Space Complexity**: `O(n)` to store the lengths of increasing sequences, though this can be optimized to `O(1)` by tracking the current and previous increasing run lengths.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> bool:
    n = len(nums)
    if k == 1:
        # If k=1, we just need two adjacent elements, which is always possible
        # unless the array is too short. However, the problem implies
        # strictly increasing, and any two adjacent elements are "adjacent
        # increasing subarrays" if they are distinct.
        # Actually, for k=1, any two adjacent elements are increasing.
        return n >= 2

    # inc_len[i] stores the length of the strictly increasing subarray ending at i
    inc_len = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            inc_len[i] = inc_len[i - 1] + 1

    # We look for an index i such that:
    # 1. The subarray ending at i has length >= k
    # 2. The subarray starting at i+1 has length >= k
    # The subarray starting at i+1 has length >= k if the increasing
    # sequence starting at i+1 continues for at least k elements.

    # Precompute lengths of increasing sequences starting at i
    inc_start = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            inc_start[i] = inc_start[i + 1] + 1

    for i in range(n - k):
        # Check if subarray ending at i has length >= k
        # and subarray starting at i+1 has length >= k
        if inc_len[i] >= k and inc_start[i + 1] >= k:
            return True

    return False
```
</details>
