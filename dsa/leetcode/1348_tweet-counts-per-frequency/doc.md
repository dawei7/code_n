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

### Required Complexity

- **Time:** $O(r+b)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Store occurrences by tweet name.** A hash map associates each name with a list of all recorded timestamps. Recording an occurrence appends its time, so duplicate timestamps remain distinct and the update takes constant amortized time.

**Translate the frequency into a bucket width.** Select 60, 3600, or 86400 seconds and compute `bucket_count = (endTime - startTime) // width + 1`. Initialize exactly that many zero counts; this formula includes the possibly shorter final bucket.

**Assign each relevant record once.** Scan the timestamps stored for the requested name. Ignore times outside the inclusive query interval. For every time inside it, `(time - startTime) // width` is its unique bucket index, so increment that count. These half-open bucket calculations agree with the inclusive query because the final accepted second `endTime` still maps within the allocated last bucket. Each qualifying occurrence is counted once, and every returned bucket corresponds to exactly one requested subinterval.

#### Complexity detail

`recordTweet` takes $O(1)$ amortized time. A query initializes $b$ counts and scans $r$ timestamps, for $O(r+b)$ time. Across all names, storage is linear in the total number of recorded occurrences; for the queried name its contribution is $O(r)$.

#### Alternatives and edge cases

- **Scan records once per bucket:** Testing all $r$ timestamps separately for each of $b$ buckets is correct but costs $O(rb)$ time.
- **Sorted timestamps plus binary search:** Maintaining or lazily sorting each name's times can answer sparse-range queries with boundary searches, but insertion and sorting tradeoffs complicate a workload where the direct linear scan already satisfies the contract.
- **Unknown tweet name:** No timestamps exist, but the method must still return the correct number of zero buckets.
- **Duplicate timestamps:** Every recording is a separate occurrence and must increment the same bucket.
- **Partial final bucket:** The last bucket ends at `endTime`, not necessarily at a full frequency boundary.
- **Inclusive endpoint:** A record exactly at `endTime` belongs to the last bucket.

</details>
