## General
**Count occurrences before choosing pairs.** Store the multiplicity of every value. Pairing decisions then consume counts without depending on the input order.

**Process smaller absolute values first.** Sort the distinct values by absolute value. For a nonzero value `x`, every remaining occurrence must use an occurrence of `2 * x`. Handling smaller magnitudes first is essential for negative numbers: ordinary numeric order would process `-4` before `-2`, even though `-4` should serve as the double in `(-2,-4)`. If fewer doubles remain than `x` occurrences, pairing is impossible; otherwise subtract that count from `2 * x`.

**Treat zero as its own double.** Since `2 * 0 == 0`, zero occurrences pair among themselves and their count must be even. No nonzero value can use zero as its double. After this special check, the same greedy consumption covers all other values.

When a value is processed, no later, larger-magnitude base can legitimately consume it as a double of a smaller unprocessed magnitude. Thus committing all its occurrences to their only possible doubles cannot invalidate a different valid pairing. If every count can be consumed, the recorded pair choices partition the whole array.

## Complexity detail
Counting takes $O(N)$ time. Sorting at most $N$ distinct values costs $O(N\log N)$, and the greedy scan is linear in the number of distinct values. The frequency map and sorted keys use $O(N)$ space.

## Alternatives and edge cases
- **Repeated unmatched-partner scan:** Process values by absolute magnitude but linearly search all unused occurrences for each required double. It is correct but costs $O(N^2)$ time.
- **Bounded frequency array:** The fixed numeric range permits an indexed count array, trading hash storage for space proportional to the value domain.
- **Ordinary numeric sorting:** Processing negative values from most negative upward is incorrect because a double may be consumed before its half.
- **Odd zero count:** Zero is its own double, so an unpaired zero makes the answer false.
- **Duplicate values:** Counts, not merely set membership, determine whether enough doubles exist.
- **Overflow:** The authored Python solution has unbounded integers; fixed-width implementations should ensure `2 * x` is represented safely.
