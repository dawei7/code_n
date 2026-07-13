# Count the Number of Inversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3193 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-the-number-of-inversions](https://leetcode.com/problems/count-the-number-of-inversions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-the-number-of-inversions/).

### Goal
Given an integer `n` representing the length of a permutation of numbers from `0` to `n-1`, and a list of constraints `requirements`, calculate the total number of permutations that satisfy all given conditions. Each condition `(end, cnt)` specifies that the prefix of the permutation ending at index `end` must contain exactly `cnt` inversions.

### Function Contract
**Inputs**

- `n`: An integer representing the length of the permutation.
- `requirements`: A list of lists, where each inner list `[end, cnt]` defines a constraint on the number of inversions for the prefix of length `end + 1`.

**Return value**

- An integer representing the total number of valid permutations modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `n = 3, requirements = [[2, 2]]`
- Output: `2`
- Explanation: The permutations of [0, 1, 2] with 2 inversions are [1, 2, 0] and [2, 0, 1].

**Example 2**

- Input: `n = 2, requirements = [[0, 0], [1, 0]]`
- Output: `1`
- Explanation: Only [0, 1] satisfies both constraints.

**Example 3**

- Input: `n = 2, requirements = [[0, 0], [1, 1]]`
- Output: `1`
- Explanation: Only [1, 0] satisfies both constraints.

---

## Solution
### Approach
The problem is solved using Dynamic Programming. Let `dp[i][j]` be the number of permutations of length `i` with exactly `j` inversions. The recurrence relation is `dp[i][j] = sum(dp[i-1][j-k])` for `0 <= k < i`. This can be optimized using a sliding window sum (prefix sums) to achieve O(n * max_inversions) time complexity. Constraints are handled by resetting the DP state at each `end` index to only include the required inversion count.

### Complexity Analysis
- **Time Complexity**: `O(n * max_inversions)`, where `n` is the length of the permutation and `max_inversions` is at most `n*(n-1)/2`.
- **Space Complexity**: `O(max_inversions)` using space-optimized DP arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, requirements: list[list[int]]) -> int:
    MOD = 10**9 + 7

    # Map requirements for quick lookup
    req_map = {}
    max_inv = 0
    for end, cnt in requirements:
        req_map[end] = cnt
        max_inv = max(max_inv, cnt)

    # dp[j] stores the number of permutations of current length with j inversions
    dp = [0] * (max_inv + 1)
    dp[0] = 1

    for i in range(n):
        new_dp = [0] * (max_inv + 1)

        # Prefix sum array to optimize the transition:
        # dp[i][j] = sum(dp[i-1][j-k]) for 0 <= k < i
        prefix_sum = [0] * (max_inv + 2)
        for j in range(max_inv + 1):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MOD

        for j in range(max_inv + 1):
            # The number of inversions we can add by placing the current element
            # at position i is between 0 and i.
            # So we sum dp[i-1] from j-i to j.
            lower = max(0, j - i)
            new_dp[j] = (prefix_sum[j + 1] - prefix_sum[lower]) % MOD

        # Apply constraints if they exist for the current index i
        if i in req_map:
            target = req_map[i]
            for j in range(max_inv + 1):
                if j != target:
                    new_dp[j] = 0

        dp = new_dp

    return dp[req_map.get(n - 1, 0)] % MOD
```
</details>
