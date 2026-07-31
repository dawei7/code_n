## Function Contract

**Inputs**

- `nums`: The nonempty initial list of positive integer values.
- `p`: The positive initial state used as the base of the first modular power.
- `queries`: A nonempty list of pairs `[val_i, k_i]`; each pair inserts `val_i` and requests the `k_i`th largest value after that insertion.

Let $N=\lvert\texttt{nums}\rvert$, $Q=\lvert\texttt{queries}\rvert$, and let $V$ be the largest value appearing initially or as an insertion. For zero-based query index $i$, the current multiset contains $N+i+1$ elements after insertion, and `k_i` is guaranteed to be a valid one-based rank in that multiset. Equal values occupy separate rank positions.

All state updates use the modulus

$$
M=10^9+7.
$$

**Return value**

Return a list of length $Q$. Its entry at index $i$ is the updated `p` after inserting `val_i`, selecting the requested order statistic, and computing the modular power. Processing a query never resets `p` to its original value.
