## General

**Think about boundaries rather than individual array elements.** An array of length $n$ has exactly $n-1$ boundaries between adjacent positions. At each boundary, one of two events happens:

- the next value equals the previous value, so the boundary is a matching boundary;
- the next value differs, so the boundary starts a new constant-valued segment.

The problem requires exactly $k$ matching boundaries. Therefore, exactly

$$
(n-1)-k=n-k-1
$$

boundaries must be changing boundaries.

The first independent choice is which $k$ of the $n-1$ boundaries match. There are

$$
\binom{n-1}{k}
$$

ways to choose them. Equivalently, one could choose the $n-k-1$ changing boundaries; binomial symmetry makes the count identical.

**Count value assignments after the boundary pattern is fixed.** The first array position may contain any integer from $1$ through $m$, giving $m$ choices. Now move from left to right. At a boundary previously marked “matching,” the next value is forced to equal the current value, so it contributes one choice. At a boundary marked “changing,” the next value may be any allowed value except the current one, so it contributes $m-1$ choices.

There are $n-k-1$ changing boundaries. Thus, every fixed boundary pattern permits

$$
m(m-1)^{n-k-1}
$$

arrays. Multiplying by the number of boundary patterns gives the closed form

$$
\binom{n-1}{k}\,m\,(m-1)^{n-k-1}.
$$

This counting is exact rather than an inclusion-exclusion approximation. Every constructed array has exactly the selected matching boundaries, because a changing boundary is explicitly assigned a value different from its predecessor. Conversely, every good array determines one unique set of its $k$ matching boundaries, its first value, and the value chosen after each changing boundary. Hence no array is omitted or counted twice.

For `n = 3`, `m = 2`, and `k = 1`, choose one of the two boundaries to match, choose either starting value, and make one forced change at the other boundary. The formula gives $\binom21\cdot2\cdot1^1=4$, producing the four arrays in the example.

**Why modular inverses are needed.** The answer is required modulo the prime

$$
P=10^9+7.
$$

The helper computes a binomial coefficient using factorials:

$$
\binom{x}{y}=\frac{x!}{y!(x-y)!}.
$$

Ordinary integer division cannot be applied after reducing values modulo $P$. Instead, division by a nonzero residue $z$ is multiplication by its modular inverse. Since $P$ is prime, Fermat's little theorem gives

$$
z^{-1}\equiv z^{P-2}\pmod P.
$$

The global array `f` stores factorials modulo $P$: `f[i]` is $i!\bmod P$. The global array `g` stores their modular inverses: `g[i]` is $(i!)^{-1}\bmod P$. Therefore, `comb(m, n)` returns

`f[m] * g[n] * g[m - n] % mod`,

which is $\binom{m}{n}\bmod P$. The constraints ensure every required factorial index is less than $P$, so its factorial is nonzero modulo $P$ and the inverse exists.

**Follow the exact protected source's initialization.** The module declares `mx = 10**5 + 10` and allocates global arrays large enough for all allowed values of $n$. It fills `f` from left to right. On the same iteration, it calls Python's three-argument `pow` to compute the inverse of every individual factorial:

`g[i] = pow(f[i], mod - 2, mod)`.

After this module-level work has run once, `countGoodArrays` performs only three mathematical operations at a high level: obtain $\binom{n-1}{k}$, multiply by $m$, and multiply by the modular power $(m-1)^{n-k-1}$. The final `% mod` returns the required residue.

It is important not to describe a different precomputation. A common optimized implementation computes just one inverse factorial at the maximum index, then derives the rest in a backward linear pass. This protected source instead performs a modular exponentiation for every `g[i]`. The mathematical formula is optimal, but the exact startup implementation has a larger preprocessing cost than the manifest's stated per-input bound suggests.

## Complexity detail

Let $M=\texttt{mx}=100010$ and $P=10^9+7$.

At module initialization, filling factorials costs $O(M)$. The source also performs $M-1$ modular exponentiations, each with exponent $P-2$ and therefore $O(\log P)$ modular multiplications. Its exact one-time initialization cost is $O(M\log P)$ time. The two global arrays `f` and `g` consume $O(M)$ space.

Once preprocessing has completed, `comb(n - 1, k)` uses constant time and `pow(m - 1, n - k - 1, mod)` uses $O(\log(n-k))$ time. Thus one method call costs $O(\log n)$ time and $O(1)$ additional working space, excluding the already allocated global tables.

If $M$ and $P$ are treated as permanently fixed implementation constants, the startup is a fixed cost, but it is still material work and storage performed by this source. The manifest's $O(\min(k,n-1-k)+\log n)$ time does not match the constant-time table lookup used for the combination, and its $O(1)$ space omits the $O(M)$ tables. A source-faithful accounting is $O(M\log P+\log n)$ for module initialization plus the first call, $O(\log n)$ for later calls, and $O(M)$ persistent space.

## Alternatives and edge cases

- **Linear inverse-factorial precomputation:** Compute all factorials, find the inverse of the largest factorial with one modular exponentiation, and fill inverse factorials backward. This reduces startup to $O(M+\log P)$ while preserving $O(1)$ combination queries.
- **Multiplicative binomial coefficient:** Computing $\binom{n-1}{k}$ with $\min(k,n-1-k)$ numerator factors avoids global tables and uses $O(\min(k,n-1-k)+\log P)$ time. That resembles the manifest bound but is not the protected implementation.
- **Dynamic programming over positions and match counts:** A DP can track arrays ending with equal or changed boundaries, but it uses at least $O(nk)$ transitions without further algebra and obscures the direct combinatorial structure.
- **Single allowed value:** If `m == 1`, only the all-ones array exists. It has $n-1$ matching boundaries. The formula returns one when `k == n - 1` because the exponent is zero, and zero otherwise because a positive power of `m - 1` is zero.
- **Length one:** For `n == 1`, necessarily `k == 0`. There are no boundaries, and the formula becomes $\binom00m(m-1)^0=m$. Python's modular `pow` correctly treats the zero exponent as one.
- **All boundaries match:** When `k == n - 1`, the array is constant. There are exactly $m$ choices, which the formula gives because the exponent of $m-1$ is zero.
- **No boundaries match:** When `k == 0`, choose the first value in $m$ ways and each later value in $m-1$ ways, yielding $m(m-1)^{n-1}$.
- **Modulo division:** Dividing reduced factorial residues with `//` would be incorrect. Modular inverses are required because arithmetic is taking place in residues modulo a prime.
- **Global startup timing:** Importing the module performs all precomputation even if `countGoodArrays` is called only once. Complexity discussions and performance investigations should not silently exclude that work.
