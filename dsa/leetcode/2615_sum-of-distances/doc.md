# Sum of Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2615 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-distances](https://leetcode.com/problems/sum-of-distances/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-distances/).

### Goal
Given an array of integers, calculate for each element at index `i` the sum of absolute differences between `i` and all other indices `j` where the values at `i` and `j` are identical.

### Function Contract
**Inputs**

- `nums`: A list of integers where `1 <= nums.length <= 10^5`.

**Return value**

- A list of integers `arr` where `arr[i]` is the sum of distances for `nums[i]`.

### Examples
**Example 1**

- Input: `nums = [1, 3, 1, 1, 2]`
- Output: `[5, 0, 3, 4, 0]`

**Example 2**

- Input: `nums = [0, 5, 3]`
- Output: `[0, 0, 0]`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `[3, 2, 3]`

---

## Solution
### Approach
The problem is solved using a Hash Map to group indices by their corresponding values. For each group of indices, we use the Prefix Sum technique to calculate the sum of absolute differences in linear time. Specifically, for a sorted list of indices `idx_list`, the sum of distances for an index `idx_list[i]` is calculated as:
`(i * idx_list[i] - prefix_sum[i]) + ((total_sum - prefix_sum[i+1]) - (count - 1 - i) * idx_list[i])`.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the length of the input array. We iterate through the array once to group indices and once more to compute the sums.
- **Space Complexity**: `O(N)` to store the hash map of indices and the resulting array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n

    # Group indices by their values
    val_to_indices = defaultdict(list)
    for i, val in enumerate(nums):
        val_to_indices[val].append(i)

    # For each group, calculate the sum of distances using prefix sums
    for val in val_to_indices:
        indices = val_to_indices[val]
        m = len(indices)
        if m == 1:
            continue

        # Calculate prefix sums of the indices
        prefix_sums = [0] * (m + 1)
        for i in range(m):
            prefix_sums[i + 1] = prefix_sums[i] + indices[i]

        total_sum = prefix_sums[m]

        # For each index in the group, calculate the sum of distances
        # Sum = (i * current_idx - prefix_sum_before) +
        #       ((total_sum - prefix_sum_after) - (m - 1 - i) * current_idx)
        for i in range(m):
            current_idx = indices[i]

            left_sum = prefix_sums[i]
            right_sum = total_sum - prefix_sums[i + 1]

            left_count = i
            right_count = m - 1 - i

            dist_left = (left_count * current_idx) - left_sum
            dist_right = right_sum - (right_count * current_idx)

            ans[current_idx] = dist_left + dist_right

    return ans
```
</details>
