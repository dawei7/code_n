## General

**Replace directions by a chosen visible subset**

For each person other than `pos`, exactly one direction makes that person visible to the observer: `L` on the observer's left and `R` on the observer's right. The opposite direction makes the person invisible. Therefore, after choosing which `k` of the $n-1$ other people are visible, every one of their directions is forced.

This is a bijection between size-`k` subsets of the other people and direction assignments outside `pos` with exactly `k` visible people. The observer's own direction never affects the count and remains an independent choice between `L` and `R`. The unreduced answer is consequently

$$
2\binom{n-1}{k}.
$$

**Evaluate the binomial coefficient modulo a prime**

Let $m=n-1$ and $r=\min(k,m-k)$. Symmetry gives $\binom{m}{k}=\binom{m}{r}$, so multiply the $r$ consecutive numerator factors $m-r+1$ through $m$ and the denominator factors $1$ through $r$, reducing after each multiplication.

Because the modulus $P=10^9+7$ is prime and $r<P$, the denominator is nonzero modulo $P$. Fermat's little theorem gives its inverse as `pow(denominator, P - 2, P)`. Multiplying the numerator, inverse, and the observer's factor of two yields the required residue.

Every counted subset forces exactly one direction for each non-observer and allows both directions at `pos`, so each constructed assignment is valid and counted once. Conversely, any valid assignment identifies its exact size-`k` visible subset and one of the observer's two directions, so it appears in the formula. The modular computation preserves that exact integer count modulo $P$.

## Complexity detail

The product uses $r=\min(k,n-1-k)$ iterations and modular exponentiation uses $O(\log P)$ multiplications. Since $P$ is fixed and $r\le n$, the required bound is $O(n)$ time and $O(1)$ auxiliary space.

The benchmark defines size as $n$ and uses `n = 32`, `128`, and `512`, with `k` near half of `n - 1`. The accepted multiplicative formula and an independent factorial formula should scale linearly. A correct one-dimensional Pascal recurrence performs $O(nk)=O(n^2)$ updates on these inputs and should fail only the scaling verdict.

## Alternatives and edge cases

- **Pascal dynamic programming:** Repeatedly applying `C(a,b) = C(a-1,b-1) + C(a-1,b)` is correct but takes $O(nk)$ time.
- **Factorial tables:** Precomputing factorials and inverse factorials gives $O(n)$ preparation and $O(n)$ space, useful for many queries but unnecessary for one result.
- **Enumerate all direction strings:** Testing all $2^n$ assignments is direct but exponential.
- **Observer position:** `pos` changes which direction means visible on each side, but it does not change the number of assignments.
- **No visible people:** For `k = 0`, every non-observer's direction is forced invisible and only the observer remains free, so the answer is `2`.
- **Everyone visible:** For `k = n - 1`, all other directions are forced visible and the answer is again `2`.
- **Single person:** When `n = 1`, `k` must be `0`; the sole observer has two direction choices.
