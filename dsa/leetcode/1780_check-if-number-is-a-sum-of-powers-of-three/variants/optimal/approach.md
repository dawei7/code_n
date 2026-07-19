## General
**Translate distinct powers into ternary digits**

In a base-three representation, the coefficient of $3^k$ is the digit at position $k$. A sum of distinct powers chooses each coefficient from $\{0,1\}$: zero excludes the power and one includes it. Therefore the requested representation exists exactly when the ordinary ternary expansion of `n` contains no digit `2`.

**Inspect the expansion from least significant digit**

Repeatedly apply `divmod(n, 3)`. The remainder is the next ternary digit, and the quotient contains all higher digits. Return `false` immediately if a remainder is `2`; otherwise continue until the quotient becomes zero. If every digit was zero or one, those one-valued positions give a valid set of distinct powers, proving `true`.

## Complexity detail
For an unrestricted integer, extracting its ternary digits takes $O(\log_3 n)$ time and $O(1)$ space. The public constraint $n \le 10^7 < 3^{15}$ fixes the loop at no more than fifteen iterations, so both time and auxiliary space are $O(1)$ over the complete legal domain.

## Alternatives and edge cases
- **Greedy subtraction:** Repeatedly subtract the largest power of three not exceeding the remainder. This can work, but base-three division states the no-repetition condition more directly.
- **Enumerate subsets:** Generate sums of the relevant powers and test membership. With fifteen powers the domain is bounded, but this performs exponential work and obscures the numeral-system structure.
- `n = 1` is representable as $3^0$.
- Any ternary digit `2`, including the least significant one, makes the representation impossible.
- Zero digits are allowed because not every power must be selected.
- A dense valid value can use every power from $3^0$ through $3^{14}$ once.
