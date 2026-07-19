# Minimum Moves to Equal Array Elements II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 462 |
| Difficulty | Medium |
| Topics | Array, Math, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) |

## Problem Description
### Goal
Given a nonempty integer array, one move chooses one element and either increments or decrements it by exactly one. Apply moves until every array position contains one common integer value.

Return the minimum total number of unit moves required. The final common value is not prescribed and may be any integer; choosing a median minimizes the sum of absolute distances, while choosing the mean or maximum can require more moves. Negative values and duplicates are handled normally. The function returns only the optimal move count, not the target value or transformed array.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- The minimum sum of unit changes required to move all values to one common integer

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`

**Example 2**

- Input: `nums = [1, 10, 2, 9]`
- Output: `16`

**Example 3**

- Input: `nums = [1, 0, 0, 8, 6]`
- Output: `14`
