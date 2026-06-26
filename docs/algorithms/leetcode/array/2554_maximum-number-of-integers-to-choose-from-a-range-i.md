# Maximum Number of Integers to Choose From a Range I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2554 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Greedy, Sorting |
| Official Link | [maximum-number-of-integers-to-choose-from-a-range-i](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/) |

## Problem Description & Examples
### Goal
Given a range of integers from 1 to `n` and a list of "banned" integers, determine the maximum count of unique integers you can select from the range such that no selected integer is in the banned list and the total sum of the selected integers does not exceed a specified limit `maxSum`.

### Function Contract
**Inputs**

- `banned`: A list of integers that cannot be chosen.
- `n`: An integer representing the upper bound of the range [1, n].
- `maxSum`: An integer representing the maximum allowable sum of chosen integers.

**Return value**

- An integer representing the maximum number of integers that can be picked under the given constraints.

### Examples
**Example 1**

- Input: `banned = [1, 6, 5], n = 5, maxSum = 6`
- Output: `2` (We can choose 2 and 4, which sum to 6.)

**Example 2**

- Input: `banned = [1, 2, 3, 4, 5, 6, 7], n = 8, maxSum = 1`
- Output: `0` (No integers can be chosen without exceeding the sum.)

**Example 3**

- Input: `banned = [11], n = 7, maxSum = 50`
- Output: `7` (We can choose all integers from 1 to 7, as their sum is 28, which is less than 50.)

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach**. By iterating through the range [1, n] in ascending order and skipping any numbers present in the banned set, we maximize the count of integers chosen while keeping the running sum as small as possible. A Hash Set is used for O(1) average-time lookups of banned numbers.

---

## Complexity Analysis
- **Time Complexity**: O(n + m), where n is the upper bound of the range and m is the number of elements in the banned list. We iterate up to n times and perform constant-time set lookups.
- **Space Complexity**: O(m), required to store the banned integers in a hash set for efficient lookup.
