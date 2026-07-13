# Maximum Strength of K Disjoint Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3077 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-strength-of-k-disjoint-subarrays](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/).

### Goal
Given an array of integers and an integer `k`, partition the array into exactly `k` disjoint subarrays such that the total "strength" is maximized. The strength of the partition is defined as the sum of the strengths of each subarray, where the strength of a subarray is the sum of its elements multiplied by `(k - i + 1)` if it is the `i`-th subarray (1-indexed) and `i` is odd, or multiplied by `-(k - i + 1)` if `i` is even.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the number of disjoint subarrays to form.

**Return value**

- An integer representing the maximum possible strength achievable.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, -1, 2], k = 3`
- Output: `22`
- Explanation: Subarrays could be [1, 2], [3], [-1, 2]. Strengths: (1+2)*3 + (3)*(-2) + (-1+2)*1 = 9 - 6 + 1 = 4. Optimal partition yields 22.

**Example 2**

- Input: `nums = [12, -2, -2, -2, -2], k = 5`
- Output: `64`

**Example 3**

- Input: `nums = [-1, -2, -3], k = 1`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with state optimization. We define `dp[i][j]` as the maximum strength using `i` subarrays considering the first `j` elements. To optimize space, we observe that the state only depends on the previous number of subarrays, allowing us to reduce space complexity to O(N). We use prefix sums to calculate subarray sums in O(1) time.

### Complexity Analysis
- **Time Complexity**: `O(k * n)`, where `n` is the length of the array, as we iterate through `k` subarrays and `n` elements.
- **Space Complexity**: `O(n)`, as we only store the current and previous DP states.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    neg_inf = -10**30
    best = [neg_inf] * (k + 1)
    ending = [neg_inf] * (k + 1)
    best[0] = 0

    for value in nums:
        for used in range(k, 0, -1):
            weight = k - used + 1
            if used % 2 == 0:
                weight = -weight
            contribution = weight * value
            ending[used] = max(
                ending[used] + contribution,
                best[used - 1] + contribution,
            )
            best[used] = max(best[used], ending[used])

    return best[k]
```
</details>
