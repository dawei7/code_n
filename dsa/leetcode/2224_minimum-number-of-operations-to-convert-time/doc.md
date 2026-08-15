# Minimum Number of Operations to Convert Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2224 |
| Difficulty | Easy |
| Topics | String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/) |

## Problem Description

### Goal

Two strings describe valid 24-hour times in `HH:MM` format, ranging from `00:00` through `23:59`. The time `current` is no later than `correct`.

In one operation, increase `current` by exactly 1, 5, 15, or 60 minutes. Operations may be repeated, but no backward move or other increment is available. Return the minimum number needed to make `current` equal `correct`.

### Function Contract

**Inputs**

- `current`: The starting 24-hour time in `HH:MM` format.
- `correct`: The target 24-hour time in `HH:MM` format, with `current <= correct`.

The minute difference is between 0 and 1439 inclusive.

**Return value**

Return the minimum number of allowed minute increments whose sum equals the time difference.

### Examples

#### Example 1

- **Input:** `current = "02:30", correct = "04:35"`
- **Output:** `3`

#### Example 2

- **Input:** `current = "11:00", correct = "11:01"`
- **Output:** `1`

#### Example 3

- **Input:** `current = "00:00", correct = "01:20"`
- **Output:** `3`
