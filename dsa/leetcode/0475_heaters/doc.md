# Heaters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 475 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/heaters/) |

## Problem Description
### Goal
Houses and heaters occupy integer coordinates on a one-dimensional number line. Every heater uses the same nonnegative radius `r` and covers all houses whose absolute coordinate distance from it is at most `r`.

Return the smallest common radius that ensures every house is covered by at least one heater. Each house may use its nearest heater independently, and heaters do not need to cover one another. Input coordinates may be unordered and may contain repeated locations. A house at a heater needs distance zero. The function returns only the radius, not house-to-heater assignments or coverage intervals.

### Function Contract
**Inputs**

- `houses`: house coordinates
- `heaters`: heater coordinates

**Return value**

- The minimum nonnegative integer radius shared by all heaters that covers every house

### Examples
**Example 1**

- Input: `houses = [1, 2, 3], heaters = [2]`
- Output: `1`

**Example 2**

- Input: `houses = [1, 2, 3, 4], heaters = [1, 4]`
- Output: `1`

**Example 3**

- Input: `houses = [1, 5], heaters = [2]`
- Output: `3`
