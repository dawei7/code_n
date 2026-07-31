## General

There are only five possible characters, so enumerate each of the $5\cdot4$ ordered choices for the odd-frequency character `a` and the positive-even-frequency character `b`. For one fixed pair, let $A_i$ and $B_i$ be their counts in the prefix ending just before position $i$. A substring from prefix boundary $l$ to boundary $r$ has the desired difference

$$
(A_r-B_r)-(A_l-B_l).
$$

Its `a` count is odd exactly when $A_l$ and $A_r$ have opposite parity. Its `b` count is even exactly when $B_l$ and $B_r$ have the same parity. Therefore, for each of the four prefix-parity combinations, retain the smallest previously eligible value of `A_l - B_l`; subtracting the smallest compatible value maximizes the current substring's difference.

A prefix boundary `l` becomes eligible for a right boundary `r` only if `l <= r - k`, which enforces the minimum length, and `B_l <= B_r - 2`, which ensures the even `b` count is positive rather than zero. Both thresholds move monotonically as `r` advances. Because prefix `b` counts never decrease, a single pointer can add every newly eligible left boundary in order. If its current boundary has too many `b` characters, no later boundary can yet satisfy the positive-even requirement.

For every right boundary, query the parity state opposite to $A_r$ and equal to $B_r$. Each recorded prefix already satisfies both eligibility inequalities, and each compatible prefix produces odd `a` frequency and positive even `b` frequency. Conversely, every valid substring is considered when its right boundary is processed, so taking the largest candidate over all right boundaries and ordered pairs yields the required maximum.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. There are exactly twenty ordered pairs of distinct digits. Building two prefix arrays and scanning them takes $O(n)$ time per pair, so the fixed alphabet keeps the total time at $O(n)$. The two prefix arrays use $O(n)$ space; the parity table itself has only four entries.

## Alternatives and edge cases

- **Enumerate every substring:** Updating counts incrementally still examines $O(n^2)$ substrings, which is too slow for $n=3\cdot10^4$.
- **Track parity without occurrence counts:** Parity alone would accept a zero frequency for `b`; requiring at least two occurrences is essential.
- **Use one unordered digit pair:** The objective is directional, so swapping the odd and even roles can change both validity and the difference.
- **Negative optimum:** A valid odd count may be smaller than the required positive even count, so initializing the answer to zero would be incorrect.
- **Additional characters:** Digits other than the selected pair may appear freely and still contribute to the substring length.
- **Minimum length:** Prefix boundary `l` is recorded only after `l <= r - k`, including the exact-length case.
