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

### Required Complexity

- **Time:** $O(Q\log Q)$
- **Space:** $O(Q)$

<details>
<summary>Approach</summary>

#### General

**Keep one chronological history per key:** Map each key to a list of `(timestamp, value)` records. Because every `set` timestamp is strictly larger than all preceding set timestamps, appending preserves the sorted order of every individual key's history without insertion work.

**Search for the rightmost eligible version:** For `get(key, timestamp)`, binary-search that key's timestamps for the first record strictly later than the query. The record immediately before that boundary has the largest timestamp not exceeding the query and is therefore the required value. If the boundary is zero, no eligible version exists, so return `""`.

The history contains every value ever assigned to the key in chronological order. Binary search partitions it into eligible records at or before the query and ineligible later records. Choosing the last item of the eligible prefix exactly implements the requested greatest-`timestamp_prev` rule, including exact timestamp matches.

#### Complexity detail

Each `set` appends in $O(1)$ time. A `get` over $S$ versions takes $O(\log S)$ time. Across $Q$ arbitrary operations this is bounded by $O(Q\log Q)$ time. All stored records together use $O(Q)$ space.

#### Alternatives and edge cases

- **Reverse linear scan:** Searching a key's history from newest to oldest is correct and often short, but a query earlier than every version scans all $S$ records and can make a trace quadratic.
- **Ordered map per key:** A balanced search tree supports predecessor queries, but it adds machinery that the strictly increasing set timestamps make unnecessary.
- **Unknown key:** With no history to search, `get` must return `""`.
- **Query before the first version:** The binary-search boundary is zero, so there is no eligible record.
- **Exact timestamp:** A record whose timestamp equals the query is eligible and must be preferred over every earlier version.

</details>
