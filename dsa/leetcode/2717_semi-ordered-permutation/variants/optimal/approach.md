## General

Let `one_index` be the original position of $1$. Moving it to index $0$ requires exactly `one_index` adjacent swaps: each operation can reduce its index by only one, and repeatedly swapping it with its left neighbor achieves that bound.

Similarly, if `maximum_index` is the original position of $n$, moving it to the last index independently requires $n-1-\texttt{maximum_index}$ swaps.

When $1$ originally lies to the left of $n$, their movements never cross and the distances simply add. When $1$ lies to the right, they must cross exactly once. That crossing swap moves $1$ one position left and $n$ one position right at the same time, so it was counted twice by the independent distances and one must be subtracted.

The minimum is therefore

$$
\texttt{one_index} + n - 1 - \texttt{maximum_index}
- [\texttt{one_index} > \texttt{maximum_index}],
$$

where the bracketed condition contributes one when true and zero otherwise. The lower bounds from endpoint distances and the direct neighbor-swapping construction show that this value is both necessary and attainable.

## Complexity detail

Finding the positions of $1$ and $n$ takes $O(n)$ time. The formula then takes $O(1)$ time and uses $O(1)$ auxiliary space. The benchmark uses `size` as $n$ and contrasts the direct calculation with repeatedly searching the current permutation before each simulated swap.

## Alternatives and edge cases

- **Simulate adjacent swaps:** This is correct, but linearly locating an endpoint again before every swap can take $O(n^2)$ time.
- **Build a position map:** Recording every value's position takes $O(n)$ space, although only the positions of $1$ and $n$ are needed.
- **Sort the whole permutation:** Full sorting does unnecessary work because middle values have no required order.
- An already semi-ordered permutation needs zero swaps.
- For `[2,1]`, one swap simultaneously puts both endpoints in place.
- The overlap subtraction applies only when $1$ starts to the right of $n$.
- If either endpoint is already correct, its individual distance contributes zero.

