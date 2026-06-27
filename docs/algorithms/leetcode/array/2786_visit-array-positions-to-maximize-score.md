# Visit Array Positions to Maximize Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2786 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [visit-array-positions-to-maximize-score](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) |

## Problem Description & Examples
### Goal
Given an array of integers and a penalty value, you start at the first element of the array. You must traverse the array from left to right, choosing a subsequence of indices starting at index 0. If you move from an element with a different parity (even vs. odd) to another, you incur a penalty. The objective is to maximize the total sum of the values of the chosen indices.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the values at each position.
- `x`: An integer representing the penalty incurred when switching between odd and even numbers.

**Return value**

- An integer representing the maximum possible score achievable by selecting a valid subsequence of indices.

### Examples
**Example 1**

- Input: `nums = [2, 3, 6, 1, 9, 2], x = 5`
- Output: `13`
- Explanation: We choose indices 0, 2, 4. Values: 2 + 6 + 9 = 17. Parity changes: 2(even) to 6(even) [no penalty], 6(even) to 9(odd) [penalty 5]. Total: 17 - 5 = 12. Alternatively, choosing 0, 1, 4 gives 2+3+9 - 5 - 5 = 4. The optimal path is 13.

**Example 2**

- Input: `nums = [2, 4, 6], x = 3`
- Output: `12`
- Explanation: All numbers are even, so no penalty is incurred. Sum = 2 + 4 + 6 = 12.

**Example 3**

- Input: `nums = [1], x = 2`
- Output: `1`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain two states: the maximum score ending with an even number and the maximum score ending with an odd number. For each new number, we update these states based on whether the current number is even or odd, considering the penalty `x` if the parity differs from the previous state.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store two variables to track the maximum scores for even and odd parities.
