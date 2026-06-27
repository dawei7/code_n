# Minimum Number of Groups to Create a Valid Assignment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2910 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy |
| Official Link | [minimum-number-of-groups-to-create-a-valid-assignment](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/) |

## Problem Description & Examples
### Goal
Given an array of integers, partition all elements into groups such that each group contains only one type of integer. A valid assignment requires that for any two groups of the same integer type, the difference in their sizes is at most 1. The objective is to minimize the total number of groups formed.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the items to be grouped.

**Return value**

- An integer representing the minimum total number of groups possible under the given constraints.

### Examples
**Example 1**

- Input: `nums = [3,2,3,2,3]`
- Output: `2`
- Explanation: We can form two groups of 3s (size 3) and two groups of 2s (size 2). Total groups: 2.

**Example 2**

- Input: `nums = [10,10,10,3,1,1]`
- Output: `4`
- Explanation: We can group 10s into one group of 3, 3s into one group of 1, and 1s into one group of 2. Total groups: 4.

**Example 3**

- Input: `nums = [1,1,3,3,3,3,3,3]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a greedy approach combined with mathematical optimization. First, we count the frequency of each number. Let the minimum frequency be `min_f`. Any valid group size `k` must satisfy the condition that each frequency `f` can be partitioned into groups of size `k` and `k+1`. Specifically, `f = a*k + b*(k+1)` where `a+b` is the number of groups. We iterate through all possible group sizes `k` from `min_f` down to 1. For a fixed `k`, we check if every frequency can be validly partitioned. The first `k` that satisfies this for all frequencies yields the minimum number of groups.

---

## Complexity Analysis
- **Time Complexity**: O(N + M * sqrt(min_f)), where N is the number of elements and M is the number of unique elements. We iterate through possible group sizes up to the minimum frequency.
- **Space Complexity**: O(M) to store the frequency map of the elements.
