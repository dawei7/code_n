# Restore IP Addresses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 93 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/restore-ip-addresses/) |

## Problem Description
### Goal
You are given a string containing only decimal digits. Restore IPv4 punctuation by inserting exactly three dots without deleting, reordering, or changing any digit, thereby creating four nonempty segments.

Each segment must represent an integer from `0` through `255` and cannot contain a leading zero unless it is exactly `"0"`. Return every valid restored address, in any order, with no duplicates. If the string length or digit values cannot support four legal segments, return an empty list.

### Function Contract
**Inputs**

- `s`: a string containing only decimal digits

**Return value**

All valid restored addresses in any order.

### Examples
**Example 1**

- Input: `s = "25525511135"`
- Output: `["255.255.11.135","255.255.111.35"]`

**Example 2**

- Input: `s = "0000"`
- Output: `["0.0.0.0"]`

**Example 3**

- Input: `s = "101023"`
- Output: five valid addresses
