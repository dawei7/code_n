## General

Assign each value a group number: `0` when it is less than `a`, `1` when it lies in inclusive range `[a, b]`, and `2` when it is greater than `b`. A good array is exactly an array whose group numbers are non-decreasing. Values within the same group do not need any particular order.

An adjacent swap can remove at most one inversion of this group-number sequence, where an inversion is an earlier group number that is larger than a later one. Conversely, repeatedly swapping inverted neighboring groups sorts the sequence using exactly one swap per inversion. The required minimum is therefore the inversion count.

Because there are only three groups, count those inversions directly during one left-to-right scan. Maintain how many middle-group and high-group values have already appeared. A new low-group value forms an inversion with every prior middle or high value, so add both counts. A new middle-group value forms an inversion only with prior high values, so add the high count before incrementing the middle count. A high-group value cannot be the right endpoint of an inversion and only increases the high count.

Every inversion is counted exactly once when its right endpoint is processed, and no non-inverted pair contributes. The accumulated total is therefore both attainable and a lower bound on every adjacent-swap sequence. Reduce it modulo $10^9+7$ for the required return value.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan examines each element once and performs constant work per element, taking $O(n)$ time. The counters and running total use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Merge-sort inversion counting:** Sorting the group sequence while merging also counts inversions, but it costs $O(n\log n)$ time and $O(n)$ auxiliary space for a problem with only three categories.
- **Fenwick tree over three groups:** A frequency tree can count earlier greater groups in $O(n\log 3)$ time, which is asymptotically linear but adds unnecessary data-structure overhead.
- **Explicit adjacent swaps:** Simulating bubble sort realizes the minimum number of swaps but can take $O(n^2)$ time.
- **Empty parts:** If one or two groups are absent, the same inversion rule remains valid; no special partition boundaries are needed.
- **Boundary values:** Values equal to `a` or `b` belong to the middle group because `[a, b]` is inclusive.
- **Repeated values:** Equal values receive the same group number and never form an inversion with one another.
- **Modulo:** Count with a wide integer and reduce by $10^9+7$ before returning, because the unreduced inversion count can exceed 32-bit range.
