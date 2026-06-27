# Maximum Number of Operations With the Same Score I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3038 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [maximum-number-of-operations-with-the-same-score-i](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, perform a sequence of operations where each operation removes the first two elements of the array. An operation is valid only if the sum of the two removed elements equals the sum of the two elements removed in the very first operation. The goal is to determine the maximum number of operations that can be performed until the condition is no longer met or there are fewer than two elements remaining.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is always even.

**Return value**

- An integer representing the total count of valid operations performed.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 4]`
- Output: `2`
- Explanation: First op: 3+2=5. Second op: 1+4=5. Both match, total 2.

**Example 2**

- Input: `nums = [3, 2, 6, 1, 4]`
- Output: `1`
- Explanation: First op: 3+2=5. Second op: 6+1=7. 7 != 5, stop.

**Example 3**

- Input: `nums = [1, 1, 1, 1, 1, 1]`
- Output: `3`
- Explanation: All pairs sum to 2.

---

## Underlying Base Algorithm(s)
Simulation using a greedy approach. Since the problem requires the sum of every subsequent pair to match the sum of the first pair, we simply calculate the target sum once and iterate through the array in steps of two, incrementing a counter until the condition fails or the array is exhausted.

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we traverse the array at most once.
- **Space Complexity**: O(1), as we only store the target sum and the operation counter.
