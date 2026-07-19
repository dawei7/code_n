# Open the Lock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 752 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/open-the-lock/) |

## Problem Description

### Goal

A lock has four circular decimal wheels and begins at `"0000"`. In one move, rotate exactly one wheel by one slot forward or backward; digits wrap between `0` and `9`.

The listed `deadends` are forbidden combinations: if the lock displays one, its wheels can no longer turn. Return the minimum number of legal moves needed to display `target`, or `-1` if the target cannot be reached without entering a deadend. The starting combination also obeys the deadend restriction.

### Function Contract

**Inputs**

- `deadends`: a list of forbidden four-character digit combinations.
- `target`: the four-character digit combination to reach.

**Return value**

- The minimum number of single-wheel turns from `"0000"` to `target`, or `-1` when unreachable.

### Examples

**Example 1**

- Input: `deadends = ["0201", "0101", "0102", "1212", "2002"]`, `target = "0202"`
- Output: `6`
- Explanation: A shortest legal route avoids the forbidden combinations and uses six wheel turns.

**Example 2**

- Input: `deadends = ["8888"]`, `target = "0009"`
- Output: `1`
- Explanation: Rotate the last wheel backward once, wrapping from `0` to `9`.
