## General

Choose an ordered pair of distinct colors `(i, j)`. If the first segment has length $x$, then the second has length $n-x$. Because both segments are nonempty, a color can never use more than $n-1$ sheets; replace every limit by

$$
a_i = \min(\texttt{limit[i]}, n-1).
$$

For fixed colors, the valid split lengths satisfy $n-a_j \leq x \leq a_i$. Their count is therefore

$$
\max(0, a_i+a_j-(n-1)).
$$

Let $T=n-1$ and sort the capped limits. For each first-color value $a_i$, binary search for the first sorted value strictly greater than $T-a_i$. Every value $a_j$ in that suffix contributes $a_i+a_j-T$. A prefix-sum array gives the entire suffix contribution as

$$
k(a_i-T)+\text{suffixSum},
$$

where $k$ is the suffix length. This sum temporarily includes pairing the color with itself when $2a_i>T$; subtract `2 * a_i - T` in that case. Color identities remain distinct even when their limits are equal, because every array entry participates separately in the iteration and suffix count.

The pair formula counts exactly one term for every legal split of every ordered pair. The suffix query aggregates precisely the partners with a positive term, and removing the self term enforces the requirement that the two colors be distinct. Thus the final sum counts every valid painting once.

## Complexity detail

Let $M=\lvert\texttt{limit}\rvert$. Sorting and building prefix sums take $O(M\log M)$ and $O(M)$ time, respectively. Each color performs one $O(\log M)$ binary search and constant-time arithmetic, so total time is $O(M\log M)$. The capped sorted values and prefix sums use $O(M)$ auxiliary space. Reduce the accumulated answer modulo $10^9+7$.

## Alternatives and edge cases

- **Enumerate ordered color pairs:** Applying the closed-form split count to all $M(M-1)$ pairs is correct but costs $O(M^2)$ time.
- **Enumerate split positions:** Iterating $x$ from `1` through `n - 1` is infeasible because $n$ can be $10^9$.
- **Treat color pairs as unordered:** `(i, j)` and `(j, i)` paint opposite segments and are distinct ways under the problem's note.
- **Allow one empty segment:** Capping at $n-1$ and using the derived interval enforce that each of the exactly two colors appears at least once.
- **Equal limits:** Different indices still name different colors, so equal numeric capacities must not be deduplicated.
- **Limits larger than `n`:** Values above $n-1$ are equivalent because neither segment may contain all $n$ sheets.
