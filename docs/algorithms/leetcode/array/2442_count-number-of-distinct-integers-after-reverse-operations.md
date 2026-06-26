# Count Number of Distinct Integers After Reverse Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2442 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Counting |
| Official Link | [count-number-of-distinct-integers-after-reverse-operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) |

## Problem Description & Examples
### Goal
Given an array of integers, generate a new collection that includes every original integer plus the value obtained by reversing the digits of each original integer. The objective is to determine the total count of unique integers present in this combined collection.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the count of distinct values found after adding all reversed versions of the input numbers to the original set.

### Examples
**Example 1**

- Input: `nums = [1, 13, 10, 12, 31]`
- Output: `6`
- Explanation: Reversed values are [1, 31, 1, 21, 13]. Combined set: {1, 13, 10, 12, 31, 21}. Total count is 6.

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `1`
- Explanation: Reversed values are [2, 2, 2]. Combined set: {2}. Total count is 1.

**Example 3**

- Input: `nums = [71, 17]`
- Output: `2`
- Explanation: Reversed values are [17, 71]. Combined set: {71, 17}. Total count is 2.

---

## Underlying Base Algorithm(s)
The problem utilizes a **Hash Set** data structure to efficiently track unique elements. The core logic involves iterating through the input array, calculating the integer reversal using modulo and division arithmetic, and inserting both the original and reversed values into the set.

---

## Complexity Analysis
- **Time Complexity**: O(N * D), where N is the number of elements in the input array and D is the average number of digits in the integers. Reversing an integer takes time proportional to its number of digits.
- **Space Complexity**: O(N), as we store up to 2N integers in the hash set.
