# Find Median Given Frequency of Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 571 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-median-given-frequency-of-numbers/) |

## Problem Description
### Goal
Given a `Numbers` table whose rows contain a distinct number and the frequency with which it occurs, interpret the table as a multiset in which each number is repeated exactly that many times. Find the median value that would result if this expanded multiset were sorted in non-decreasing order.

For an odd total frequency, the median is the value at the single central position. For an even total, it is the arithmetic mean of the two central values. Return the result in a column named `median`, rounded to one decimal place, without requiring the repeated rows to be physically materialized.

### Function Contract
**Inputs**

- `Numbers(num, frequency)`: each distinct number and its positive occurrence count

**Return value**

- A one-row result grid with column `median`

### Examples
**Example 1**

- Input frequencies: `1:1, 2:1, 3:1`
- Output: `2.0`

**Example 2**

- Input frequencies: `1:1, 3:1`
- Output: `2.0`

**Example 3**

- Input frequency: `7:100`
- Output: `7.0`
