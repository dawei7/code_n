# Find the Most Common Response

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3527 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-most-common-response/) |

## Problem Description

### Goal

You are given a two-dimensional string array `responses`. Each inner array contains the survey responses collected on one day. Before combining the days, remove duplicate strings independently within each day: repeating the same response several times on one day contributes only once for that day, while the same response on different days contributes once for every such day.

After this per-day deduplication, find the response with the greatest total frequency across all days. If several responses have the same greatest frequency, return the lexicographically smallest one.

### Function Contract

**Inputs**

- `responses`: A non-empty list of non-empty daily response lists.

There are at most $1000$ days and at most $1000$ responses per day. Every response has length from $1$ through $10$ and contains only lowercase English letters.

**Return value**

- The most frequent response after per-day deduplication, breaking ties lexicographically.

### Examples

**Example 1**

- Input: `responses = [["good", "ok", "good", "ok"], ["ok", "bad", "good", "ok", "ok"], ["good"], ["bad"]]`
- Output: `"good"`
- Explanation: The deduplicated days are `[["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]`; `"good"` occurs on three days.

**Example 2**

- Input: `responses = [["good", "ok", "good"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]`
- Output: `"bad"`
- Explanation: `"bad"`, `"good"`, and `"ok"` each occur twice after deduplication, and `"bad"` is lexicographically smallest.
