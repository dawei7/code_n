# Tweet Counts Per Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1348 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Binary Search, Design, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/tweet-counts-per-frequency/) |

## Problem Description

### Goal

Design a `TweetCounts` service that records the time of each occurrence of a named tweet and later reports occurrence counts over an inclusive time range.

`recordTweet(tweetName, time)` stores one occurrence of `tweetName` at the given time in seconds. Multiple occurrences may have the same name and time.

`getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)` divides the inclusive interval from `startTime` through `endTime` into consecutive buckets starting at `startTime`. The bucket width is 60 seconds for `"minute"`, 3600 seconds for `"hour"`, and 86400 seconds for `"day"`; the final bucket is truncated at `endTime` when necessary. Return the number of stored occurrences of `tweetName` in each bucket.

### Function Contract

**Inputs**

- `recordTweet(tweetName, time)`: a tweet name and its nonnegative integer timestamp.
- `getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)`: one of the three supported frequency names, a tweet name, and inclusive integer bounds with `startTime <= endTime`.
- For one query, let $r$ be the number of stored occurrences for `tweetName`, and let $b$ be the number of requested buckets.
- The app-local `solve(operations, arguments)` adapter receives the constructor and method calls in order.

**Return value**

- `recordTweet` returns no value.
- `getTweetCountsPerFrequency` returns a length-$b$ list of occurrence counts in chronological bucket order.
- The app-local adapter returns every operation result in order, using `null` for the constructor and recording calls.

### Examples

**Example 1**

- Operations: construct, record `"tweet3"` at times `0`, `60`, and `10`; then query minute buckets from `0` through `59`.
- Query output: `[2]`

**Example 2**

- Using the same records, query minute buckets from `0` through `60`.
- Query output: `[2, 1]`

**Example 3**

- After also recording `"tweet3"` at time `120`, query hour buckets from `0` through `210`.
- Query output: `[4]`
