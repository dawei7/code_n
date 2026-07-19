## General
**Express all three sums with prefixes**

Build `prefix` so `prefix[i]` is the sum of the first `i` elements. If `left_end` and `middle_end` are the two exclusive boundaries, the part sums are `prefix[left_end]`, `prefix[middle_end] - prefix[left_end]`, and `prefix[n] - prefix[middle_end]`.

For a fixed non-empty left part, valid middle boundaries satisfy both

$$
\texttt{prefix[middle\_end]} \ge 2\texttt{prefix[left\_end]}
$$

and

$$
2\texttt{prefix[middle\_end]}
\le \texttt{prefix[n]}+\texttt{prefix[left\_end]}.
$$

The middle boundary must also remain below $n$ so the right part is non-empty.

**Maintain the valid boundary interval**

Because every array value is non-negative, prefix sums never decrease. For each successive `left_end`, advance one pointer to the first middle boundary satisfying the lower inequality. Advance a second pointer to the first boundary violating the upper inequality. Every index in the half-open interval between those pointers is valid, so add its length.

Neither pointer ever moves backward. The first pointer excludes middle sums that are too small; the second excludes middle sums that are too large relative to the remaining suffix. The derived inequalities prove that every boundary retained between them satisfies both original sum conditions, and monotonicity proves no skipped earlier boundary can become valid later.

## Complexity detail
Building the $n+1$ prefix sums takes $O(n)$ time and space. The outer loop advances across possible left boundaries, while each middle pointer advances at most $n$ times in total. The sweep therefore takes $O(n)$ time, and the prefix list uses $O(n)$ space.

## Alternatives and edge cases
- **Enumerate both cuts:** checking every boundary pair directly takes $O(n^2)$ time.
- **Binary search for each left boundary:** monotone prefixes support two binary searches per left boundary in $O(n\log n)$ time, but persistent pointers remove the logarithmic factor.
- **Allow an empty part:** boundaries must satisfy `1 <= left_end < middle_end < n`; including either endpoint changes the contract.
- **Zero values:** equal adjacent prefix sums create multiple distinct cut positions, all of which must be counted.
- **All zeros:** every legal pair of cuts is valid even though all three sums are equal.
- **Equality:** both comparisons are non-strict, so boundaries producing equal neighboring sums belong in the interval.
- **No valid interval:** when the lower pointer reaches or passes the upper pointer, that left boundary contributes zero.
- **Large counts:** apply the required modulus while or after accumulating interval lengths.
