# Time Based Key-Value Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 981 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Binary Search, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/time-based-key-value-store/) |

## Problem Description

### Goal

Design a time-based key-value data structure that can retain several values for the same key at different timestamps and retrieve the value that was current at a requested time.

The `TimeMap()` constructor creates an empty store. Calling `set(key, value, timestamp)` records `value` for `key` at that timestamp. Calling `get(key, timestamp)` returns the value recorded for that key at the greatest previous timestamp satisfying $\texttt{timestamp_prev}\le\texttt{timestamp}$. If the key has no record at or before the requested time, return the empty string `""`. All timestamps supplied to `set` are strictly increasing across the operation sequence.

### Function Contract

**Inputs**

- `operations`: the app-local ordered trace of `["set", key, value, timestamp]` and `["get", key, timestamp]` calls.
- Keys and values contain lowercase English letters and digits and have lengths from $1$ through $100$.
- Timestamps satisfy $1\le\texttt{timestamp}\le10^7$, and at most $2\cdot10^5$ calls are made.

Let $Q$ be the number of operations and $S$ the number of stored versions for the key involved in one `get`.

**Return value**

- The app-local adapter returns one result per operation: `null` for each `set`, and the specified string for each `get`.
- The native artifact implements the `TimeMap` constructor plus `set` and `get` methods directly.

### Examples

**Example 1**

- Input: `operations = [["set", "foo", "bar", 1], ["get", "foo", 1], ["get", "foo", 3], ["set", "foo", "bar2", 4], ["get", "foo", 4], ["get", "foo", 5]]`
- Output: `[null, "bar", "bar", null, "bar2", "bar2"]`
- Explanation: the record at timestamp `1` remains current until the later record at timestamp `4`.

**Example 2**

- Input: `operations = [["set", "x", "a", 5], ["get", "x", 4], ["get", "missing", 9]]`
- Output: `[null, "", ""]`
