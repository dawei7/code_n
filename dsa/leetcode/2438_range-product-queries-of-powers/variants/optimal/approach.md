## General

The minimum distinct-power decomposition is already encoded by the set bits of `n`. If bit $b$ is set, the sorted array contains $2^b$; scanning bits from least significant to most significant therefore visits the array in its required non-decreasing order.

Every product in a query is itself a power of two:

$$
\prod_{i=\texttt{left}}^{\texttt{right}} 2^{e_i}
=
2^{\sum_{i=\texttt{left}}^{\texttt{right}} e_i},
$$

where $e_i$ is the bit index represented by `powers[i]`. Store prefix sums of these indices while scanning `n`. The exponent for an inclusive range is then the difference between two prefix sums, so no query needs to revisit the selected powers. Modular exponentiation produces the requested residue directly.

This works because multiplication adds exponents, and the prefix difference contains every selected exponent exactly once. The set-bit scan also reconstructs precisely the unique minimum decomposition: omitting a set bit changes the sum, while replacing it with smaller powers would require more elements.

## Complexity detail

Let $q=\lvert\texttt{queries}\rvert$. Scanning the binary digits takes $O(\log n)$ time and stores at most $O(\log n)$ prefix values. Under the stated bound $n\le 10^9$, every range exponent is at most $0+1+\cdots+29=435$, so modular exponentiation performs bounded work per query. The total time is $O(\log n+q)$.

The prefix array uses $O(\log n)$ auxiliary space, and the returned list uses $O(q)$ space, for $O(\log n+q)$ total space.

## Alternatives and edge cases

- **Multiply each selected power:** Extracting `powers` and traversing every queried range is correct, but it can repeat up to $\lvert\texttt{powers}\rvert$ multiplications per query.
- **Prefix products with modular inverses:** Range products can also be recovered by modular division, but exponent sums are simpler because every factor is a power of two.
- **One set bit:** The decomposition has one element, and every valid query returns that power modulo $10^9+7$.
- **Bit zero is set:** The first decomposition value is $1=2^0$; its zero exponent must still be recorded in the prefix sequence.
- **Inclusive endpoints:** The right prefix index is `right + 1`, ensuring a single-element range keeps its sole factor.
- **Repeated queries:** Each occurrence produces an answer independently and in the original order.
- **Large products:** Compute the power modulo $10^9+7$ rather than materializing the potentially large integer product.
