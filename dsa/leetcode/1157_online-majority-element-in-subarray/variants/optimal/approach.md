## General
**Store a composable majority candidate.** A Boyer-Moore summary of a segment is a pair `(candidate, balance)`. To merge two summaries, equal candidates add balances; different candidates cancel the smaller balance from the larger. If a value occupies more than half of a range, cancellation cannot eliminate all of its excess occurrences, so the merged summary for that range must retain it as the candidate. Store these summaries in a segment tree.

**Preserve range order while querying.** Convert the inclusive endpoints to segment-tree leaves and collect the $O(\log n)$ nodes covering the range. Nodes taken from the left boundary are merged left to right, while nodes taken from the right boundary are prepended to a separate right summary. Merging the two accumulated summaries yields the only possible strict-majority candidate for the requested subarray.

**Verify the threshold exactly.** A Boyer-Moore candidate is only a candidate; a range with no strict majority can still leave a positive balance. During construction, also record the sorted array indexes for each value. Two binary searches in the candidate's index list count its occurrences between `left` and `right`. Return the candidate exactly when this count reaches `threshold`; otherwise return `-1`. The query guarantee ensures no second candidate needs to be tested.

The app adapter constructs one checker and invokes it for every query. Tree construction is linear because each leaf and internal node is initialized once, and the position lists are naturally sorted by the left-to-right array scan.

## Complexity detail
Building the position lists and segment tree costs $O(n)$ time and space. Each range decomposes into $O(\log n)$ tree nodes, and verification performs two binary searches in one position list, also bounded by $O(\log n)$. Across $q$ queries, total time is $O(n + q \log n)$ and auxiliary storage is $O(n)$.

## Alternatives and edge cases
- **Scan every queried subarray:** Counting values directly is simple and correct, but a full-range query costs $O(n)$ and $q$ such queries can cost $O(nq)$.
- **Random sampling:** Sampling positions and verifying their values is often fast, but it is probabilistic and does not provide the deterministic contract of the segment tree.
- **Store full frequency maps in tree nodes:** Queries become easy to combine, but construction and memory can grow far beyond linear size.
- **Candidate without verification:** Boyer-Moore always returns some candidate for a nonempty range, even when that value does not meet `threshold`.
- **Inclusive endpoints:** Both `left` and `right` belong to the query; binary-search bounds must count indexes equal to either endpoint.
- **Single-element range:** Its sole value is the candidate and satisfies the only legal threshold of $1$.
