# Count Number of Distinct Integers After Reverse Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2442 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Number of Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. For each integer in the original array, reverse the order of its decimal digits and append the resulting integer to the array. Apply this operation only to the original entries, not recursively to values that have just been appended.

Leading zeros in a reversed digit sequence do not remain in its integer value; for example, reversing 10 produces `01`, which represents 1. After all original values and their reversals are present, return the number of distinct integers in the final array.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- The number of distinct integers among all original values and the digit reversal of each original value.

### Examples

#### Example 1

- **Input:** `nums = [1, 13, 10, 12, 31]`
- **Output:** `6`
- **Explanation:** The reversals are `[1, 31, 1, 21, 13]`; the distinct final values are 1, 10, 12, 13, 21, and 31.

#### Example 2

- **Input:** `nums = [2, 2, 2]`
- **Output:** `1`
- **Explanation:** Every original value and every reversal equals 2.
