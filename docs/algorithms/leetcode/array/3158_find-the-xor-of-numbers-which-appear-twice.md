# Find the XOR of Numbers Which Appear Twice

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3158 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation |
| Official Link | [find-the-xor-of-numbers-which-appear-twice](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/) |

## Problem Description & Examples
### Goal
Given an array of integers where each number appears either once or twice, identify all numbers that occur exactly twice and compute their bitwise XOR sum. If no numbers appear twice, the result should be zero.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where each element is between 1 and 50.

**Return value**

- An integer representing the XOR sum of all elements that appear exactly twice in the input array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 3]`
- Output: `1`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 2, 1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem utilizes a frequency tracking mechanism, typically implemented via a Hash Set or a frequency array. By iterating through the input, we track seen elements; when an element is encountered for the second time, it is identified as a duplicate and included in the running XOR calculation.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass over the data.
- **Space Complexity**: `O(n)` in the worst case to store the set of seen numbers, or `O(1)` if considering the fixed constraint (numbers are between 1 and 50).
