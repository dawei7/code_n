## General

Every positive ordered sequence of length $k$ with sum $n$ is a composition of $n$. Stars and bars counts all of them as

$$
\binom{n-1}{k-1}.
$$

The product is odd exactly when every element is odd. Count that complement by writing each sequence element as $a_i=2x_i+1$, where $x_i\ge0$. The transformed variables must satisfy

$$
\sum_{i=1}^{k}x_i=\frac{n-k}{2}.
$$

If $n-k$ is odd, this equation has no integer solutions, so every composition already has an even product. Otherwise, stars and bars counts the all-odd sequences as

$$
\binom{(n-k)/2+k-1}{k-1}
=\binom{(n+k)/2-1}{k-1}.
$$

Subtracting this complement from the total counts precisely the sequences containing at least one even element, which are precisely the sequences with an even product.

To evaluate each binomial coefficient, multiply only its shorter side, reducing numerator and denominator modulo $M=10^9+7$ after every factor. Because every factorial factor is smaller than the prime $M$, the denominator is nonzero modulo $M$. Fermat's little theorem supplies its inverse as the denominator raised to $M-2$ modulo $M$.

## Complexity detail

Each binomial coefficient uses at most a linear number of modular multiplications in $n$. Modular exponentiation adds $O(\log M)$ time; since $M=10^9+7$ is fixed by the contract, the package bound is $O(n)$ time. The calculation retains only counters and modular products, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Factorial and inverse-factorial tables:** Precomputing both arrays also gives $O(n)$ time and constant-time binomial queries, but consumes $O(n)$ auxiliary space for only two queries.
- **Pascal-triangle dynamic programming:** It avoids modular division but takes $O(nk)$ time and $O(k)$ space when computing the required coefficients row by row.
- **Odd value of `n - k`:** An all-odd length-`k` sequence cannot have the required sum, so nothing is subtracted from the total.
- **`k = n`:** Positivity forces the all-ones sequence, whose odd product makes the answer zero.
- **`k = 1`:** The sole sequence is `[n]`; it is valid exactly when `n` is even.
- **Modulo subtraction:** Reduce the difference modulo $M$ so a smaller residue for the total does not produce a negative return value.
