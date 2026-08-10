## General

The next chosen value must satisfy two independent restrictions:

1. its index must be at least $k$ after the previous chosen index; and
2. its comparison direction must be the opposite of the previous comparison.

The source uses dynamic programming for the alternating direction and delays each completed state until its index becomes eligible under the distance rule. Two maximum Fenwick trees then find the best eligible predecessor with a strictly smaller or strictly larger value.

**Two states describe the last comparison**

For every index $i$, define:

- `dp[i][1]` as the maximum sum of a valid subsequence ending at $i$ whose last comparison is upward, so the previous selected value is smaller than `nums[i]`;
- `dp[i][0]` as the maximum sum ending at $i$ whose last comparison is downward, so the previous selected value is larger than `nums[i]`.

A singleton has no last comparison and is allowed to act as the beginning of either future pattern. The source initializes both states to `nums[i]`.

To create an upward-ending state at current value $x$:

- the predecessor value must be strictly less than $x$; and
- the predecessor state must be downward-ending, `dp[j][0]`, so directions alternate.

Therefore:

$$
\texttt{dp}[i][1]
=
x+\max_{\substack{j\le i-k\\ \texttt{nums}[j]<x}}
\texttt{dp}[j][0].
$$

The downward transition is symmetric:

$$
\texttt{dp}[i][0]
=
x+\max_{\substack{j\le i-k\\ \texttt{nums}[j]>x}}
\texttt{dp}[j][1].
$$

Taking the maximum with the singleton initialization covers the case where no eligible predecessor improves the sum.

**Coordinate compression preserves strict value order**

Array values can be as large as $10^5$, but only their relative order matters for less-than and greater-than queries.

The source builds `stl = sorted(set(nums))` and assigns one-based ranks:

$$
\operatorname{rank}(v)
=
1+\#\{\text{distinct input values smaller than }v\}.
$$

Equal values receive the same rank. Smaller values have smaller ranks, and larger values have larger ranks.

If current rank is $r$, strictly smaller values occupy ranks $1..r-1$. Excluding rank $r$ correctly prevents equal adjacent selected values, which would violate strict alternation.

**The forward-rank Fenwick tree**

`fwt0` stores maxima of eligible `dp[j][0]` values at their ordinary ranks.

Its `preSum(r - 1)` query returns the maximum state among all ranks strictly smaller than the current rank. Adding current `nums[i]` produces the best upward transition.

The Fenwick tree combines values with `max` rather than addition. An update walks to all tree nodes covering the inserted rank and retains the largest DP sum. A prefix query walks downward and combines the stored maxima covering the requested prefix.

**The reversed-rank Fenwick tree**

A Fenwick tree naturally answers prefix queries, but the downward transition needs values strictly greater than the current value—a suffix in ordinary rank order.

For $M=\lvert\texttt{stl}\rvert$, the source maps ordinary rank $r$ to reversed rank

$$
M-r+1.
$$

Larger values then receive smaller reversed ranks. A current value of ordinary rank $r$ has exactly $M-r$ strictly larger ranks, which become reversed prefix positions $1..M-r$.

`fwt1.preSum(M - r)` therefore returns the best eligible `dp[j][1]` whose predecessor value is strictly greater than the current value. Adding the current value creates a downward-ending state.

Again, equality is excluded because the current value's own reversed rank is $M-r+1$, just beyond the queried prefix.

**Delaying states until the distance is legal**

When processing index $i$, only predecessors $j$ satisfying

$$
j\le i-k
$$

may be queried.

The source ensures the Fenwick trees contain exactly those eligible indices. At the end of iteration $i$, it inserts state

$$
j=i-k+1.
$$

That state is not used for the current $i$. It becomes available at the next iteration $i+1$, where

$$
(i+1)-j=k.
$$

By the time iteration $i$ begins, the most recently inserted index is $i-k$, and all earlier ones have also been inserted. No more recent state is present.

This update-after-query order avoids an off-by-one error. Inserting `i-k+1` before querying would allow a gap of only $k-1$.

For iterations before any predecessor can be $k$ positions away, the trees remain empty and both DP states keep their singleton values.

**Why older states can stay forever**

Once an index becomes distance-eligible, it remains eligible for every later current index. Fenwick entries therefore never need deletion.

The tree stores only the maximum DP value for each covered rank region. A dominated older state with the same or less useful value can never help a later maximum, so retaining only maxima loses no optimal transition.

**A small trace**

For `nums = [5,4,2]` and $k=2$:

- indices 0 and 1 begin only as singletons because no eligible predecessor has yet entered the trees;
- after iteration 1, index 0 is inserted and becomes eligible for index 2;
- current value 2 queries strictly larger predecessors in `fwt1` and finds the state of value 5;
- it forms downward sequence `[5,2]` with sum 7.

No adjacent-index choice is allowed because the gap must be at least two.

**Why the maximum over both states is the answer**

Every nonempty valid subsequence has a final index. If it has length one, it is represented by both singleton states. If longer, its last comparison is uniquely upward or downward and it belongs to the corresponding DP state.

Each transition considers every eligible predecessor value with the required strict relation and opposite prior direction. The Fenwick maximum selects the best sum among them. Thus `res`, updated from both states at every index, covers every valid subsequence and returns the maximum score.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $M$ be the number of distinct values.

Building and sorting the distinct values costs $O(N\log N)$. Rank construction costs $O(M)$.

Each index performs up to two Fenwick prefix queries and later two Fenwick updates. Every operation costs $O(\log M)$, so the dynamic program costs $O(N\log M)$.

Total time is

$$
O(N\log N).
$$

The rank map, sorted values, two Fenwick arrays, and `dp` table each use $O(N)$ or $O(M)$ storage. Total auxiliary space is

$$
O(N).
$$

The source stores every DP row even though each row is inserted exactly once after a fixed delay. A queue of delayed states could reduce some storage organization, but coordinate structures still use $O(N)$ in the worst case.

All values are positive, so zero-initialized Fenwick maxima act as “no predecessor” without incorrectly beating a real DP sum.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Check every prior index for distance, strict comparison, and direction. It is direct but costs $O(N^2)$.
- **Segment trees:** Two max segment trees over compressed ranks provide the same transitions in $O(N\log N)$ time with larger constants.
- **Balanced ordered maps:** They can maintain value-keyed maxima but require explicit prefix/suffix aggregation support.
- **Singleton:** Both states start at `nums[i]`, ensuring every index is a valid candidate by itself.
- **Equal selected values:** Rank queries exclude the current rank, so equality never forms a transition.
- **\(k=1\):** A state from index $i-1$ is inserted before index $i$ is queried, allowing adjacent selections.
- **\(k=n\):** No two distinct indices can satisfy the gap, so the best answer is the largest singleton value.
- **Repeated array values:** Compression merges their rank while DP states remain separate by index and eligibility time.
- **Strict alternation:** Upward states transition only from downward states and vice versa; two consecutive rises or falls cannot enter the DP.
- **Positive-value assumption:** Zero is a safe Fenwick identity because every real subsequence sum is positive.
- **Update timing:** States at index `i-k+1` are inserted only after current queries, becoming legal exactly one iteration later.
- **Input preservation:** Compression and DP use separate structures; `nums` is not modified.
