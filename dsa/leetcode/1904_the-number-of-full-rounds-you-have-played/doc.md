# The Number of Full Rounds You Have Played

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1904 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [The Number of Full Rounds You Have Played](https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/) |

## Problem Description

### Goal

An online chess tournament starts a new 15-minute round at `00:00`, `00:15`, `00:30`, and every other quarter-hour through `23:45`. You are given the times at which you log in and log out, using the 24-hour `hh:mm` format.

Count only rounds whose complete interval lies within your connected session. If `logoutTime` is earlier than `loginTime`, the session crosses midnight into the next day. The two times are guaranteed to differ.

### Function Contract

**Inputs**

- `loginTime`: the session's start time in `hh:mm` format.
- `logoutTime`: the session's end time in `hh:mm` format.
- Hours range from `00` through `23`, and minutes from `00` through `59`.

**Return value**

Return the number of complete 15-minute tournament rounds played from login through logout, accounting for a possible midnight crossing.

### Examples

**Example 1**

- Input: `loginTime = "09:31", logoutTime = "10:14"`
- Output: `1`
- Explanation: Only the round from `09:45` through `10:00` is fully contained in the session.

**Example 2**

- Input: `loginTime = "21:30", logoutTime = "03:00"`
- Output: `22`
- Explanation: Ten complete rounds occur before midnight and twelve after it.

**Example 3**

- Input: `loginTime = "00:00", logoutTime = "00:15"`
- Output: `1`
