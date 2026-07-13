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

### Required Complexity

- **Time:** $O(QP)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Preserve insertion order in a flat log list**

Append each `(identifier, timestamp)` pair. `put` is constant time, and scanning this list naturally emits matching identifiers in insertion order without a second ordering structure.

**Translate granularity into a prefix length**

The timestamp fields have fixed widths and separators, so each granularity corresponds to a fixed prefix: four characters for `Year`, seven for `Month`, through all nineteen for `Second`. Truncating the stored timestamp and both query endpoints to that length applies the requested precision exactly.

**Use lexicographic order as chronological order**

Every field is zero-padded from most significant to least significant. Therefore, two equal-length timestamp prefixes compare lexicographically in the same order as their represented dates and times. Include a log precisely when `start_prefix <= timestamp_prefix <= end_prefix`.

**Why truncation gives inclusive boundaries**

All timestamps sharing the start prefix belong to the first requested time bucket, even if their omitted fields precede the literal fields in `start`; the same applies to the entire end bucket. Prefix comparison includes both buckets and every complete bucket between them, which is exactly an inclusive granularity query.

#### Complexity detail

Let `P` be the number of stored logs and `Q` the number of retrievals in a trace. `put` takes $O(1)$ time, while each `retrieve` scans `P` logs in $O(P)$ time, for $O(QP)$ worst-case trace time. The stored log list uses $O(P)$ space; each returned list uses space proportional to its matches.

#### Alternatives and edge cases

- **Keep logs sorted and binary-search bounds:** retrieval can start in $O(\log P)$ time, but array insertion costs $O(P)$ unless a balanced ordered structure is available.
- **Sort a copy on every retrieval:** enables binary search afterward but repeats $O(P \log P)$ work for each query.
- **Bucket maps by every granularity:** can accelerate repeated queries but duplicates indexing state across six precision levels.
- Query endpoints are inclusive after truncation to the selected granularity.
- A `Day` query ignores hours, minutes, and seconds in both endpoint strings.
- Distinct IDs may share an identical timestamp and must all be returned.
- A query with no stored timestamp in its truncated interval returns an empty list.
- Fixed-width zero padding is essential to the equivalence between string and chronological ordering.

</details>
