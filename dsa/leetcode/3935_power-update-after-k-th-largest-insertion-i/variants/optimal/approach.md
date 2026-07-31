## General

**Maintain an ordered partition rather than one global order.** Keep two heaps:

- `top` is a min-heap containing exactly the largest values required by the current rank. Its smallest element, `top[0]`, is therefore the current `k`th largest value.
- `remaining` is a max-heap, represented with negated values, containing every other inserted or initial value.

The partition invariant is that every value in `top` is at least every value in `remaining`. Initially, heapify all values into `remaining` and leave `top` empty; the first query establishes its possibly large requested rank.

**Insert without breaking the boundary.** If `top` is nonempty and a new value is at least its minimum, push the value into `top`. Otherwise push it into `remaining`. This classification preserves the ordering invariant, although `top` may temporarily have the wrong size.

Rebalance to the query's requested `k`. While `top` is too large, move its minimum to `remaining`; that is the correct value to remove from the largest partition. While `top` is too small, move the maximum of `remaining` into `top`; that is the correct next value to add. Both operations preserve the partition ordering. Once `len(top) == k`, the invariant proves that `top` contains exactly the largest `k` values with multiplicity, so `top[0]` is the requested exponent.

Apply modular exponentiation to update `p`, append that new state, and continue. The first rebalance may move up to $N+1$ elements because `k_0` is unrestricted. Every later query inserts one element and changes the target heap size by fewer than ten, so only a constant number of values move across the boundary. The heaps therefore perform only $O(N+Q)$ pushes and pops over the complete run.

## Complexity detail

Let $N$ be the initial length, $Q$ the query count, and $V$ the maximum array or inserted value. Initial heap construction takes $O(N)$ time. There are $O(N+Q)$ total heap operations, each costing $O(\log(N+Q))$. Fast modular exponentiation costs $O(\log V)$ multiplications per query because the selected exponent is at most $V$. The total time is

$$
O((N+Q)\log(N+Q)+Q\log V).
$$

The two heaps together store every current multiset element once, and the returned array stores $Q$ results, giving $O(N+Q)$ auxiliary and output storage.

The benchmark defines size as the query count $Q$, keeps `k = 1`, and uses equal values so every selected exponent is known. The accepted heap partition processes each insertion incrementally, while re-sorting the entire growing multiset after every query performs quadratic total element work across the tiers.

## Alternatives and edge cases

- **Sort after every insertion:** This directly reveals any requested rank and is easy to verify, but repeatedly ordering a growing array takes $O(Q(N+Q)\log(N+Q))$ time in the worst case.
- **Coordinate compression plus Fenwick tree:** An offline compression of all initial and inserted values supports arbitrary order-statistic queries in $O((N+Q)\log(N+Q)+Q\log V)$ time. It does not exploit the bounded change between consecutive ranks and needs a more involved selection routine.
- **One fixed-size heap:** A single heap works when `k` never changes, but cannot recover efficiently when a later query asks for values that were discarded outside the previous top set.
- **Duplicate values:** Equal elements occupy separate multiset ranks. Either heap may hold copies at the boundary without changing the selected value.
- **First requested rank:** `k_0` can be as large as the complete post-insertion multiset. The initial transfer from `remaining` to `top` must allow all of those elements to move.
- **Rank movement in either direction:** An increase moves the greatest remaining values into `top`; a decrease moves the smallest top values out. The strict difference bound applies in both directions.
- **Sequential modular state:** Use the newly computed `p` as the base for the next query, not the original input value.
