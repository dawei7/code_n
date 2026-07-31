## General

Let $M=\max(\texttt{nums})$. Store the frequency of every value from 1 through $M$. For a candidate divisor $d$, sum the frequencies at $d,2d,3d,\ldots$; call this count $c_d$. Any two of those elements have a GCD divisible by $d$, so there are $\binom{c_d}{2}$ pairs whose GCD is some multiple of $d$.

Process divisors downward. When handling $d$, the exact pair counts for every proper multiple $2d,3d,\ldots$ are already known. Subtract those counts from $\binom{c_d}{2}$. Every pair counted initially has one unique exact GCD that is a multiple of $d$, so this inclusion-exclusion leaves exactly the number of pairs whose GCD equals $d$.

Turn the exact counts into an ascending cumulative array: `cumulative[d]` is the number of conceptual pair values at most $d$. A zero-based query `query` belongs to the first GCD value whose cumulative count is strictly greater than `query`. `bisect_right(cumulative, query)` returns precisely that value, without constructing or sorting the quadratic pair multiset.

All pair counts and cumulative totals may reach $\binom{10^5}{2}$, so they require integer arithmetic wider than 32 bits in languages with fixed-width numeric types.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$, $q=\lvert\texttt{queries}\rvert$, and $M=\max(\texttt{nums})$. The two multiple loops perform $\sum_{d=1}^{M}O(M/d)=O(M\log M)$ iterations. Frequency and prefix construction cost $O(n+M)$, and the queries cost $O(q\log M)$ by binary search. Total time is $O(n+M\log M+q\log M)$ and the arrays use $O(M)$ space.

## Alternatives and edge cases

- **Enumerate and sort all pairs:** This requires $\Theta(n^2)$ GCD computations and storage, which is infeasible for $n=10^5$.
- **Binary search with repeated divisor counts:** Recomputing the number of pairs below every trial GCD repeats sieve work across queries; one cumulative distribution shares that work.
- **Duplicate values:** Frequency counts naturally include the $\binom{f}{2}$ pairs formed by two occurrences of the same value.
- **Absent GCD values:** Consecutive cumulative entries may be equal; `bisect_right` skips them until reaching a value with positive multiplicity.
- **Repeated queries:** Each query is answered independently, so identical ranks correctly produce identical GCDs.
- **Zero-based ranks:** The comparison must find the first cumulative total strictly greater than the query, not greater than or equal to it.
