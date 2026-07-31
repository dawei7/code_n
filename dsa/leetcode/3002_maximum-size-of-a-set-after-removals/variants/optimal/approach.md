## General

**Identify the two independent ceilings.** After the removals, each array has
exactly $N/2$ positions. The first array can therefore contribute at most the
smaller of $N/2$ and its number of distinct values; the same statement holds
for the second array.

Adding those two capacities may count shared values twice. The result also
cannot contain more values than the union of both original distinct-value
sets. Therefore the answer is the smaller of the union size and the sum of the
two per-array capacities.

This bound is attainable. Prefer values unique to one array because they can
only consume that array's capacity. Fill remaining positions with shared
values. If the capacity sum is below the union size, every selected capacity
slot can represent a different value. Otherwise the selections can cover the
entire union, distributing shared values between arrays wherever capacity
remains.

## Complexity detail

Constructing the two hash sets and their union takes expected $O(N)$ time and
$O(N)$ auxiliary space. The expectation is the standard average-case bound for
hash-table operations.

## Alternatives and edge cases

- **Separate unique and shared groups:** Counting `values1 - values2`, `values2 - values1`, and the intersection leads to the same greedy capacity calculation.
- **Sort both arrays:** Sorting can derive the distinct counts but costs $O(N\log N)$ time.
- **Explicit uniqueness scans:** Searching a growing list for every value is correct but costs $O(N^2)$ time on distinct inputs.
- **All values identical:** The final set has size one even though many positions remain.
- **Identical distinct sets:** The two arrays may retain different members of the shared set and jointly reach both capacities.
- **Disjoint sets:** Each array contributes up to exactly $N/2$ distinct values.
