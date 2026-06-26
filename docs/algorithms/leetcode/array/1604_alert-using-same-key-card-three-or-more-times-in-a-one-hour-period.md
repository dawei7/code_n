# Alert Using Same Key-Card Three or More Times in a One Hour Period

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1604 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [alert-using-same-key-card-three-or-more-times-in-a-one-hour-period](https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/) |

## Problem Description & Examples
### Goal
Find employees who used their key card at least three times within any one-hour
window.

### Function Contract
**Inputs**

- `keyName`: employee names for each card use.
- `keyTime`: corresponding times in `"HH:MM"` format.

**Return value**

The alerted employee names in lexicographic order.

### Examples
**Example 1**

- Input: `keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"], keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]`
- Output: `["daniel"]`

**Example 2**

- Input: `keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"], keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]`
- Output: `["bob"]`

**Example 3**

- Input: `keyName = ["john", "john", "john"], keyTime = ["23:58", "23:59", "00:01"]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Group times by employee and convert each time to minutes after midnight. Sort
each employee's times, then check every window of three consecutive uses. If
`times[i + 2] - times[i] <= 60`, that employee triggers an alert.

---

## Complexity Analysis
- **Time Complexity**: `O(k log k)`, dominated by sorting grouped times.
- **Space Complexity**: `O(k)`.
