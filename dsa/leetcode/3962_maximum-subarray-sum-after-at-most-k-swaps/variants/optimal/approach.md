## General

Fix a candidate subarray and call its multiset of values *inside*; every other value is *outside*. If the inside values are sorted as $a_1 \le a_2 \le \cdots$ and the outside values as $b_1 \ge b_2 \ge \cdots$, then the best result with exactly $t$ useful swaps pairs $a_j$ with $b_j$ for $1 \le j \le t$. Any other pairing can be improved by exchanging partners so that smaller inside values receive larger outside values. The marginal gains $b_j-a_j$ are non-increasing, so the optimal fixed-subarray choice takes the first positive gains, capped by `k`.

Materializing those sorted multisets for every subarray would be too slow. Instead, count how many paired gains are positive. For a value threshold $v$, let $C_I(v)$ be the number of inside values at most $v$, and let $C_O(v)$ be the number of outside values greater than $v$. The number of profitable pairs is

$$
p = \max_v \min\bigl(C_I(v), C_O(v)\bigr).
$$

This identity counts how many small inside values can be matched with strictly larger outside values. Conversely, every positive pair crosses at least one such threshold, so no larger matching can exist.

Let $q$ be the outside size and let $G(v)$ count all array values at most $v$. Because the outside is the complement of the current subarray,

$$
C_O(v)=q-G(v)+C_I(v).
$$

Consequently, $C_I(v)-C_O(v)=G(v)-q$: the point where the smaller count changes sides depends only on the globally sorted array and $q$, not on the chosen subarray. Precompute, for every $q$, the first compressed value whose global prefix count reaches $q$. With duplicate pivot values, the maximum can lie immediately before that value or at it, so compare both counts. One Fenwick prefix query supplies the inside count before the pivot; the frequency at the pivot supplies the second candidate.

Set $t=\min(k,p)$. Two order-statistic sum queries now give the exact gain: subtract the sum of the $t$ smallest inside values and add the sum of the $t$ largest outside values. Fenwick trees store both counts and sums on compressed value ranks. The outside tree is represented implicitly as the fixed whole-array tree minus the current inside tree, and Fenwick bit lifting finds each requested prefix by count.

Enumerate `left`, extend `right`, and insert the new inside value into its count and sum trees. Every nonempty subarray is evaluated, and the fixed-subarray exchange argument proves that its computed value is the best obtainable for those positions. Taking the maximum therefore yields the global optimum.

## Complexity detail

There are $O(n^2)$ nonempty subarrays. Each extension performs a constant number of Fenwick updates, prefix queries, and order-statistic sum queries over at most $M \le n$ ranks, each costing $O(\log n)$ time. Reinitializing the inside arrays for every left endpoint adds $O(nM)$ work and does not exceed the main bound. The total time is $O(n^2\log n)$.

The compressed values, global prefixes, precomputed pivots, frequencies, and Fenwick arrays each contain $O(n)$ entries, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Sort inside and outside for every subarray:** Pairing extremes is direct and correct, but rebuilding both sorted lists costs $O(n^3\log n)$ time across all subarrays.
- **Binary-search every possible swap count:** Fenwick trees can test a proposed count, but an extra binary search per subarray raises the bound to $O(n^2\log^2 n)$; the global crossing identity removes that factor.
- **Zero swaps:** When `k = 0`, every candidate is its original sum, so the enumeration naturally reproduces the ordinary maximum-subarray answer.
- **Duplicate values:** Equal values produce zero gain and must not be counted as profitable; checking both sides of the pivot preserves the strict comparison.
- **All-negative arrays:** The selected subarray must be nonempty, so the answer starts below every legal sum rather than at zero.
- **Large `k`:** A subarray cannot benefit from more pairs than either side contains or more pairs than have positive gain; capping by $p$ handles all of these limits.
