# Maximum Good Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3026 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-good-subarray-sum](https://leetcode.com/problems/maximum-good-subarray-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-good-subarray-sum/).

### Goal
Given an integer array `nums` and an integer `k`, identify the maximum sum of a "good" subarray. A subarray is considered "good" if the absolute difference between its first and last elements is exactly `k`. If no such subarray exists, return 0.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: A non-negative integer representing the required absolute difference.

**Return value**

- An integer representing the maximum sum of a good subarray, or 0 if none exist.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5, 6], k = 1`
- Output: `11`
- Explanation: The subarray `[5, 6]` has a sum of 11, and `|5 - 6| = 1`.

**Example 2**

- Input: `nums = [-1, 3, 2, 4, 5], k = 3`
- Output: `11`
- Explanation: The subarray `[-1, 3, 2, 4, 5]` has a sum of 13, but the subarray `[2, 5]` has a sum of 7. The subarray `[-1, 2]` has a sum of 1 and `|-1 - 2| = 3`. The subarray `[2, 5]` is not valid, but `[2, 5]` is not the only option. The subarray `[2, 4, 5]` is not valid. The subarray `[-1, 3, 2]` is valid.

**Example 3**

- Input: `nums = [-10, 12, -20, -8, 15], k = 25`
- Output: `20`
- Explanation: The subarray `[-10, 12, -20, -8, 15]` has a sum of -11. The subarray `[-20, 5]` is not possible. The subarray `[-10, 15]` has a sum of 5. The subarray `[-20, 5]` is not possible. The subarray `[-20, -8, 15]` has a sum of -13. The subarray `[-10, 15]` is valid.

---

## Solution
### Approach
The problem is solved using a **Prefix Sum** approach combined with a **Hash Map**. We maintain a running prefix sum and store the minimum prefix sum encountered so far for each unique value in the array. For every element `x` at index `i`, we check if `x - k` or `x + k` has been seen before. If so, we calculate the potential subarray sum using the current prefix sum and the stored minimum prefix sum associated with the target value.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array once and perform constant-time hash map lookups.
- **Space Complexity**: `O(n)`, as we store at most `n` unique elements and their corresponding minimum prefix sums in the hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    # min_prefix_sums stores the minimum prefix sum encountered for each value
    # prefix_sum[i] is the sum of nums[0...i-1]
    # The sum of subarray nums[i...j] is prefix_sum[j+1] - prefix_sum[i]

    min_prefix_sums = {}
    current_prefix_sum = 0
    max_sum = float('-inf')
    found = False

    for x in nums:
        # Check for x - k
        target1 = x - k
        if target1 in min_prefix_sums:
            found = True
            max_sum = max(max_sum, current_prefix_sum + x - min_prefix_sums[target1])

        # Check for x + k
        target2 = x + k
        if target2 in min_prefix_sums:
            found = True
            max_sum = max(max_sum, current_prefix_sum + x - min_prefix_sums[target2])

        # Update the min prefix sum for the current value x
        # We store the prefix sum *before* adding x
        if x not in min_prefix_sums or current_prefix_sum < min_prefix_sums[x]:
            min_prefix_sums[x] = current_prefix_sum

        current_prefix_sum += x

    return int(max_sum) if found else 0
```
</details>
