## General

**First decide whether any valid arrangement exists.** For a value `x`, let `nums_count[x]` be its number of copies in `nums` and `forbidden_count[x]` the number of indices that reject it. Those copies have only `N - forbidden_count[x]` legal destinations. Therefore, if

`nums_count[x] + forbidden_count[x] > N`,

the task is impossible. Conversely, these per-value capacity conditions are sufficient: each item value is excluded only from the one group of positions that forbids that same value, so no larger combination of value groups introduces a tighter destination restriction.

**Only currently bad indices need repair.** Call index `i` bad when `nums[i] == forbidden[i]`. Let `B` be the number of bad indices, and let `F` be the largest number of bad indices sharing one value.

One swap can repair at most two bad indices, which gives the lower bound $\lceil B/2\rceil$. Also, a swap between two bad indices holding the same value repairs neither of them. Every one of the `F` occurrences in the largest same-value bad group must therefore participate in a different useful swap, giving the second lower bound $F$.

These bounds are attainable. When no bad value occurs more than half the time, bad indices of different values can be paired; if `B` is odd, one final three-value cycle takes two swaps. This uses $\lceil B/2\rceil$ swaps. When one value `x` is dominant, pair each non-`x` bad index with an `x` bad index. Any remaining `x` indices swap with already-good helper indices whose current and forbidden values are both different from `x`. The feasibility inequality guarantees enough such helpers. The total is then exactly `F` swaps.

Thus, after feasibility succeeds, the answer is

$$
\max\left(F,\left\lceil\frac{B}{2}\right\rceil\right).
$$

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. A constant number of scans and expected-constant-time hash-table updates take expected $O(N)$ time. The frequency maps can contain $O(N)$ distinct values, so the auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Explicit swap construction:** Materialize the pairings and helper swaps rather than returning only their count. This can remain linear but adds bookkeeping that the requested output does not require.
- **Repeated frequency scans:** Count each distinct value by rescanning both arrays. It proves the same feasibility condition but can take $O(N^2)$ time.
- **Already valid:** With `B = 0`, both lower bounds are zero and the answer is `0`.
- **Global impossibility:** Feasibility depends on every occurrence of a value, not only its currently bad occurrences.
- **Same-value bad indices:** Swapping equal values changes nothing, which is why the largest bad group creates an independent lower bound.
- **Odd bad count:** At least one swap repairs only one remaining bad position, producing the ceiling in $\lceil B/2\rceil$.
- **Duplicate values:** Counts, rather than individual identities, determine both destination capacity and the dominant bad group.
