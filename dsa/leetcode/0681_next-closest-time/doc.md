# Next Closest Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 681 |
| Difficulty | Medium |
| Topics | Hash Table, String, Backtracking, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/next-closest-time/) |

## Problem Description
### Goal
Given a valid 24-hour time in `HH:MM` format, find the next clock time whose four displayed digits are all taken from the original display. A digit that appears once in the input may be reused any number of times in the result.

Move forward chronologically and return the first valid display encountered, preserving the `HH:MM` format. If no later time on the same day works, continue after midnight into the following day. The answer must be strictly later in cyclic time, so returning the unchanged display is allowed only after a full-day wrap.

### Function Contract
**Inputs**

- `time`: a valid zero-padded 24-hour time string

**Return value**

- The closest strictly later cyclic time display constructible from the input's digits

### Examples
**Example 1**

- Input: `time = "19:34"`
- Output: `"19:39"`

**Example 2**

- Input: `time = "23:59"`
- Output: `"22:22"`

**Example 3**

- Input: `time = "11:11"`
- Output: `"11:11"`
