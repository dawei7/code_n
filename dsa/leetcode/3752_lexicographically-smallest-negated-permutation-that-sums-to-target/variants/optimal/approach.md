## General

Let

$$
S=\frac{n(n+1)}{2},
$$

the sum when every magnitude is positive. Negating a subset whose magnitudes sum to $X$ changes the total from $S$ to $S-2X$. Therefore, the required negative-magnitude sum is

$$
X=\frac{S-\texttt{target}}{2}.
$$

A solution exists exactly when $\lvert\texttt{target}\rvert\le S$ and $S-\texttt{target}$ is even. Every integer subset sum from $0$ through $S$ is attainable with the consecutive magnitudes $1,2,\ldots,n$.

For any fixed signs, sorting the signed values produces its lexicographically smallest arrangement: negative values appear from largest magnitude to smallest, followed by positive values from smallest magnitude to largest. Choosing the signs can consequently be viewed from magnitude `n` down to `1`, preferring to negate the current value whenever possible.

If the remaining sum $X$ is at least the current magnitude $v$, negate $v$ and subtract it. This choice remains feasible because the prior invariant $X\le v(v+1)/2$ implies $X-v\le v(v-1)/2$, the sum of all smaller magnitudes. If $X<v$, including $v$ is impossible. Preferring every feasible larger negative value makes the earliest differing sorted element as small as possible, establishing lexicographic minimality.

## Complexity detail

The descending sign-selection pass and the two output passes each inspect the $n$ magnitudes once, for $O(n)$ time. The sign markers and returned array use $O(n)$ space; excluding required output storage, the markers still use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Subset-sum dynamic programming:** It can find a sign assignment but is far too expensive for $n=10^5$ and does not automatically enforce lexicographic minimality.
- **Enumerate sign assignments:** Trying all $2^n$ subsets is infeasible and then still requires choosing the smallest arrangement.
- **Feasibility by magnitude:** A target outside $[-S,S]$ cannot be reached even when every sign points in the needed direction.
- **Feasibility by parity:** Every sign change alters the all-positive sum by an even amount, so `target` must have the same parity as $S$.
- **All positive:** When `target == S`, the answer is `[1,2,...,n]`.
- **All negative:** When `target == -S`, the answer is `[-n,...,-2,-1]`.
- **Array order:** Returning selected signs in magnitude order is not enough; the final signed values must be in ascending order for the lexicographically smallest permutation.
