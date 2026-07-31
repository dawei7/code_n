# Sleep

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2621 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/sleep/) |

## Problem Description

### Goal

Given a positive integer `millis`, implement an asynchronous JavaScript function that delays completion for approximately that many milliseconds. The function must return a promise immediately, and that promise must remain pending until the requested interval has elapsed.

The promise may resolve with any value. Small timing differences caused by timer scheduling are acceptable, so the observed duration does not need to equal `millis` exactly. The requested delay is between $1$ and $1000$ milliseconds, inclusive.

### Function Contract

**Inputs**

- `millis`: The positive number of milliseconds for which the returned promise should remain pending.

Let $m = \texttt{millis}$ denote the requested elapsed delay.

**Return value**

Return a promise that resolves only after approximately $m$ milliseconds. Its resolved value is unrestricted.

### Examples

**Example 1**

- Input: `millis = 100`
- Output: approximately `100` milliseconds
- Explanation: Measuring from the call until the returned promise resolves should produce a duration close to 100 milliseconds.

**Example 2**

- Input: `millis = 200`
- Output: approximately `200` milliseconds
- Explanation: The promise stays pending for the requested interval before resolving.

**Example 3**

- Input: `millis = 1`
- Output: approximately `1` millisecond
- Explanation: Even the minimum legal delay is scheduled asynchronously rather than resolved immediately.
