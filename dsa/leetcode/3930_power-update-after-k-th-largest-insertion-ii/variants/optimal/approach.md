## General

**Compress the complete value domain without reordering the queries**

Every value that can ever enter the multiset is already present either in `nums` or as the first component of a query. Collect these values, remove duplicates, and sort them into

$$
c_1<c_2<\cdots<c_U.
$$

Map each value to its one-based position in this list. This preprocessing does not execute the queries early: insertions and updates to `p` still occur strictly in query order. It only gives every possible value a compact ordered coordinate.

**Store multiplicities in a Fenwick tree**

A Fenwick tree over the $U$ compressed coordinates stores how many copies of each value are currently present. Insert every initial element, preserving duplicate counts, then process one query at a time. Inserting `val_i` is a point-frequency increment in $O(\log U)$ time.

After query $i$ inserts its value, let $L=N+i+1$ be the current multiset size. The `k_i`th largest element is the

$$
r=L-k_i+1
$$

th smallest element. This converts the requested descending rank into an ascending prefix-count target.

**Select the compressed coordinate by binary lifting**

Fenwick binary lifting finds the smallest coordinate whose prefix frequency is at least $r$. Starting below the first coordinate, try powers of two from largest to smallest. A tentative jump is accepted exactly when the entire Fenwick block reached by that jump contains fewer than the remaining target count; subtract that block count and continue to the right. When no jump remains, the next coordinate is the desired one.

Suppose binary lifting returns the coordinate for value $x$. Exactly $r-1$ stored elements lie before that coordinate, while including it reaches or passes $r$, so $x$ is the $r$th smallest value. By the rank conversion above, it is also the requested `k_i`th largest value. Multiplicities are frequencies rather than set membership, so equal elements occupy all of their proper rank positions.

Finally compute `p = pow(p, x, 1_000_000_007)` and append the result. Python's three-argument `pow` performs fast modular exponentiation without constructing the enormous integer $p^x$. Because the next query uses this updated `p`, sequential processing produces exactly the requested answer list.

## Complexity detail

Let $U\le N+Q$ be the number of distinct values and let $V$ be the largest value. Sorting the compressed domain costs $O(U\log U)$. The $N$ initial insertions and $Q$ query insertions each take $O(\log U)$, as does every order-statistic selection. Modular exponentiation for exponent $x\le V$ takes $O(\log V)$ time.

The total bound is

$$
O\bigl(U\log U+(N+Q)\log U+Q\log V\bigr)
=O\bigl((N+Q)\log(N+Q)+Q\log V\bigr).
$$

The sorted values, coordinate map, Fenwick tree, and answer use $O(U+Q)=O(N+Q)$ auxiliary space.

The benchmark defines size as the query count $Q$, starts from one value, and uses distinct pseudo-random insertions with varying legal ranks. The accepted method takes $O(Q\log Q)$ time on these tiers. A control that re-sorts the whole growing multiset for every query takes $O(Q^2\log Q)$ on the same inputs.

## Alternatives and edge cases

- **Sort after every insertion:** Append the new value, sort all current values, and index the requested rank. This is easy to verify but costs $O(Q^2\log(N+Q))$ across the full sequence.
- **Maintain one sorted Python list:** Binary search locates an insertion point, but shifting the suffix still costs $O(N+Q)$ per insertion and remains quadratic overall.
- **Two heaps for one fixed rank:** Heaps work well when every query asks for the same `k`, but `k_i` may jump anywhere from the largest to the smallest current element, so a fixed partition does not support all ranks efficiently.
- **Balanced order-statistic tree:** A tree augmented with subtree multiplicities gives the same asymptotic update and selection bounds, but Python's standard library has no such container; compression plus Fenwick storage is simpler here.
- **Duplicate values:** Increment frequencies for every copy. Coordinate compression merges equal keys, not their multiplicities.
- **Largest and smallest ranks:** `k_i = 1` becomes ascending rank $L$, while `k_i = L` becomes ascending rank one; the same selection routine handles both.
- **Sequential state:** Insert and select before updating `p`, and carry the updated state into the next modular power.
- **Large exponents:** Use modular exponentiation. Computing `p ** x` first is infeasible when $x$ approaches $10^9$.
- **Fenwick index boundary:** Store compressed positions one-based, and translate the selected tree position back to the zero-based sorted-value array carefully.
