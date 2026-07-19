## General
**Build frequency prefixes.** For every prefix length, store the count of each value from $1$ through $V$. Copy the previous row, increment the current number's entry, and append it. For query `[left, right]`, value $x$ occurs exactly when `prefix[right + 1][x] - prefix[left][x]` is positive.

**Only consecutive present values matter.** Scan the value domain in increasing order. Retain the previous value found in the query range and minimize the difference to the current one. Any nonconsecutive pair in sorted distinct-value order has a gap at least as large as one of the consecutive gaps between it, so no other pair needs examination.

If the scan finds fewer than two values, no valid unequal pair exists and the answer is $-1$. Frequencies, rather than a membership bit alone, allow the same prefix table to answer every range by subtraction.

## Complexity detail
Let $q$ be the query count and $V=100$ the value-domain size. Creating $n$ prefix rows costs $O(nV)$ time and space. Each query scans $V$ values, adding $O(qV)$ time. Total time is $O((n+q)V)$ and space is $O(nV)$.

## Alternatives and edge cases
- **Sort every queried subarray:** It is correct but repeats $O(k\log k)$ work for a range of length $k$ and can become quadratic across overlapping queries.
- **Use a set per query:** The bounded values make sorting the set cheap, but constructing it still scans every element of every range.
- **Duplicate values:** Equal pairs are excluded, so duplicates neither create a zero answer nor alter gaps between distinct values.
- **All values equal:** Return $-1$ for that query.
- **Two distinct values:** Their absolute difference is the only candidate.
- **Inclusive right endpoint:** Query frequency uses the prefix after `right`, namely index `right + 1`.
