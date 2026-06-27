# Count the Number of Inversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3193 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [count-the-number-of-inversions](https://leetcode.com/problems/count-the-number-of-inversions/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. Let `dp[i][j]` be the number of permutations of length `i` with exactly `j` inversions. The recurrence relation is `dp[i][j] = sum(dp[i-1][j-k])` for `0 <= k < i`. This can be optimized using a sliding window sum (prefix sums) to achieve O(n * max_inversions) time complexity. Constraints are handled by resetting the DP state at each `end` index to only include the required inversion count.

---

## Complexity Analysis
- **Time Complexity**: `O(n * max_inversions)`, where `n` is the length of the permutation and `max_inversions` is at most `n*(n-1)/2`.
- **Space Complexity**: `O(max_inversions)` using space-optimized DP arrays.
