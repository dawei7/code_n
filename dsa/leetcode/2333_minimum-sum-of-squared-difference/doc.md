# Minimum Sum of Squared Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2333 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-sum-of-squared-difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-sum-of-squared-difference/).

### Goal
Given two integer arrays, `nums1` and `nums2`, of equal length, and two non-negative integers, `k1` and `k2`. You are allowed to perform at most `k1` operations on `nums1` and at most `k2` operations on `nums2`. An operation consists of either incrementing or decrementing any element of an array by 1. The objective is to minimize the total sum of squared differences, `sum((nums1[i] - nums2[i])^2)` for all `i`, after applying the allowed operations.

### Function Contract
**Inputs**

- `nums1`: A list of integers, representing the first array. Its length `n` is between 1 and 10^5. Each element `nums1[i]` is between 1 and 10^5.
- `nums2`: A list of integers of the same length `n` as `nums1`, representing the second array. Each element `nums2[i]` is between 1 and 10^5.
- `k1`: A non-negative integer representing the maximum total operations allowed on `nums1`. `k1` is between 0 and 10^9.
- `k2`: A non-negative integer representing the maximum total operations allowed on `nums2`. `k2` is between 0 and 10^9.

**Return value**

- An integer representing the minimum possible sum of squared differences after performing at most `k1 + k2` operations.

### Examples
**Example 1**

- Input: `nums1 = [1,2,3,4]`, `nums2 = [2,3,4,5]`, `k1 = 1`, `k2 = 1`
- Output: `2`
- Explanation: Initial differences are `[1,1,1,1]`. Total operations `k = k1 + k2 = 2`. We can reduce two of the `1`s to `0`s. The remaining differences are `[0,0,1,1]`. Sum of squares: `0^2 + 0^2 + 1^2 + 1^2 = 2`.

**Example 2**

- Input: `nums1 = [1,1,1,1,1]`, `nums2 = [10,10,10,10,10]`, `k1 = 0`, `k2 = 0`
- Output: `405`
- Explanation: Total operations `k = 0`. No changes can be made. Initial differences are `[9,9,9,9,9]`. Sum of squares: `5 * 9^2 = 5 * 81 = 405`.

**Example 3**

- Input: `nums1 = [7,10,8,10,3,10,3,5]`, `nums2 = [1,2,1,1,1,1,1,1]`, `k1 = 10`, `k2 = 10`
- Output: `97`
- Explanation: Initial absolute differences are `[6, 8, 7, 9, 2, 9, 2, 4]`. Total operations `k = k1 + k2 = 20`.
  The frequency of differences is: `2:2, 4:1, 6:1, 7:1, 8:1, 9:2`.
  Applying 20 operations greedily from largest differences:
  - Reduce two `9`s to `8`s (cost 2, `k=18`). Freq: `2:2, 4:1, 6:1, 7:1, 8:3`.
  - Reduce three `8`s to `7`s (cost 3, `k=15`). Freq: `2:2, 4:1, 6:1, 7:4`.
  - Reduce four `7`s to `6`s (cost 4, `k=11`). Freq: `2:2, 4:1, 6:5`.
  - Reduce five `6`s to `5`s (cost 5, `k=6`). Freq: `2:2, 4:1, 5:5`.
  - Reduce five `5`s to `4`s (cost 5, `k=1`). Freq: `2:2, 4:6`.
  - Reduce one `4` to `3` (cost 1, `k=0`). Freq: `2:2, 3:1, 4:5`.
  Final sum of squares: `2*2^2 + 1*3^2 + 5*4^2 = 2*4 + 1*9 + 5*16 = 8 + 9 + 80 = 97`.

---

## Solution
### Approach
The core idea relies on a **Greedy** strategy. To minimize the sum of squared differences, `sum(d_i^2)`, where `d_i = |nums1[i] - nums2[i]|`, it is always optimal to reduce the largest absolute differences first. This is because reducing a larger number `X` by 1 (to `X-1`) yields a greater reduction in `X^2` (which is `X^2 - (X-1)^2 = 2X - 1`) than reducing a smaller number `Y` by 1 (which is `2Y - 1`), given `X > Y`.

