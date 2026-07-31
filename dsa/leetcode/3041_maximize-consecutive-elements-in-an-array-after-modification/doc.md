# Maximize Consecutive Elements in an Array After Modification

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3041 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/) |

## Problem Description
### Goal
You are given a 0-indexed array `nums` of positive integers. Before selecting any elements, you may increase each array element by at most `1`; every element is modified independently, so it may either keep its original value or increase by exactly `1`.

From the resulting array, select one or more elements. After the selected values are sorted in increasing order, they must be consecutive: every value after the first must be exactly one greater than its predecessor. Thus `[3,4,5]` is valid, whereas `[3,4,6]` has a gap and `[1,1,2,3]` contains a duplicate rather than being strictly consecutive.

Return the maximum possible number of selected elements.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: An array of positive integers with $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

Return the largest size of a subset that can be modified as allowed and then sorted into consecutive integers.

### Examples
**Example 1**

- Input: `nums = [2,1,5,1,1]`
- Output: `3`
- Explanation: Increase the values at indices `0` and `3`, producing `[3,1,5,2,1]`. Selecting the values `3`, `1`, and `2` yields `[1,2,3]` after sorting.

**Example 2**

- Input: `nums = [1,4,7,10]`
- Output: `1`
- Explanation: Even after the allowed increases, no two selected values can be made consecutive.
