# Smallest Missing Non-negative Integer After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2598 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Greedy |
| Official Link | [smallest-missing-non-negative-integer-after-operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `value`, you are allowed to repeatedly add or subtract `value` from any element in the array. The objective is to determine the smallest non-negative integer (MEX - Minimum Excluded value) that cannot be formed by any element in the array after performing any number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `value`: An integer representing the step size for allowed modifications.

**Return value**

- An integer representing the smallest non-negative integer that cannot be represented in the modified array.

### Examples
**Example 1**

- Input: `nums = [1, -10, 7, 13, 6, 8], value = 5`
- Output: `2`

**Example 2**

- Input: `nums = [1, -10, 7, 13, 6, 8], value = 7`
- Output: `3`

**Example 3**

- Input: `nums = [3, 0, 3, 2, 4, 2, 1, 1, 0, 4], value = 5`
- Output: `10`

---

## Underlying Base Algorithm(s)
The problem relies on modular arithmetic. Since we can add or subtract `value` infinitely, any number `x` is equivalent to `x % value`. We can map every number in the input to its remainder modulo `value`. By counting the frequency of each remainder, we can determine how many times each remainder class can "fill" a slot in the sequence 0, 1, 2, ... . We greedily fill the sequence by checking which remainder class has the fewest occurrences, effectively finding the first gap in the sequence.

---

## Complexity Analysis
- **Time Complexity**: `O(n + value)`, where `n` is the length of the input array. We iterate through the array once to count remainders and then iterate up to `value` to find the MEX.
- **Space Complexity**: `O(value)`, used to store the frequency counts of the remainders.
