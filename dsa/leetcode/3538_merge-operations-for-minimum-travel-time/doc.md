# Merge Operations for Minimum Travel Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3538 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [merge-operations-for-minimum-travel-time](https://leetcode.com/problems/merge-operations-for-minimum-travel-time/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/merge-operations-for-minimum-travel-time/).

### Goal
Given an array of integers representing travel times between consecutive points, you are allowed to merge adjacent elements into their sum. The objective is to perform the minimum number of merge operations such that the resulting array becomes non-decreasing.

### Function Contract
**Inputs**

- `nums`: A list of positive integers representing the travel times.

**Return value**

- An integer representing the minimum number of merge operations required to make the array non-decreasing.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [4, 3, 2, 1]`
- Output: `3`

**Example 3**

- Input: `nums = [1, 2, 3, 1]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a Greedy approach combined with a backward traversal. By iterating from the end of the array to the beginning, we maintain the value of the "current segment" that must be less than or equal to the next segment to the right. If the current segment is too large, we merge it with its left neighbor until the condition is satisfied.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array once.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the current state.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    """
    To make the array non-decreasing with minimum merges, we process the array
    from right to left. We keep track of the value of the current segment
    (the rightmost segment of the suffix we are considering) and ensure that
    the segment to its left is smaller than or equal to it.
    """
    n = len(nums)
    if n <= 1:
        return 0

    merges = 0
    # current_val represents the value of the segment we are currently comparing against
    current_val = nums[-1]
    # current_sum represents the sum of the segment we are currently building
    current_sum = 0

    # Iterate backwards from the second to last element
    for i in range(n - 2, -1, -1):
        current_sum += nums[i]

        if current_sum <= current_val:
            # We found a valid segment, update current_val and reset current_sum
            current_val = current_sum
            current_sum = 0
        else:
            # We must merge the current element with the next one
            merges += 1

    return merges
```
</details>
