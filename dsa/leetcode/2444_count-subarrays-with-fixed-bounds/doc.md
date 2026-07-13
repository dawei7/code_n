# Count Subarrays With Fixed Bounds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2444 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-subarrays-with-fixed-bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/).

### Goal
Given an integer array and two boundary values, determine the total number of contiguous subarrays where the minimum element is exactly equal to `minK` and the maximum element is exactly equal to `maxK`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `minK`: The required minimum value for the subarray.
- `maxK`: The required maximum value for the subarray.

**Return value**

- An integer representing the count of valid subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 3, 5, 2, 7, 5]`, `minK = 1`, `maxK = 5`
- Output: `2`

**Example 2**

- Input: `nums = [1, 1, 1, 1]`, `minK = 1`, `maxK = 1`
- Output: `10`

**Example 3**

- Input: `nums = [1, 2, 3]`, `minK = 1`, `maxK = 3`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Single-Pass Sliding Window** approach. We maintain three pointers (or indices) to track the state:
1. `bad_idx`: The index of the most recent element that falls outside the range `[minK, maxK]`.
2. `min_idx`: The index of the most recent occurrence of `minK`.
3. `max_idx`: The index of the most recent occurrence of `maxK`.

For every index `i` in the array, if `nums[i]` is within `[minK, maxK]`, the number of valid subarrays ending at `i` is `max(0, min(min_idx, max_idx) - bad_idx)`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only store a few integer pointers regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], min_k: int, max_k: int) -> int:
    ans = 0
    bad_idx = -1
    min_idx = -1
    max_idx = -1

    for i, x in enumerate(nums):
        # If the current number is outside the allowed range,
        # it resets the potential window.
        if not (min_k <= x <= max_k):
            bad_idx = i

        # Update the last seen positions of min_k and max_k
        if x == min_k:
            min_idx = i
        if x == max_k:
            max_idx = i

        # The number of valid subarrays ending at i is determined by the
        # distance between the closest boundary (min or max) and the
        # last 'bad' index.
        count = min(min_idx, max_idx) - bad_idx
        if count > 0:
            ans += count

    return ans
```
</details>
