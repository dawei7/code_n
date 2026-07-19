## General
**Duplicates disappear because sequence length counts distinct integers**

Build a hash set from the input. Duplicate occurrences do not extend a consecutive-value sequence and would otherwise cause redundant work. Expected constant-time membership makes predecessor and successor checks independent of input order.

**The missing-predecessor test identifies one unique start per run**

A value is the minimum of its maximal consecutive run exactly when `value - 1` is absent. Only from such values, initialize a length and advance while successive integers remain present. Values with predecessors are interior points and never launch a scan.

**Nested loops remain linear because runs are disjoint**

Every counted run begins at its unique minimum. Its inner loop visits each value in that maximal run once. Distinct maximal runs are disjoint, and interior values do not start new loops, so the total number of successful successor advances across all starts is at most the number of distinct values.

**Trace one long run among isolated values**

In `{100,4,200,1,3,2}`, value `1` has no predecessor and expands through `2`, `3`, and `4`, producing length four. Values `2`, `3`, and `4` do not start redundant scans.

**The no-predecessor value uniquely owns each run**

Every maximal consecutive sequence has exactly one smallest value, characterized by the absence of `value - 1`. Starting only there prevents interior values from rescanning the same run.

Incrementing until the first missing successor visits every value in that maximal sequence and stops exactly at its end. Each run is measured once, so the largest recorded length is the longest consecutive sequence.

## Complexity detail
Set construction is $O(n)$ expected time. Although a run has an inner loop, each distinct value is advanced through only from its one sequence start, so total expected time remains $O(n)$. The set uses $O(n)$ space.

## Alternatives and edge cases
- **Sort then scan:** is simple but takes $O(n \log n)$ time.
- **Start a scan at every value:** can become $O(n^2)$ on one long run.
- **Union-find:** can achieve near-linear time but adds more bookkeeping than the start test.
- Empty input returns zero. Duplicate copies of a value never increase a run's length.
- Expected $O(n)$ assumes ordinary expected constant-time hash operations; adversarial hash behavior can weaken that guarantee in some models.
