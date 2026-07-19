## General
**Precompute where every letter ends**

Record the final index of each character. While scanning a prospective partition, maintain `partition_end`, the farthest final occurrence of any character encountered in that partition. The partition cannot legally end before this boundary because doing so would place another occurrence of one of its letters in a later part.

**Close at the first reachable boundary**

At index `i`, extend `partition_end` with the current character's final index. When `i = partition_end`, every character seen since the current partition began has its last occurrence at or before `i`. Cutting there is therefore valid.

It is also optimal to cut immediately: every valid partition starting at the same position must include through `partition_end`, while extending past it would only merge a suffix that could remain separate. Thus each greedy cut is the earliest legal cut. Repeating this argument on the untouched suffix maximizes the total number of parts, and the recorded distances are exactly their lengths.

## Complexity detail
The final-occurrence pass and greedy scan each take $O(n)$ time. Because the input alphabet is the fixed 26 lowercase letters, the last-position table uses $O(1)$ auxiliary space; the returned lengths are output space.

## Alternatives and edge cases
- **Merge character intervals:** Treat each letter's first-to-last span as an interval and merge overlapping spans; this is also linear with a fixed alphabet but needs more bookkeeping.
- **Repeated suffix scans:** Searching for every encountered character's last occurrence without preprocessing is correct but can take $O(n^2)$ time.
- **Backtracking over cut positions:** It can test all valid partitions but explores unnecessary combinations because every earliest legal boundary is forced.
- **All characters unique:** Every partition has length one.
- **One repeated character:** Its occurrences force the entire string into one part.
- **Chain of overlapping spans:** Even characters that do not repeat can lie inside a partition extended by other letters.
- **Output accounting:** Partition lengths must be positive and sum to the full string length.
