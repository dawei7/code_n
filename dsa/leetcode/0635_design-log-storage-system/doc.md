# Design Log Storage System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 635 |
| Difficulty | Medium |
| Topics | Hash Table, String, Design, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/design-log-storage-system/) |

## Problem Description
### Goal
Design a log storage system that accepts `put(id, timestamp)` calls, where each timestamp uses the fixed format `YYYY:MM:DD:HH:MM:SS`. Stored logs persist across operations and retain their integer identifiers.

Support `retrieve(start, end, granularity)`, returning the identifiers whose timestamps fall within the inclusive interval when compared only through the requested granularity. The granularity is one of `Year`, `Month`, `Day`, `Hour`, `Minute`, or `Second`; less significant timestamp fields are ignored at both interval boundaries. A retrieval does not remove or modify stored logs.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `LogSystem`, followed by `put` or `retrieve` calls
- `arguments`: the matching empty constructor arguments, identifier/timestamp pairs, or start/end/granularity triples
- `put(id, timestamp)`: store one log with timestamp format `YYYY:MM:DD:HH:MM:SS`
- `retrieve(start, end, granularity)`: query inclusively at `Year`, `Month`, `Day`, `Hour`, `Minute`, or `Second` precision

**Return value**

- The operation trace returns null for construction and `put`
- Each `retrieve` returns the matching identifiers in their insertion order

### Examples
**Example 1**

- Input: store IDs `1` and `2` during 2017 and ID `3` during 2016; retrieve from 2016 through 2017 at `Year` precision
- Output: `[1,2,3]`

**Example 2**

- Input: store one timestamp in January and one in February; query only January at `Month` precision
- Output: the January identifier

**Example 3**

- Input: store two logs on the same day at different times; query that date at `Day` precision
- Output: both identifiers
