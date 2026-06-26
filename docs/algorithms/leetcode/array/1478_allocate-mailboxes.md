# Allocate Mailboxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1478 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Sorting |
| Official Link | [allocate-mailboxes](https://leetcode.com/problems/allocate-mailboxes/) |

## Problem Description & Examples
### Goal
Place `k` mailboxes among houses on a line so the sum of distances from each house to its nearest mailbox is minimized.

### Function Contract
**Inputs**

- `houses`: house positions.
- `k`: number of mailboxes.

**Return value**

The minimum possible total distance.

### Examples
**Example 1**

- Input: `houses = [1,4,8,10,20], k = 3`
- Output: `5`

**Example 2**

- Input: `houses = [2,3,5,12,18], k = 2`
- Output: `9`

**Example 3**

- Input: `houses = [7,4,6,1], k = 1`
- Output: `8`

---

## Underlying Base Algorithm(s)
Sort positions, precompute the optimal one-mailbox cost for every interval using the median, then run DP over the first `i` houses and number of mailboxes used.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 k)`
- **Space Complexity**: `O(n^2 + nk)`
