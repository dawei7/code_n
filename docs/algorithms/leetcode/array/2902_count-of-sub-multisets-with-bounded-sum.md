# Count of Sub-Multisets With Bounded Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2902 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming, Sliding Window |
| Official Link | [count-of-sub-multisets-with-bounded-sum](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) |

## Problem Description & Examples
### Goal
Given a collection of integers (which may contain duplicates) and two bounds `l` and `r`, determine the total number of sub-multisets whose elements sum to a value between `l` and `r` inclusive. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available elements.
- `l`: An integer representing the lower bound of the target sum.
- `r`: An integer representing the upper bound of the target sum.

**Return value**

- An integer representing the count of sub-multisets with a sum in the range `[l, r]` modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 2, 3], l = 6, r = 7`
- Output: `3`

**Example 2**

- Input: `nums = [2, 1, 4, 2, 7], l = 1, r = 5`
- Output: `7`

**Example 3**

- Input: `nums = [1, 2, 1, 2, 1], l = 3, r = 3`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is a variation of the Bounded Knapsack Problem. We use dynamic programming with a frequency map to group identical elements. To optimize the transition, we use a sliding window sum technique on the DP array to update counts in $O(r)$ time per distinct element, rather than the naive $O(r \times \text{count})$ approach.

---

## Complexity Analysis
- **Time Complexity**: $O(N + K \cdot R)$, where $N$ is the number of elements, $K$ is the number of distinct elements, and $R$ is the upper bound `r`.
- **Space Complexity**: $O(R)$ to store the DP table.
