## General
**Fix endpoints and optimize the interior greedily**

Suppose equal values at indices $i<j$ are chosen as the required endpoints. Those two flowers cannot be removed. Every flower strictly between them is optional. Keeping a positive interior value increases the sum, while keeping a negative value decreases it; zeros do not affect the total.

Therefore the best garden for these endpoints has score

$$
2\cdot\texttt{flowers[i]}
+ \sum_{i<t<j}\max(\texttt{flowers[t]},0).
$$

This reduces the problem from choosing an arbitrary subsequence to choosing the best pair of equal endpoints.

**Rewrite each pair score with a positive prefix**

While scanning, let $P$ be the sum of positive values strictly before the current index. For a previous endpoint of beauty $v$, store its endpoint contribution after removing positive values at or before that start:

$$
v-P_{\mathrm{after\ start}}.
$$

At a later occurrence of the same $v$, add the current endpoint $v$, the current positive prefix, and the stored start contribution. The prefix terms cancel everything outside the endpoints and retain exactly the positive interior flowers.

**Keep the best start for each beauty**

Use a hash map from beauty value to the largest start contribution seen for that value. Evaluate a current flower as an ending endpoint before adding it to the positive prefix, ensuring it is not counted as an optional interior flower. Then update its possible start contribution after the prefix includes it.

For every possible endpoint pair, the formula computes its optimal interior sum. The map retains the best previous start compatible with each ending value, so taking the maximum candidate considers the optimum among all valid gardens.

## Complexity detail
The scan processes each of the $n$ flowers once and performs expected constant-time hash-map operations, giving $O(n)$ time. The map stores at most one entry for each of the $U$ distinct beauty values, so auxiliary space is $O(U)$.

## Alternatives and edge cases
- **Enumerate endpoint pairs:** For every equal pair, compute or update its positive interior sum. This is correct but can take $O(n^2)$ time when many flowers share one beauty.
- **Maximum-subarray methods:** A valid garden may remove negative values from the middle while retaining positive values on both sides, so the remaining flowers need not be contiguous.
- **Store every occurrence:** Position lists can support prefix-sum pair calculations, but the single best adjusted start per value is sufficient.
- **Exactly two flowers:** Equal endpoints alone form a valid garden, even when their total is negative.
- **Negative endpoints:** They must remain, but enough positive interior beauty may make that pair optimal.
- **All nonpositive values:** Remove every interior value and choose the repeated endpoint value with the largest doubled beauty.
- **Repeated endpoint value:** A later ending occurrence may capture additional positive interior flowers; evaluate every occurrence.
- **Positive flowers outside the endpoints:** They cannot be retained because doing so would change which flowers are first or last.
- **Large sums:** Up to $10^5$ values of magnitude $10^4$ may contribute, so fixed-width implementations should use a sufficiently wide integer type.
