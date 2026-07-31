# Count Mentions Per User

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3433 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-mentions-per-user/) |

## Problem Description

### Goal

A system has `numberOfUsers` users, all initially online, and an unordered collection of timestamped events. A `MESSAGE` event contains either explicit tokens such as `id2 id2 id0`, the token `ALL`, or the token `HERE`. Explicit tokens mention their named users even while offline and count repeated ids separately. `ALL` mentions every user, whereas `HERE` mentions only users online at that timestamp.

An `OFFLINE` event makes its named, currently online user unavailable for exactly 60 time units; that user automatically returns at `timestamp + 60`. Status changes, including automatic returns and `OFFLINE` events, are processed before messages sharing their timestamp. Return an array containing the total number of mentions received by each user across all message events.

### Function Contract

**Inputs**

- `numberOfUsers`: The number $U$ of users, where $1\le U\le100$; ids range from `0` through `U - 1`.
- `events`: Between 1 and 100 three-string records describing `MESSAGE` or `OFFLINE` events. Timestamps are integers from 1 through $10^5$, and each explicit message contains between 1 and 100 id tokens.

Every user named by an `OFFLINE` event is guaranteed to be online at that event's time.

**Return value**

Return `mentions`, where `mentions[i]` is the number of times user `i` was mentioned.

### Examples

**Example 1**

- Input: `numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]`
- Output: `[2,2]`

**Example 2**

- Input: `numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]`
- Output: `[2,2]`

**Example 3**

- Input: `numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]`
- Output: `[0,1]`
