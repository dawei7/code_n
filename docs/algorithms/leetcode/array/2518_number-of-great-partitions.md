# Number of Great Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2518 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [number-of-great-partitions](https://leetcode.com/problems/number-of-great-partitions/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, determine the number of ways to partition the array into two non-empty subsets such that the sum of elements in each subset is at least `k`. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the elements to be partitioned.
- `k`: An integer representing the minimum sum threshold for each subset.

**Return value**

- An integer representing the total count of valid partitions modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4], k = 4`
- Output: `6`

**Example 2**

- Input: `nums = [3,3,3], k = 4`
- Output: `0`

**Example 3**

- Input: `nums = [6,6], k = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using the Principle of Inclusion-Exclusion combined with 0/1 Knapsack Dynamic Programming. 
1. Total ways to partition a set into two subsets is 2^n.
2. A partition is "bad" if at least one subset has a sum strictly less than `k`.
3. We calculate the number of subsets with sum `s < k` using DP.
4. The final answer is (Total - 2 * (subsets with sum < k)) % MOD, accounting for the fact that both subsets must be non-empty and satisfy the condition.

---

## Complexity Analysis
- **Time Complexity**: O(n * k), where n is the length of the array and k is the threshold. We iterate through the array and update a DP table of size k.
- **Space Complexity**: O(k), as we only need the current and previous states of the DP table to calculate the number of subsets with a specific sum.
