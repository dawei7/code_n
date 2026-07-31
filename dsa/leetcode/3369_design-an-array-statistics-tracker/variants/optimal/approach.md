## General

The three statistics need different state, so maintain them independently while sharing the same stream updates.

**FIFO removal and mean.** A deque records numbers in insertion order. `addNumber` appends, and `removeFirstAddedNumber` removes from the left. A running total changes with the same two operations, making the floored mean `total // count` without rescanning the collection.

**Upper median with two logical heaps.** Keep the smaller half in a max-heap `lower` (stored as negatives) and the larger half in a min-heap `upper`. Their logical sizes satisfy

$$
\lvert\texttt{lower}\rvert\leq\lvert\texttt{upper}\rvert\leq\lvert\texttt{lower}\rvert+1.
$$

Every logical value in `lower` is no greater than every logical value in `upper`. Therefore `upper[0]` is the middle value for odd cardinality and the larger central value for even cardinality—the problem's exact median convention.

FIFO removal may target a value buried inside either heap. Record that value in a delayed-deletion counter, decrement the appropriate heap's logical size, and physically discard marked values only when they reach a heap root. Rebalancing moves one valid root whenever the logical-size rule is violated. Each stale entry is inserted and removed at most once, so delayed cleanup is amortized.

**Smallest mode from lazy frequency candidates.** A frequency map owns the current count of each value. After an addition, push `(-frequency, value)` into a min-heap. Its order prefers a greater frequency and then a smaller value. Old candidates are not edited in place; `getMode` pops candidates until the stored frequency equals the current map entry. The first valid pair is consequently the most frequent current value, with the required smallest-value tie break.

The accepted native class is preserved unchanged. The app-local `solve(operations, arguments)` adapter constructs it and dispatches the authored operation stream, returning `None` for constructor and update calls.

## Complexity detail

Let $q$ be the total number of calls and $m$ the current number of values. Heap insertion, rebalancing, and each physical stale-entry removal cost $O(\log q)$. Because an entry can become stale and be popped only once, additions, FIFO removals, median queries, and mode queries cost $O(\log q)$ amortized; `getMean` costs $O(1)$. Across the complete operation stream, time is $O(q\log q)$.

The deque, frequency and delayed maps, median heaps, and mode-candidate heap retain at most $O(q)$ total entries, including stale entries awaiting lazy removal. Space is therefore $O(q)$.

The benchmark defines `size` as $n$, uses $n$ insertions followed by $n$ alternating median and mode queries, and has $q=2n$. The reference performs $O(n\log n)$ total heap work. A correct baseline that sorts or recounts all $n$ values for every query requires $\Theta(n^2\log n)$ work and must fail the scaling verdict without failing an output.

## Alternatives and edge cases

- **Recompute all statistics per query:** A list plus sorting and counting is simple and correct, but repeated queries make it quadratic or worse over the operation stream.
- **One ordered multiset:** It supports median updates, but Python has no built-in order-statistics multiset and it does not directly provide FIFO removal or the mode.
- **Two heaps without delayed deletion:** Removing the oldest value can require a linear search inside a heap and destroys the desired update bound.
- **Rebuild heaps after each removal:** It restores valid medians but costs $O(m)$ per FIFO removal.
- **Mode heap without frequency validation:** Stale high-frequency entries can remain above the true current mode after removals.
- **Even cardinality:** The minimum of `upper`, not the maximum of `lower`, selects the larger central value.
- **Duplicate values across both median heaps:** Delayed counts treat equal copies interchangeably while logical sizes preserve the partition invariant.
- **Mode ties:** Heap pairs order by value after frequency, so the smallest equally frequent value wins.
- **Single remaining value:** It is simultaneously the floored mean, upper median, and mode.
- **Large sums:** Python integers grow as needed, so up to $10^5$ values of $10^9$ do not overflow.
