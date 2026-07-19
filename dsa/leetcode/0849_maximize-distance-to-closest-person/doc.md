# Maximize Distance to Closest Person

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 849 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-distance-to-closest-person/) |

## Problem Description
### Goal
A 0-indexed array `seats` represents one row of seats. A value of `1` means that someone already occupies that position, and `0` means that the seat is empty. The row is guaranteed to contain at least one occupied seat and at least one empty seat.

Alex will choose one empty seat. For any choice, his distance to the closest person is the smallest absolute index difference between his seat and an occupied seat. Return the largest such closest-person distance that Alex can obtain.

### Function Contract
**Inputs**

- `seats`: a binary array of length $n$, where $2 \leq n \leq 2 \cdot 10^4$, containing at least one `0` and at least one `1`.

**Return value**

Return the maximum possible distance from an empty seat to its closest occupied seat.

### Examples
**Example 1**

- Input: `seats = [1,0,0,0,1,0,1]`
- Output: `2`

Sitting at index `2` leaves the nearest occupied seats two positions away.

**Example 2**

- Input: `seats = [1,0,0,0]`
- Output: `3`

The last seat is three positions from the only person.

**Example 3**

- Input: `seats = [0,1]`
- Output: `1`
