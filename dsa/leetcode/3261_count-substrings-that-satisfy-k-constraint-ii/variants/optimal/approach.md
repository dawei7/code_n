## General

Let $n$ be the string length and $q$ the query count.

**Precompute both views of the valid window**

A substring is invalid only when both its zero and one counts exceed $k$. Scan a sliding window with right boundary increasing. Whenever both counts become too large, the current right index is the first invalid end for the current `left`; record `right - 1` as that start's rightmost valid end, remove its bit, and advance `left`.

After shrinking, `left` is the earliest valid start for the current ending index. Thus `right - left + 1` valid substrings end there. Store a prefix sum of these ending counts. Starts never displaced by the window remain valid through the final string position.

**Split each query into a triangle and a tail**

For a query `[L, R]`, let `P = min(R, rightmost_valid[L])`. The whole substring `s[L..P]` is valid, so every one of its contained substrings is valid. These contribute the triangular count

$$
\frac{(P-L+1)(P-L+2)}{2}.
$$

For ending positions after $P$, `L` is no longer a valid start. Their globally precomputed earliest valid starts are strictly greater than `L`, so every valid suffix ending there already lies inside the query. One subtraction from the ending-count prefix sum supplies that tail.

The sliding window records the exact transition between valid and invalid ends for each start, because adding characters cannot restore a substring once both counts exceed $k$. The triangular part therefore covers exactly all query substrings ending through $P$. Later valid substrings are counted exactly by their ending positions in the prefix-sum tail. The two parts are disjoint and exhaustive.

## Complexity detail

Each string boundary advances at most $n$ times, so preprocessing is $O(n)$. Every query performs constant arithmetic and two prefix accesses, for $O(q)$ additional time and $O(n+q)$ total. The rightmost-end and prefix arrays use $O(n)$ auxiliary space; the returned $q$ answers are output space.

## Alternatives and edge cases

- **Run a sliding window per query:** Correctly counting each range independently can take $O(nq)$ total time.
- **Binary-search earliest starts:** A nondecreasing boundary array supports $O(\log n)$ queries, but the rightmost-valid-start view removes that logarithm.
- **Count all substrings per query:** Nested start/end loops can become quadratic for each range.
- **Treat OR as AND:** Shrinking when either count exceeds $k$ rejects valid one-bit-heavy substrings.
- A singleton query always returns one.
- Homogeneous ranges have every substring valid.
- If `k` is at least the query length, the answer is the full triangular count.
- Query ranges are inclusive at both ends.
- Counts can exceed 32-bit range for long ranges.
- Queries may overlap, but each answer is independent and must preserve input order.
