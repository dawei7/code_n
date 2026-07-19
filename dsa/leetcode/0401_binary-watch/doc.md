# Binary Watch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 401 |
| Difficulty | Easy |
| Topics | Backtracking, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-watch/) |

## Problem Description
### Goal
On a binary watch, four LEDs encode an hour from `0` through `11` and six LEDs encode minutes from `0` through `59`. Given `turned_on`, consider all valid times whose combined hour and minute representations contain exactly that many lit bits.

Return every matching time in any order. Format the hour without a leading zero and the minute with exactly two decimal digits, such as `"1:05"`. Exclude bit patterns that would represent invalid hours or minutes even when their total lit count matches. Each valid clock time appears once, and impossible LED counts produce an empty list.

### Function Contract
**Inputs**

- `turned_on`: the total number of lit hour and minute LEDs

**Return value**

- Return all valid times in any order. Format hours without a leading zero and minutes with exactly two digits.

### Examples
**Example 1**

- Input: `turned_on = 0`
- Output: `["0:00"]`

**Example 2**

- Input: `turned_on = 1`
- Output: `["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]`

**Example 3**

- Input: `turned_on = 9`
- Output: `[]`
