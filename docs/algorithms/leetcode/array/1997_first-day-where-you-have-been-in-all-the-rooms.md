# First Day Where You Have Been in All the Rooms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1997 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [first-day-where-you-have-been-in-all-the-rooms](https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/) |

## Problem Description & Examples
### Goal
Rooms are visited by deterministic rules based on visit parity. Find the first day on which every room has been visited at least once.

### Function Contract
**Inputs**

- `nextVisit`: for each room, the room to visit after an odd-numbered visit to that room.

**Return value**

Return the first day modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nextVisit = [0,0]`
- Output: `2`

**Example 2**

- Input: `nextVisit = [0,0,2]`
- Output: `6`

**Example 3**

- Input: `nextVisit = [0,1,2,0]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Let `dp[i]` be the first day room `i` is reached. Moving from room `i` to `i + 1` requires revisiting the interval from `nextVisit[i]` back to `i`; prefix-style recurrence gives `dp[i + 1] = 2 * dp[i] - dp[nextVisit[i]] + 2` modulo the limit.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
