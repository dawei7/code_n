# Maximum Number of Groups With Increasing Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2790 |
| Difficulty | Hard |
| Topics | Array, Math, Binary Search, Greedy, Sorting |
| Official Link | [maximum-number-of-groups-with-increasing-length](https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/) |

## Problem Description & Examples
### Goal
Given a collection of items with various counts, determine the maximum number of groups you can form such that each group has a strictly greater length than the previous one. Each group must consist of distinct items (i.e., you cannot use the same item more than once within a single group).

### Function Contract
**Inputs**

- `usageLimits`: A list of integers where `usageLimits[i]` represents the total number of times the $i$-th item can be used across all groups.

**Return value**

- An integer representing the maximum number of groups that can be formed.

### Examples
**Example 1**

- Input: `usageLimits = [1, 2, 5]`
- Output: `3`
- Explanation: We can form groups of sizes 1, 2, and 3.

**Example 2**

- Input: `usageLimits = [2, 1, 2, 1]`
- Output: `2`
- Explanation: We can form groups of sizes 1 and 2.

**Example 3**

- Input: `usageLimits = [1, 1]`
- Output: `1`
- Explanation: We can only form one group of size 1.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach combined with Sorting**. By sorting the `usageLimits` in non-decreasing order, we can greedily attempt to build groups of increasing size. We maintain a running count of available items and compare it against the required number of items needed to form the next group of size $k$. If the total number of items accumulated so far is sufficient to satisfy the requirement for a group of size $k$, we increment our group count.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the length of `usageLimits`, primarily due to the sorting step. The subsequent linear scan is $O(N)$.
- **Space Complexity**: $O(1)$ or $O(N)$ depending on the sorting implementation's space requirements.
