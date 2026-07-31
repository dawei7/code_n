## General

An array of length $n$ has $n-1$ adjacency slots. First choose exactly which $k$ slots will match their preceding value. This contributes

$$
\binom{n-1}{k}
$$

boundary patterns. The first array element has $m$ choices. At a selected matching slot, the next value is forced to equal the previous value and contributes one choice. At each of the remaining $n-1-k$ slots, the next value must differ from its predecessor and can be any of the other $m-1$ values. Therefore the answer before taking the modulus is

$$
m\binom{n-1}{k}(m-1)^{n-1-k}.
$$

This construction is bijective. Every choice of matching slots, first value, and alternative value at each changing slot produces one good array. Conversely, every good array uniquely reveals those choices, so nothing is omitted or counted twice.

Let $P=10^9+7$. Compute the binomial coefficient modulo $P$. By symmetry, use

$$
t=\min(k,n-1-k)
$$

and form the $t$ numerator factors and $t!$ denominator. Because $t<P$, the denominator is nonzero modulo $P$. Fermat's little theorem gives its inverse as `denominator^(P - 2) mod P`. Modular exponentiation also evaluates the $(m-1)$ power efficiently.

## Complexity detail

The multiplicative binomial coefficient performs $t=\min(k,n-1-k)$ iterations. The two modular powers take $O(\log P)$ and $O(\log n)$ multiplications respectively; $P$ is fixed. The total time is $O(\min(k,n-1-k)+\log n)$, and only a constant number of integers is stored, so the auxiliary space is $O(1)$.

The benchmark defines `size` as $n$ and uses legal 10-, 20-, and 40-element tiers with $k$ near $n/2$, spanning 4x. The accepted formula performs linear work in the smaller side of the binomial coefficient. A correct slower dynamic program tracks every possible match count after every position, taking $O(nk)$ time and $O(k)$ space, and fails only the scaling verdict.

## Alternatives and edge cases

- **Dynamic programming by position and match count:** This directly models equal and unequal transitions, but it needs $O(nk)$ time instead of exploiting the closed form.
- **Generate arrays:** Enumerating all $m^n$ arrays is infeasible even at moderate input sizes.
- **Compute the ordinary binomial integer first:** The exact integer can contain tens of thousands of digits; modular multiplication and inversion keep every intermediate bounded.
- **One element:** There are no adjacency slots, so `k` must be zero and every one of the $m$ single-element arrays is good.
- **One available value:** Only the constant array exists. It is good exactly when $k=n-1$; the factor $(m-1)^{n-1-k}$ handles both cases, including $0^0=1$.
- **No matches:** Every boundary changes, giving $m(m-1)^{n-1}$ arrays.
- **All matches:** Every element equals the first, giving exactly $m$ arrays.
