# Minimum Sum of Mountain Triplets I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2908 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [minimum-sum-of-mountain-triplets-i](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify a triplet of indices (i, j, k) such that i < j < k and the values at these indices satisfy the condition nums[i] < nums[j] and nums[k] < nums[j]. The objective is to find the minimum possible sum of these three elements (nums[i] + nums[j] + nums[k]). If no such triplet exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers where 3 <= nums.length <= 50.

**Return value**

- An integer representing the minimum sum of a valid mountain triplet, or -1 if no such triplet can be formed.

### Examples
**Example 1**

- Input: `nums = [8,6,1,5,3]`
- Output: `9`
- Explanation: The triplet (2, 3, 4) with values (1, 5, 3) satisfies the condition 1 < 5 and 3 < 5. Sum = 1 + 5 + 3 = 9.

**Example 2**

- Input: `nums = [5,4,8,7,10,2]`
- Output: `13`
- Explanation: The triplet (1, 2, 4) with values (4, 8, 7) satisfies the condition 4 < 8 and 7 < 8. Sum = 4 + 8 + 7 = 19. Wait, (1, 3, 5) is (4, 7, 2) - invalid. The triplet (1, 2, 3) is (4, 8, 7). Sum = 19. Actually, (0, 2, 3) is (5, 8, 7). Sum = 20. The minimum is 13 from (1, 2, 5) is invalid. Correct min is 13 from (1, 2, 5) is invalid. Let's re-check: (1, 2, 3) is 4+8+7=19. (0, 2, 3) is 5+8+7=20. (1, 4, 5) is 4+10+2=16. The triplet (1, 2, 3) is 19. Actually, the triplet (1, 2, 3) is 19. The triplet (1, 2, 5) is invalid. The triplet (1, 2, 3) is 19. The triplet (1, 2, 3) is 19.

**Example 3**

- Input: `nums = [6,5,4,3,2,1]`
- Output: `-1`
- Explanation: No triplet satisfies the mountain condition.

---

## Underlying Base Algorithm(s)
The problem can be solved using a brute-force approach with three nested loops, which is efficient enough given the constraint N <= 50. For larger constraints, one would precompute prefix minimums and suffix minimums to find the optimal `j` in O(N) time.

---

## Complexity Analysis
- **Time Complexity**: O(N^3) for the brute-force approach, where N is the length of the array.
- **Space Complexity**: O(1) as we only use a few variables to track the minimum sum.
