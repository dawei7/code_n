# Maximum Number of Distinct Elements After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3397 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-distinct-elements-after-operations](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/).

### Goal
Given an array of integers and a range parameter `k`, you are allowed to modify each element `nums[i]` by replacing it with any value in the range `[nums[i] - k, nums[i] + k]`. The objective is to maximize the total number of unique elements in the resulting array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial values.
- `k`: An integer representing the maximum allowed deviation for each element.

**Return value**

- An integer representing the maximum possible count of distinct elements achievable after performing the allowed operations on each element.

### Examples
**Example 1**

- Input: `nums = [1, 2, 2, 3, 3, 4], k = 2`
- Output: `6`

**Example 2**

- Input: `nums = [4, 4, 4, 4], k = 1`
- Output: `3`

**Example 3**

- Input: `nums = [1, 1, 1, 1], k = 0`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Greedy approach combined with Sorting**. By sorting the input array, we can process elements in non-decreasing order. We maintain a variable `last_used` to track the smallest value assigned to the previous element. For each current element `nums[i]`, we attempt to pick the smallest possible value in its valid range `[nums[i] - k, nums[i] + k]` that is strictly greater than `last_used`. If the lower bound of the range is less than or equal to `last_used`, we pick `last_used + 1` (provided it is within the valid range). If `last_used + 1` exceeds the upper bound, we cannot make this element distinct from the previous ones, so we effectively "skip" it or assign it a value that doesn't contribute to the count.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where `N` is the length of the input array. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(N)`).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    """
    Maximizes the number of distinct elements by greedily picking the smallest
    available valid integer for each element in sorted order.
    """
    nums.sort()

    # last_used tracks the value assigned to the previous element
    # Initialize with a value smaller than any possible range start
    last_used = -float('inf')
    distinct_count = 0

    for x in nums:
        # The range for the current element is [x - k, x + k]
        lower_bound = x - k
        upper_bound = x + k

        # We want to pick the smallest value >= lower_bound that is > last_used
        # If last_used + 1 is within the valid range, we pick it.
        # Otherwise, we pick the lower_bound if it's > last_used.
        target = max(lower_bound, last_used + 1)

        if target <= upper_bound:
            distinct_count += 1
            last_used = target

    return distinct_count
```
</details>
