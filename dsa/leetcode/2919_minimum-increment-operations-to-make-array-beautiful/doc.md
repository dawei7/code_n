# Minimum Increment Operations to Make Array Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2919 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-increment-operations-to-make-array-beautiful](https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/).

### Goal
Given an array of non-negative integers and a threshold `k`, determine the minimum total increment operations required such that every contiguous subarray of length 3 contains at least one element greater than or equal to `k`. An increment operation consists of increasing any element in the array by 1.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: An integer representing the minimum threshold value.

**Return value**

- An integer representing the minimum total increments needed to satisfy the condition.

### Examples
**Example 1**

- Input: `nums = [2, 3, 0, 0, 2], k = 4`
- Output: `3`

**Example 2**

- Input: `nums = [0, 1, 3, 3], k = 5`
- Output: `2`

**Example 3**

- Input: `nums = [1, 1, 2], k = 1`
- Output: `0`

---

## Solution
### Approach
Dynamic Programming. We maintain a state representing the minimum cost to satisfy the condition up to index `i`, considering the "distance" to the last element that was made $\ge k$. Specifically, we track the minimum cost to have the last element $\ge k$ at index `i`, `i-1`, or `i-2`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array once with constant time transitions.
- **Space Complexity**: `O(1)`, as we only store the costs for the last three positions.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    # dp[i] stores the minimum increments to make the subarray ending at i valid,
    # where nums[i] is the element that was increased to be >= k.
    # We only need the last 3 states to calculate the next state.

    n = len(nums)
    # dp[i] = max(0, k - nums[i]) + min(dp[i-1], dp[i-2], dp[i-3])
    # Initialize with the first three elements
    dp = [0] * n

    for i in range(n):
        cost = max(0, k - nums[i])
        if i < 3:
            dp[i] = cost
        else:
            dp[i] = cost + min(dp[i-1], dp[i-2], dp[i-3])

    # The answer is the minimum of the last three positions,
    # because the last window of 3 must contain at least one element >= k.
    return min(dp[n-1], dp[n-2], dp[n-3])
```
</details>
