## General
**Keep one chronological history per key:** Map each key to a list of `(timestamp, value)` records. Because every `set` timestamp is strictly larger than all preceding set timestamps, appending preserves the sorted order of every individual key's history without insertion work.

**Search for the rightmost eligible version:** For `get(key, timestamp)`, binary-search that key's timestamps for the first record strictly later than the query. The record immediately before that boundary has the largest timestamp not exceeding the query and is therefore the required value. If the boundary is zero, no eligible version exists, so return `""`.

The history contains every value ever assigned to the key in chronological order. Binary search partitions it into eligible records at or before the query and ineligible later records. Choosing the last item of the eligible prefix exactly implements the requested greatest-`timestamp_prev` rule, including exact timestamp matches.

## Complexity detail
Each `set` appends in $O(1)$ time. A `get` over $S$ versions takes $O(\log S)$ time. Across $Q$ arbitrary operations this is bounded by $O(Q\log Q)$ time. All stored records together use $O(Q)$ space.

## Alternatives and edge cases
- **Reverse linear scan:** Searching a key's history from newest to oldest is correct and often short, but a query earlier than every version scans all $S$ records and can make a trace quadratic.
- **Ordered map per key:** A balanced search tree supports predecessor queries, but it adds machinery that the strictly increasing set timestamps make unnecessary.
- **Unknown key:** With no history to search, `get` must return `""`.
- **Query before the first version:** The binary-search boundary is zero, so there is no eligible record.
- **Exact timestamp:** A record whose timestamp equals the query is eligible and must be preferred over every earlier version.
