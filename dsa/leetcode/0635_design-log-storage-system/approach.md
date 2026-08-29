## General

**Use the timestamp's text format as an ordered key.** Every timestamp has exactly the same field order:

`Year:Month:Day:Hour:Minute:Second`.

Every field is zero-padded, so lexicographic string order agrees with chronological field order. The first differing character belongs to the earliest differing time component, and equal-width decimal text sorts in numeric order. For example, `"09" < "10"` just as month 9 precedes month 10.

This property means the exact class does not need to parse dates, calculate seconds, or know the number of days in each month.

**Map each granularity to a prefix length.** The dictionary `d` stores:

- Year: 4 characters, such as `2017`;
- Month: 7 characters, such as `2017:01`;
- Day: 10 characters, such as `2017:01:31`;
- Hour: 13 characters;
- Minute: 16 characters;
- Second: 19 characters, the complete timestamp.

The lengths include all separators preceding the selected field. Taking `timestamp[:i]` therefore keeps exactly the components that matter and discards every less significant component.

**Why truncation implements granularity.** A Day query says that hours, minutes, and seconds should be ignored. Comparing only the first 10 characters compares year, then month, then day, and nothing else. A log at `2017:01:01:23:59:59` and one at `2017:01:01:00:00:00` both become `2017:01:01` at Day precision.

The same rule applies uniformly at every supported precision. At Year precision, all timestamps in 2017 collapse to `2017`. At Second precision, no character is discarded.

**Store logs with constant-work insertion.** `put` appends `(id, timestamp)` to `self.logs`. The problem does not require logs to be returned in timestamp order, so maintaining a sorted structure during insertion is unnecessary. The unique-ID promise means each stored pair represents a distinct log identity.

**Retrieve by comparing all three prefixes.** For a requested granularity, let `i = d[granularity]`. The list comprehension keeps a log exactly when

`start[:i] <= ts[:i] <= end[:i]`.

Truncating all three values is crucial:

- truncating `ts` ignores the log's lower fields;
- truncating `start` makes the lower start fields irrelevant;
- truncating `end` includes the complete final granularity bucket rather than stopping at its supplied lower fields.

The two `<=` comparisons make both ends inclusive, as required.

Consider the sample Year query from a timestamp in 2016 through one in 2017. The boundaries become `"2016"` and `"2017"`. All three stored logs have a year prefix inside that inclusive interval, regardless of their month or time.

For the Hour query, the boundaries retain text through the hour. The 2016 log at hour 00 is smaller than the start prefix at hour 01, so it is excluded. The two 2017 logs at hours 22 and 23 are included through the end hour 23; their minute and second fields do not matter.

**Why lexicographic comparison is correct.** Compare two truncated timestamps at the same precision. If all retained fields are equal, they represent the same granularity bucket. Otherwise, their first unequal retained field is the most significant time component on which they differ. Zero-padding makes that field's textual comparison match its numeric comparison. Therefore, the whole prefix's string comparison matches chronological bucket order.

The comprehension scans logs in insertion order, so matching IDs are returned in insertion order. The contract permits any result order, making this a valid deterministic choice.

**No calendar arithmetic is needed.** The algorithm compares structured labels rather than elapsed durations. Even the statement's broad Day range does not require validating whether every day exists in every month. Stored and queried timestamps obey the provided format, and ordered components alone determine the requested relation.

## Complexity detail

Let $P$ be the number of stored logs and $Q$ the number of retrieval calls. `put` performs an amortized $O(1)$ list append and adds one stored pair.

One retrieval scans all $P$ logs. Each slice and comparison touches at most 19 characters, a fixed maximum, so it is $O(P)$ time under the source constraints. Across $Q$ retrievals, worst-case query work is $O(QP)$, matching the manifest.

Persistent storage is $O(P)$ for the log pairs. The returned list may contain up to $P$ IDs and therefore uses $O(P)$ output space. Apart from that output, retrieval uses constant working state. The six-entry granularity dictionary is constant size.

If timestamp length were not fixed, comparison cost would include the retained prefix length $G$, giving $O(PG)$ per retrieval. Here $G\le19$.

## Alternatives and edge cases

- **Convert timestamps to numeric keys:** Parse fields and encode them in a monotone mixed-radix number. This permits numeric comparisons but adds arithmetic and calendar-like constants that fixed text already avoids.
- **Sorted map or balanced tree:** Store logs by timestamp and range-query only matching keys. Retrieval can improve for large datasets, but insertion becomes logarithmic and duplicate timestamps need grouped IDs.
- **Keep a sorted list with binary search:** It can narrow scans, but arbitrary insertion requires shifting unless logs arrive chronologically.
- **Year granularity:** Only four characters are compared, so every lower component is ignored.
- **Second granularity:** All 19 characters are compared, giving exact timestamp boundaries.
- **Inclusive end:** The second `<=` includes every log in the final granularity bucket.
- **Same start and end bucket:** Every log sharing that truncated prefix is returned.
- **Zero padding:** It is essential. Without it, textual month `"10"` could sort before `"2"`.
- **Duplicate timestamps:** They are harmless; every stored pair is scanned and every matching ID is returned.
- **Unique IDs:** The statement guarantees them, so the result does not need ID deduplication.
- **Unrecognized granularity:** Dictionary lookup would fail, but the contract restricts input to the six known strings.
- **Result order:** Insertion order is returned, and no sorting is needed because any order is accepted.
