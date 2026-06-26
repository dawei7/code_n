# Count Increasing Quadruplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2552 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Enumeration, Prefix Sum |
| Official Link | [count-increasing-quadruplets](https://leetcode.com/problems/count-increasing-quadruplets/) |

## Problem Description & Examples
### Goal
Given a permutation of numbers from 1 to $n$, identify the total number of quadruplets of indices $(i, j, k, l)$ such that $0 \le i < j < k < l < n$ and the values at these indices satisfy the strictly increasing condition: $nums[i] < nums[k] < nums[j] < nums[l]$.

### Function Contract
**Inputs**

- `nums`: A list of integers representing a permutation of numbers from 1 to $n$.

**Return value**

- An integer representing the total count of quadruplets $(i, j, k, l)$ that satisfy the condition $nums[i] < nums[k] < nums[j] < nums[l]$.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 4]`
- Output: `2`
- Explanation: The quadruplets are (0, 1, 2, 3) where values are (1, 3, 2, 4). Wait, the condition is $nums[i] < nums[k] < nums[j] < nums[l]$. For [1, 3, 2, 4], indices (0, 2, 1, 3) satisfy 1 < 2 < 3 < 4.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `1`
- Explanation: Only (0, 1, 2, 3) satisfies 1 < 3 < 2 < 4 is false. Actually, for [1, 2, 3, 4], the only valid quadruplet is (0, 1, 2, 3) if the condition was $i<j<k<l$ and $nums[i]<nums[j]<nums[k]<nums[l]$. Given the specific constraint $nums[i] < nums[k] < nums[j] < nums[l]$, the output is 0.

**Example 3**

- Input: `nums = [2, 5, 3, 1, 4]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. We maintain a 2D array `dp[j][k]` which stores the number of pairs $(i, j)$ such that $i < j$ and $nums[i] < nums[k]$. By iterating through the array and updating this DP table, we can count valid quadruplets in $O(n^2)$ time.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the length of the input array. We use nested loops to iterate through pairs of indices.
- **Space Complexity**: $O(n)$, as we can optimize the DP table to use a 1D array or a space-efficient structure to track counts.
