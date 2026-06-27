# Count Almost Equal Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3267 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sorting, Counting, Enumeration |
| Official Link | [count-almost-equal-pairs-ii](https://leetcode.com/problems/count-almost-equal-pairs-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the number of pairs `(i, j)` such that `i < j` and the two numbers can be made equal by performing at most two "swap" operations on the digits of one of the numbers. A swap operation involves choosing two indices in the string representation of the number and swapping the digits at those positions.

### Function Contract
**Inputs**

- `nums`: A list of integers where each integer is between 1 and 1,000,000.

**Return value**

- An integer representing the total count of pairs `(i, j)` that satisfy the "almost equal" condition.

### Examples
**Example 1**

- Input: `nums = [1023, 2310]`
- Output: `1`
- Explanation: 1023 can become 2310 by swapping '1' with '2' and '0' with '3'.

**Example 2**

- Input: `nums = [1, 10, 30]`
- Output: `3`
- Explanation: (1, 10), (1, 30), and (10, 30) are all valid pairs after padding with leading zeros.

**Example 3**

- Input: `nums = [12, 12]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved by normalizing all numbers to the same string length (padding with leading zeros) and using a Hash Map to store the frequency of numbers encountered so far. For each number, we generate all possible variations reachable within two swaps. Since the maximum number of digits is 7, the number of permutations is small enough to generate efficiently. We use a set to store unique variations to avoid double-counting when checking against the frequency map.

## Complexity Analysis
- **Time Complexity**: `O(N * D^4)`, where `N` is the length of the input array and `D` is the maximum number of digits (7). Generating all variations within 2 swaps involves choosing 2 pairs of indices, which is roughly `O(D^4)`.
- **Space Complexity**: `O(N * D^4)` to store the frequency map of all possible variations for each number.