Since the total number of operations (`k1 + k2`) can be very large (`2 * 10^9`), but the maximum possible absolute difference between elements is relatively small (`10^5 - 1`), a **Frequency Array** (similar to a counting sort approach) is the most efficient way to manage and apply operations to the differences. Instead of using a priority queue (heap) which would be `O(K log N)` in the worst case, a frequency array allows processing differences in `O(MaxDiff)` time, where `MaxDiff` is the maximum possible absolute difference.

The algorithm proceeds as follows:
1.  Combine `k1` and `k2` into a single `total_k`.
2.  Calculate the absolute differences `|nums1[i] - nums2[i]|` for all `i`.
3.  Store the frequencies of these differences in a frequency array (e.g., `counts[d]` stores how many times difference `d` appears). Also, track the maximum difference observed.
4.  Iterate downwards from the maximum observed difference to `1`. For each difference `d`:
    *   If there are items with difference `d` and `total_k > 0`:
    *   Determine how many operations are needed to reduce all `counts[d]` items by one (i.e., `counts[d]` operations).
    *   If `total_k` is greater than or equal to `counts[d]`, apply these operations: decrement `total_k` by `counts[d]`, and move all `counts[d]` items from `d` to `d-1` (by incrementing `counts[d-1]` by `counts[d]`).
    *   If `total_k` is less than `counts[d]`, apply the remaining `total_k` operations: decrement `total_k` by `total_k`, move `total_k` items from `d` to `d-1`, and then stop, as no more operations are available.
5.  After exhausting `total_k` operations, calculate the sum of squares of the remaining differences using the updated frequency array: `sum(counts[d] * d^2)`.

### Complexity Analysis
- **Time Complexity**: `O(N + MaxDiff)`.
    - Calculating initial differences and populating the frequency array takes `O(N)` time, where `N` is the length of `nums1` (and `nums2`).
    - Iterating through the frequency array from `MaxDiff` down to `0` takes `O(MaxDiff)` time, where `MaxDiff` is the maximum possible absolute difference (which is `10^5 - 1`).
    - Calculating the final sum of squares also takes `O(MaxDiff)` time.
    - Given `N <= 10^5` and `MaxDiff <= 10^5`, the overall time complexity is dominated by `O(N + MaxDiff)`.
- **Space Complexity**: `O(MaxDiff)`.
    - A frequency array of size `MaxDiff + 1` is used to store the counts of differences. This is `O(10^5)` space.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections

def solve(nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
    n = len(nums1)
    total_k = k1 + k2

    # Max possible difference is 10^5 - 1 = 99999.
    # An array of size 100001 is sufficient for counts (indices 0 to 100000).
    MAX_DIFF_VAL = 100000
    counts = [0] * (MAX_DIFF_VAL + 1)

    max_current_diff = 0
    for i in range(n):
        diff = abs(nums1[i] - nums2[i])
        counts[diff] += 1
        if diff > max_current_diff:
            max_current_diff = diff

    # Greedily reduce the largest differences
    # Iterate from the largest observed difference down to 1
    for d in range(max_current_diff, 0, -1):
        if total_k == 0:
            break # No operations left

        if counts[d] > 0:
            # Number of items with current difference 'd'
            num_items_at_d = counts[d]

            # If we have enough operations to reduce all these items by 1
            if total_k >= num_items_at_d:
                total_k -= num_items_at_d
                counts[d-1] += num_items_at_d
                counts[d] = 0 # All items at 'd' moved to 'd-1'
            else:
                # We only have 'total_k' operations left.
                # Reduce 'total_k' items from 'd' to 'd-1'.
                counts[d-1] += total_k
                counts[d] -= total_k
                total_k = 0 # No operations left
                break # Exit loop as no more operations

    # Calculate the final sum of squared differences
    min_sum_sq_diff = 0
    # Iterate through all possible differences (from 0 up to max_current_diff, or MAX_DIFF_VAL)
    # Using max_current_diff as upper bound is slightly more efficient if max_current_diff is small.
    # Using MAX_DIFF_VAL is also correct and safe.
    for d in range(max_current_diff + 1):
        if counts[d] > 0:
            min_sum_sq_diff += counts[d] * d * d

    return min_sum_sq_diff
```
</details>
