## General
Use a hash table whose key is a requested group size and whose value is the not-yet-complete bucket of people requesting that size. Process people in identifier order. Append person `i` to the bucket keyed by `groupSizes[i]`.

A bucket with key $s$ becomes a complete valid group exactly when it contains $s$ people. Move that bucket into the answer immediately and replace it with an empty bucket so later people requesting $s$ start another group. Every person enters exactly one bucket and a completed bucket contains only people who requested its exact size. Because the input guarantees a solution, no partial bucket remains after all people have been processed; consequently the emitted groups cover every person exactly once and satisfy every requested size.

## Complexity detail
Let $n$ be the number of people. Each index is appended once and transferred into the answer once, while expected hash-table access is constant time, for $O(n)$ total time. The incomplete buckets and returned grouping together store $n$ indices, so auxiliary construction space is $O(n)$ including the returned answer.

## Alternatives and edge cases
- **Sort by requested size:** Sorting pairs of size and identifier makes equal requests contiguous, but costs $O(n \log n)$ time and requires careful chunking.
- **Repeated search among people:** Building each group by scanning for compatible unassigned people can take $O(n^2)$ time.
- **Several groups of one size:** Filling and clearing a bucket is essential; a size may require multiple distinct groups.
- **Singleton requests:** Every person requesting size one must be emitted immediately in a separate group.
- **Non-unique output:** Tests must validate the partition rather than require one particular ordering of otherwise valid groups.
