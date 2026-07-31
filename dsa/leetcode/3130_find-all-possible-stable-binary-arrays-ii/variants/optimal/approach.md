## General

**Represent the final run without storing its length.** Let $Z[i][j]$ be the number of stable arrays that use $i$ zeroes and $j$ ones and end in `0`; define $O[i][j]$ analogously for arrays ending in `1`. The single-value boundaries contain one valid array while their length is at most `limit`: $Z[i][0]=1$ and $O[0][j]=1$ in that range, and zero beyond it.

**View each transition as a bounded suffix sum.** An array counted by $Z[i][j]$ ends with a zero run of some length from 1 through `limit`, preceded by an array ending in `1`. Directly summing all such run lengths would cost $O(\texttt{limit})$ per state. Instead, append one zero to every stable array using $i-1$ zeroes and $j$ ones. This gives `Z[i - 1][j] + O[i - 1][j]` candidates. If $i>\texttt{limit}$, exactly the candidates obtained from `O[i - limit - 1][j]` now have `limit + 1` trailing zeroes and must be removed. Thus

$$
Z[i][j]=Z[i-1][j]+O[i-1][j]-O[i-\texttt{limit}-1][j].
$$

The subtraction is omitted when its index would be negative. Swapping zeroes and ones gives

$$
O[i][j]=Z[i][j-1]+O[i][j-1]-Z[i][j-\texttt{limit}-1].
$$

**Why the subtraction is exact.** Every invalid extension has one newly formed suffix of exactly `limit + 1` equal values. Removing that suffix leaves a stable prefix ending in the opposite bit, establishing a bijection with the subtracted state. Every other extension remains stable because appending a bit can affect only the trailing run. Induction over $i+j$ therefore proves both state tables correct, and their disjoint final-bit classes sum to the answer.

Apply the modulus after each update, including after subtraction. The constant-time removal of the outgoing suffix state is the prefix-sum optimization that makes the recurrence viable at the 1,000-by-1,000 bound.

## Complexity detail

Let $z=\texttt{zero}$ and $o=\texttt{one}$. The algorithm fills two tables over $(z+1)(o+1)$ count pairs and performs $O(1)$ work per entry, for $O(zo)$ time. Both tables occupy $O(zo)$ auxiliary space. In particular, the running time does not gain another factor of `limit`.

## Alternatives and edge cases

- **Enumerate every final-run length:** Sum the opposite-ending states for all suffix lengths from 1 through `limit`. This is correct but takes $O(zo\cdot\texttt{limit})$ time and is too slow at the upper bounds.
- **Store `(last, run)` explicitly:** A three-dimensional DP or memoized recursion exposes the rule directly but also creates $O(zo\cdot\texttt{limit})$ states.
- **Bounded compositions of runs:** Count alternating zero and one runs through inclusion-exclusion. This can work, but requires careful positive-part composition formulas and modular binomial coefficients.
- **Limit equal to 1:** Values must alternate; with positive counts, the answer is 0 when their difference exceeds one, 1 when it equals one, and 2 when they are equal.
- **One count far larger than the other:** The minority value creates at most one more majority run than its own count, so some inputs are impossible even when both counts are positive.
- **Limit larger than both counts:** Every arrangement is legal, and the result is $\binom{z+o}{z}$ modulo $10^9+7$.
- **Negative modular intermediate:** Normalize each subtraction immediately so the same recurrence remains correct in languages whose remainder operator preserves a negative sign.
