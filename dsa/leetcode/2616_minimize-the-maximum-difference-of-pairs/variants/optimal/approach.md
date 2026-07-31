## General

Sort the values. For a proposed maximum difference $x$, ask whether at least `p` disjoint pairs can be formed with difference at most $x$.

Scan the sorted array from left to right. Whenever two adjacent unused values differ by at most $x$, pair them and skip both. Otherwise skip only the smaller value. This greedy choice maximizes the number of valid pairs: pairing the current smallest unused value with its closest possible partner consumes no larger value than any alternative, leaving an equally favorable suffix for the remaining pairs.

Feasibility is monotone. If threshold $x$ permits `p` pairs, every larger threshold also permits them; if it does not, every smaller threshold also fails. Binary-search the smallest feasible threshold from $0$ through the complete value range.

The greedy scan correctly decides each threshold by the exchange argument above. Binary search preserves the invariant that the optimum remains in the current interval and terminates at its smallest feasible value, which is exactly the minimum possible maximum pair difference.

## Complexity detail

Let $n$ be the array length and define

$$
D=\max(\texttt{nums})-\min(\texttt{nums})+1.
$$

Sorting costs $O(n\log n)$. Each feasibility check costs $O(n)$ and binary search performs $O(\log D)$ checks, for total time $O(n\log n+n\log D)$. The sorted copy uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming:** After sorting, a recurrence can either skip the current value or pair the last two values, but tracking every pair count costs $O(np)$ time.
- **Enumerate candidate thresholds:** Testing sorted adjacent differences in increasing order avoids numeric binary search but needs additional ordering or repeated scans.
- **Zero pairs:** The defined maximum of the empty pair set is zero, so no sorting or search is necessary.
- **Duplicate values:** A threshold of zero can pair equal values.
- **Maximum pair count:** When $p=\lfloor n/2\rfloor$, every usable index must belong to a pair; the greedy feasibility scan still applies.
- **Unpaired values:** Forming exactly `p` pairs allows all remaining indices to be ignored.
- **Large numeric range:** Binary search depends logarithmically on values up to $10^9$ rather than allocating by value.
