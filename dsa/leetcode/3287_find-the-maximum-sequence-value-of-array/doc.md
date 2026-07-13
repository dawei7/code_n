# Find the Maximum Sequence Value of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3287 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-maximum-sequence-value-of-array](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/).

### Goal
Given an integer array `nums` and an integer `k`, identify two disjoint subsequences of length `k`. The objective is to maximize the bitwise XOR result of the bitwise OR of the first subsequence and the bitwise OR of the second subsequence.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 400 and 1 <= nums[i] <= 127.
- `k`: An integer representing the required length of each subsequence.

**Return value**

- An integer representing the maximum possible value of `(OR(subsequence1) ^ OR(subsequence2))`.

### Examples
**Example 1**

- Input: `nums = [1,2,1,3], k = 2`
- Output: `3`

**Example 2**

- Input: `nums = [5,7,8,9], k = 2`
- Output: `14`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with bitsets (or boolean arrays). Since the maximum value of elements is 127 (which is less than 2^7), the bitwise OR of any subsequence will always be in the range [0, 127]. We precompute all possible OR values for subsequences of length `k` starting from the left and ending at the right. Finally, we iterate through all possible split points to find the maximum XOR of the OR values from the left and right segments.

### Complexity Analysis
- **Time Complexity**: O(n * k * 128), where n is the length of the array. We compute DP states for each index up to k, and each state involves 128 possible OR values.
- **Space Complexity**: O(n * k * 128) to store the DP tables for all possible subsequence lengths up to k.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    n = len(nums)

    def get_possible_ors(arr):
        # dp[i][v] is true if a subsequence of length i can have OR value v
        dp = [[False] * 128 for _ in range(k + 1)]
        dp[0][0] = True
        for x in arr:
            for i in range(k - 1, -1, -1):
                for v in range(128):
                    if dp[i][v]:
                        dp[i + 1][v | x] = True
        return dp[k]

    # Precompute possible ORs for subsequences of length k ending at or before i
    # and starting at or after i
    left_dp = [[False] * 128 for _ in range(n)]
    right_dp = [[False] * 128 for _ in range(n)]

    # Forward pass
    curr_dp = [[False] * 128 for _ in range(k + 1)]
    curr_dp[0][0] = True
    for i in range(n):
        for j in range(k - 1, -1, -1):
            for v in range(128):
                if curr_dp[j][v]:
                    curr_dp[j + 1][v | nums[i]] = True
        for v in range(128):
            if curr_dp[k][v]:
                left_dp[i][v] = True

    # Backward pass
    curr_dp = [[False] * 128 for _ in range(k + 1)]
    curr_dp[0][0] = True
    for i in range(n - 1, -1, -1):
        for j in range(k - 1, -1, -1):
            for v in range(128):
                if curr_dp[j][v]:
                    curr_dp[j + 1][v | nums[i]] = True
        for v in range(128):
            if curr_dp[k][v]:
                right_dp[i][v] = True

    # Prefix/Suffix OR sets
    left_sets = [set() for _ in range(n)]
    right_sets = [set() for _ in range(n)]

    for i in range(n):
        for v in range(128):
            if left_dp[i][v]:
                left_sets[i].add(v)
            if i > 0:
                left_sets[i].update(left_sets[i-1])

    for i in range(n - 1, -1, -1):
        for v in range(128):
            if right_dp[i][v]:
                right_sets[i].add(v)
            if i < n - 1:
                right_sets[i].update(right_sets[i+1])

    ans = 0
    for i in range(k - 1, n - k):
        for l in left_sets[i]:
            for r in right_sets[i + 1]:
                ans = max(ans, l ^ r)

    return ans
```
</details>
