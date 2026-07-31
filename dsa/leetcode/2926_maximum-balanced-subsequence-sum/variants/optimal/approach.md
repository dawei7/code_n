## General

**Expose the order hidden in the balance inequality.** Suppose consecutive
chosen indices are $p<q$. Their required relation can be rearranged as

$$
\texttt{nums}[q]-\texttt{nums}[p]\ge q-p
\iff
\texttt{nums}[p]-p\le\texttt{nums}[q]-q.
$$

Define the transformed key $b_i=\texttt{nums}[i]-i$. A subsequence is balanced
exactly when its selected keys are non-decreasing. This equivalence applies to
each consecutive pair, so it characterizes the complete subsequence.

**Dynamic programming by the last key.** Let the state ending at index $i$ be
the greatest sum of a balanced subsequence whose final element is `nums[i]`.
It may start at $i$, or extend any earlier state with key at most $b_i$:

$$
\texttt{dp}[i]=\texttt{nums}[i]+\max\left(0,
\max_{j<i,\ b_j\le b_i}\texttt{dp}[j]\right).
$$

The zero option starts a new subsequence when every compatible earlier sum is
harmful. The overall answer is still tracked from actual states, which is
essential when all values are negative.

**Answer prefix maxima efficiently.** Coordinate-compress all keys while
preserving their order. A Fenwick tree stores the maximum DP value seen at
each rank and answers the maximum over every rank up to the current one.
Querying the current rank inclusively permits equal transformed keys, matching
the non-strict inequality. Processing indices left to right ensures every
stored state comes from an earlier position. The recurrence considers every
legal predecessor and selects its best state, so each computed state is
optimal; taking the maximum of all ending states is therefore the required
non-empty subsequence sum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Sorting the transformed keys costs
$O(n\log n)$ time. Each of the $n$ Fenwick queries and updates costs
$O(\log n)$, so total time is $O(n\log n)$. The keys, compressed order, and
Fenwick tree use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Check all earlier indices for every endpoint; it implements the same recurrence directly but takes $O(n^2)$ time.
- **Segment tree:** Range-maximum queries over compressed keys also achieve $O(n\log n)$ time, with more machinery than the Fenwick tree needs for prefix ranges.
- **Longest-increasing-subsequence tails:** Standard tails preserve minimum ending values for each length, not maximum weighted sums, so they do not solve this weighted objective.
- **Equal transformed keys:** They may follow one another because balance requires a non-decreasing, not strictly increasing, key sequence.
- **Negative compatible sums:** Extending them can only reduce the current sum; the zero option correctly starts a new singleton state.
- **All-negative input:** The answer must be the largest single value rather than zero, because the selected subsequence must be non-empty.
- **Large totals:** Up to $10^5$ values of magnitude $10^9$ may contribute, so fixed-width implementations need 64-bit sums.
