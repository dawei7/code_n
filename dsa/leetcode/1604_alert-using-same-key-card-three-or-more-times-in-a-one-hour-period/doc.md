# Alert Using Same Key-Card Three or More Times in a One Hour Period

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1604 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/) |

## Problem Description
### Goal
An office records every use of an employee key card. For each event, `keyName[i]` identifies the employee and `keyTime[i]` gives that event's time during one particular day in 24-hour `"HH:MM"` format. Every `(name, time)` pair is unique.

An employee triggers an alert when their card appears at least three times during one one-hour period. Both endpoints count: events at `"10:00"` and `"11:00"` are exactly one hour apart and may belong to the same alerting window, whereas events 61 minutes apart do not.

Return every alerted employee name exactly once, sorted in ascending alphabetical order.

### Function Contract
**Inputs**

- `keyName`: an array of $n$ lowercase employee names, where $1 \le n \le 10^5$ and each name has length from 1 through 10.
- `keyTime`: an array of $n$ corresponding access times in 24-hour `"HH:MM"` format. All records belong to one day, and each paired name and time is unique.

**Return value**

Return the unique names for which some three access times span at most 60 minutes, in ascending lexicographic order.

### Examples
**Example 1**

- Input: `keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]`, `keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]`
- Output: `["daniel"]`
- Explanation: Daniel's uses at `"10:00"`, `"10:40"`, and `"11:00"` span exactly 60 minutes.

**Example 2**

- Input: `keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]`, `keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]`
- Output: `["bob"]`
- Explanation: Alice has no qualifying triple, while Bob has three uses between `"21:00"` and `"21:30"`.
