# Minimum Operations to Make Array Equal to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3229 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-array-equal-to-target](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/).

### Goal
Given two integer arrays `nums` and `target` of the same length, calculate the minimum number of operations required to transform `nums` into `target`. An operation consists of choosing a subarray and incrementing or decrementing all elements within that subarray by 1. Crucially, you can only perform increment operations on a subarray if all elements in that subarray are currently less than their corresponding target values, and decrement operations if all are greater.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the starting state.
- `target`: A list of integers representing the desired state.

**Return value**

- An integer representing the minimum total operations required to reach the target state.

### Examples
**Example 1**

- Input: `nums = [3, 5, 1, 2]`, `target = [4, 6, 2, 4]`
- Output: `2`

**Example 2**

- Input: `nums = [1, 3, 2]`, `target = [2, 1, 4]`
- Output: `5`

**Example 3**

- Input: `nums = [0, 0, 0]`, `target = [1, 2, 3]`
- Output: `3`

---

## Solution
### Approach
The problem can be reduced to analyzing the difference array `diff[i] = target[i] - nums[i]`. The goal is to transform the `diff` array into an array of zeros using range increment/decrement operations. By observing the differences between adjacent elements in `diff`, we can apply a greedy strategy: we accumulate the positive increments and negative decrements separately. If the current difference and the previous difference share the same sign, we can extend the previous operation; otherwise, we must start a new operation.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input arrays, as we perform a single linear pass to calculate differences and accumulate operations.
- **Space Complexity**: `O(1)` (excluding input storage), as we only maintain a few variables to track the state of the previous difference and the running totals.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], target: list[int]) -> int:
    """
    Calculates the minimum operations to transform nums to target.
    We define diff[i] = target[i] - nums[i].
    We want to reach an array of all zeros.
    This is equivalent to the classic problem of making an array zero
    using range increments/decrements.
    """
    n = len(nums)
    diff = [target[i] - nums[i] for i in range(n)]

    total_ops = 0
    inc = 0  # Current accumulated positive operations
    dec = 0  # Current accumulated negative operations

    for d in diff:
        if d > 0:
            if d > inc:
                total_ops += (d - inc)
            inc = d
            dec = 0
        elif d < 0:
            if d < dec:
                total_ops += (dec - d)
            dec = d
            inc = 0
        else:
            inc = 0
            dec = 0

    return total_ops
```
</details>
