## Function Contract

**Inputs**

- `nums`: A permutation of the integers from $0$ through $n-1$.
- `pre`: The distinct prefix lengths that may be reversed.

Let $n = \lvert\texttt{nums}\rvert$, $q = \lvert\texttt{pre}\rvert$, and $P=n!$, the maximum number of permutation states.

Each operation chooses one value `x` from `pre` and replaces the prefix `nums[:x]` with its reverse. An allowed length may be used more than once. The operation is conceptual; the function only has to return the distance to the target permutation.

**Return value**

Return the fewest operations that transform `nums` into `[0, 1, ..., n - 1]`. Return `-1` if the target is unreachable.
