# Minimum Moves to Pick K Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3086 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sliding Window, Prefix Sum |
| Official Link | [minimum-moves-to-pick-k-ones](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/) |

## Problem Description & Examples
### Goal
Given a binary array `nums` and integers `k` and `maxChanges`, determine the minimum number of operations required to collect `k` ones. An operation consists of either moving a one to an adjacent index or changing a zero to a one. You are allowed at most `maxChanges` operations to flip zeros to ones. When moving a one, the cost is the absolute difference between the current and target indices.

### Function Contract
**Inputs**

- `nums`: A list of integers containing only 0s and 1s.
- `k`: The total number of ones to collect.
- `maxChanges`: The maximum number of zeros that can be converted into ones.

**Return value**

- An integer representing the minimum total moves required to gather `k` ones.

### Examples
**Example 1**

- Input: `nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1`
- Output: `3`

**Example 2**

- Input: `nums = [0,0,0,0], k = 2, maxChanges = 3`
- Output: `4`

**Example 3**

- Input: `nums = [1,0,0,0,0,1], k = 2, maxChanges = 0`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem is solved by combining three strategies:
1. **Direct Conversion**: If `maxChanges` is sufficient, we can convert zeros to ones adjacent to existing ones.
2. **Sliding Window**: For existing ones, we use a sliding window of size `k` to find the optimal cluster. The cost to move all ones in a window to the median position is calculated efficiently using prefix sums.
3. **Greedy Selection**: We prioritize using `maxChanges` to flip zeros that are immediately adjacent to the target window, as these cost only 1 move each.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the length of the array. We iterate through the array to collect indices of ones and use prefix sums to calculate window costs in constant time.
- **Space Complexity**: `O(N)` to store the indices of the ones present in the input array.
