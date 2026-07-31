## General

Only each value's remainder modulo `d` affects divisibility. Process indices
from left to right and treat the current index as `k`, the final position of a
triplet. Maintain `singles[r]`, the number of earlier indices with remainder
`r`, and `pairs[s]`, the number of earlier index pairs whose remainder sum is
`s`.

For current remainder `r`, every earlier pair with sum remainder `-r mod d`
forms one valid ordered-index triplet, so add that pair count. Next combine the
current index with every earlier single remainder to create pairs for future
indices. Only after those two steps add the current remainder to `singles`,
which guarantees the maintained indices always satisfy $i<j<k$.

Inductively, the maps contain exactly all singles and pairs from the processed
prefix. Every triplet is counted once when its largest index arrives, and the
modular complement test accepts it exactly when its sum is divisible by `d`.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. At index `k`, the algorithm iterates over
at most `k` distinct earlier remainders, so total time is $O(N^2)$. Each map
contains at most $N$ distinct remainders, giving $O(N)$ space.

## Alternatives and edge cases

- **Three nested index loops:** Testing every $i<j<k$ directly is correct but takes $O(N^3)$ time.
- **Remainder-frequency combinations:** Counting triples of remainder classes can also achieve $O(U^2)$ time for $U$ distinct remainders, but multiplicity cases require careful combinatorics.
- **Divisor one:** Every integer sum is divisible by one, so all $\binom{N}{3}$ index triplets qualify.
- **Fewer than three elements:** No ordered-index triplet exists and the answer is zero.
- **Duplicate values or remainders:** Counts represent indices, so equal values still create distinct triplets.
- **Large values:** Reducing each value immediately avoids dependence on its magnitude up to $10^9$.
