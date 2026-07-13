# Minimum Array Changes to Make Differences Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3224 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-array-changes-to-make-differences-equal](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/).

### Goal
Given an array of even length `nums` and an integer `k`, we want to make all pairs `(nums[i], nums[n-1-i])` have the same absolute difference `x` by modifying elements in the array. Each modification allows changing an element to any integer between `0` and `k` (inclusive). We need to find the minimum number of modifications required to achieve this target difference `x` for all pairs.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is even.
- `k`: An integer representing the upper bound for any element in the array.

**Return value**

- An integer representing the minimum number of modifications required to make all pairs have the same absolute difference.

### Examples
**Example 1**

- Input: `nums = [1, 0, 1, 2, 4, 3], k = 4`
- Output: `2`

**Example 2**

- Input: `nums = [0, 1, 2, 3], k = 3`
- Output: `1`

**Example 3**

- Input: `nums = [1, 1, 1, 1], k = 0`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a difference array (or sweep-line) technique combined with frequency counting. For each pair `(a, b)`, the maximum possible difference we can achieve with one change is `max(max(a, b), k - min(a, b))`. We count the occurrences of each possible difference `d = abs(a - b)`. Then, we use a difference array to track how many operations are needed for any target difference `x`. Specifically, for each pair, 0 changes are needed if `x == abs(a - b)`, 1 change is needed if `x <= max_diff`, and 2 changes are needed otherwise.

### Complexity Analysis
- **Time Complexity**: `O(n + k)`, where `n` is the length of the array and `k` is the maximum value allowed. We iterate through the array once and then iterate through the difference array of size `k`.
- **Space Complexity**: `O(k)`, used to store the frequency counts and the difference array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    # diff_counts stores the frequency of absolute differences of pairs
    diff_counts = [0] * (k + 1)
    # diff_array for sweep-line:
    # change_needed[x] = (count of pairs needing 2 changes) + (count of pairs needing 1 change)
    # We use a difference array to calculate this efficiently.
    # Base cost: every pair needs at least 1 change if target x != abs(a-b)
    # If x <= max_possible_diff, we can achieve it with 1 change.
    # If x > max_possible_diff, we need 2 changes.

    # diff_array[i] stores the change in the number of operations needed at difference i
    diff_array = [0] * (k + 2)

    for i in range(n // 2):
        a, b = nums[i], nums[n - 1 - i]
        diff = abs(a - b)
        diff_counts[diff] += 1

        # Max difference achievable with 1 change
        max_diff = max(max(a, b), k - min(a, b))

        # For a target x:
        # If x == diff: 0 changes
        # If x <= max_diff: 1 change
        # If x > max_diff: 2 changes

        # Start with 2 changes for all x.
        diff_array[0] += 2
        # If x <= max_diff, we only need 1 change.
        diff_array[0] -= 1
        diff_array[max_diff + 1] += 1
        # If x == diff, we need 0 changes (so subtract 1 more)
        diff_array[diff] -= 1
        diff_array[diff + 1] += 1

    min_ops = float('inf')
    current_ops = 0
    for x in range(k + 1):
        current_ops += diff_array[x]
        min_ops = min(min_ops, current_ops)

    return int(min_ops)
```
</details>
