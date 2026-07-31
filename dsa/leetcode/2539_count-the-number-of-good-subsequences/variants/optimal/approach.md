## General

Let $f_c$ be the number of occurrences of character $c$. In any good subsequence there is one common positive frequency $k$: every character is either absent or appears exactly $k$ times. Grouping answers by this $k$ makes the groups disjoint, so their counts can be added without duplication.

**Choices for one character**

When $f_c \geq k$, there are $\binom{f_c}{k}$ ways to select exactly $k$ source positions containing $c$, plus one way to omit $c$. If $f_c < k$, omission is its only option. Choices for different characters use disjoint positions and are independent, so the number of selections for a fixed $k$ is

$$
\prod_{c:f_c\geq k}\left(\binom{f_c}{k}+1\right)-1.
$$

The subtraction removes the selection that omits every character. Summing this expression for $1 \leq k \leq \max_c f_c$ counts every good subsequence exactly once according to its common positive frequency.

**Computing combinations modulo a prime**

Precompute factorials and inverse factorials through $n$. Fermat's little theorem gives the inverse of $n!$ modulo the prime $M=10^9+7$, and a reverse pass derives all smaller inverse factorials. Then each binomial coefficient is obtained in constant time:

$$
\binom{f}{k}\equiv f!\,(k!)^{-1}\,((f-k)!)^{-1}\pmod M.
$$

All products and sums are reduced modulo $M$ as they are formed.

## Complexity detail

Let $A$ be the number of distinct characters and $m=\max_c f_c$. Counting characters and building factorial tables costs $O(n)$. Evaluating all frequencies costs $O(Am)$; because the alphabet has at most 26 letters, this is $O(n)$ overall. The factorial and inverse-factorial arrays use $O(n)$ space, while the frequency map uses $O(1)$ space under the fixed alphabet.

## Alternatives and edge cases

- **Enumerate subsequences:** Testing all $2^n-1$ nonempty position subsets is exact but infeasible for $n$ up to $10^4$.
- **Pascal-triangle combinations:** Building every binomial coefficient up to the largest frequency avoids modular inverses but needs $O(n^2)$ time in the worst case.
- **One distinct character:** Every nonempty subsequence is good, and the formula sums to $2^n-1$.
- **All characters distinct:** Only $k=1$ contributes, yielding every nonempty position subset.
- **Repeated text values:** Subsequences are distinguished by selected indices, which is why choosing $k$ copies contributes $\binom{f_c}{k}$ rather than one.
- **Empty selection:** The all-omitted choice must be subtracted separately for every common frequency $k$.
- **Modular subtraction:** Reduce after subtracting one so intermediate negative values do not leak into languages whose remainder operator preserves the sign.
