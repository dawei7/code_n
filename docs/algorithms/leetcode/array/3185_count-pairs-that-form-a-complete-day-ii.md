# Count Pairs That Form a Complete Day II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3185 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [count-pairs-that-form-a-complete-day-ii](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers representing durations in hours, determine the total number of pairs (i, j) such that i < j and the sum of the durations at these indices is exactly divisible by 24.

### Function Contract
**Inputs**

- `hours`: A list of integers where each element represents a duration in hours.

**Return value**

- An integer representing the total count of valid pairs whose sum is a multiple of 24.

### Examples
**Example 1**

- Input: `hours = [12, 12, 30, 24, 24]`
- Output: `2`
- Explanation: The pairs are (0, 1) where 12+12=24, and (3, 4) where 24+24=48.

**Example 2**

- Input: `hours = [72, 48, 24, 5]`
- Output: `3`
- Explanation: The pairs are (0, 1), (0, 2), and (1, 2). All sums are multiples of 24.

**Example 3**

- Input: `hours = [1, 2, 3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem utilizes the **Modular Arithmetic** property: $(a + b) \pmod{24} = 0$ if and only if $(a \pmod{24} + b \pmod{24}) \pmod{24} = 0$. By maintaining a frequency array (or hash map) of remainders encountered so far, we can count valid pairs in a single pass. For each duration $h$, we look for the complement remainder $r' = (24 - (h \pmod{24})) \pmod{24}$ already stored in our frequency map.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, because the frequency array size is fixed at 24, regardless of the input size.
