# Binary Watch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 401 |
| Difficulty | Easy |
| Topics | Backtracking, Bit Manipulation |
| Official Link | [binary-watch](https://leetcode.com/problems/binary-watch/) |

## Problem Description & Examples
### Goal
A binary watch has four hour LEDs and six minute LEDs. Given how many LEDs are on, list every valid time that could be displayed.

### Function Contract
**Inputs**

- `turnedOn`: int number of lit LEDs

**Return value**

List[str] - valid times formatted as `H:MM`

### Examples
**Example 1**

- Input: `turnedOn = 0`
- Output: `["0:00"]`

**Example 2**

- Input: `turnedOn = 1`
- Output: `["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]`

**Example 3**

- Input: `turnedOn = 9`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Bounded enumeration with bit counting.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` because there are only 12 hours and 60 minutes
- **Space Complexity**: `O(1)` excluding the returned list
