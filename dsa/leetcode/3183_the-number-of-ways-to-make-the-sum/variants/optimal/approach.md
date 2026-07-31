## General

**Separate the bounded coin.** A combination uses a uniquely determined number $k$ of value-4 coins, where $k\in\{0,1,2\}$. After fixing $k$, the remaining sum is $m=n-4k$ and must be formed only with unlimited coins of values 1, 2, and 6. The three choices of $k$ are disjoint, so their counts can be added.

**Count values 1, 2, and 6 without dynamic programming.** Fix the number $c$ of value-6 coins. For $0\le c\le\lfloor m/6\rfloor$, the residual $m-6c$ can use any number of value-2 coins from zero through $\lfloor(m-6c)/2\rfloor$; the remaining value is then supplied uniquely by value-1 coins. Thus this fixed $c$ contributes

$$
\left\lfloor\frac{m-6c}{2}\right\rfloor+1
=
\left\lfloor\frac{m}{2}\right\rfloor-3c+1.
$$

Let $q=\lfloor m/6\rfloor$. Summing that arithmetic progression gives, for $m\ge0$,

$$
F(m)
=
(q+1)\left(\left\lfloor\frac{m}{2}\right\rfloor+1\right)
-
\frac{3q(q+1)}{2}.
$$

Define $F(m)=0$ for negative $m$. The required result is

$$
\bigl(F(n)+F(n-4)+F(n-8)\bigr)\bmod(10^9+7).
$$

Every combination has exactly one value of $k$ and exactly one value of $c$, after which its value-2 count determines its value-1 count. It is therefore counted once by one term of one progression. Conversely, each enumerated choice has nonnegative coin counts, respects the two-coin limit for value 4, and sums to $n$. Hence the formula counts precisely all valid combinations.

## Complexity detail

The formula evaluates exactly three bounded-coin choices and uses a constant number of integer operations for each. It therefore takes $O(1)$ time and $O(1)$ auxiliary space. The modulus is applied to the final sum; all intermediate values fit comfortably within ordinary integer ranges under $n\le10^5$.

## Alternatives and edge cases

- **One-dimensional coin-change DP:** Build counts for unlimited coins 1, 2, and 6 in $O(n)$ time and $O(n)$ space, then add the entries for `n`, `n - 4`, and `n - 8`. This is correct and direct but does unnecessary work for fixed coin values.
- **Loop over value-6 counts:** Evaluate the same residual value-1/value-2 count for every possible number of sixes. It uses $O(1)$ space but $O(n)$ time instead of summing the arithmetic progression.
- **Target-first DP iteration:** Iterating sums before coin types counts different orders as separate sequences, violating the combination contract.
- **Bound on value 4:** Treating 4 as an unlimited coin incorrectly admits combinations containing three or more value-4 coins.
- **Small targets:** When `n < 4` or `n < 8`, the corresponding negative residual contributes zero.
- **Modulo arithmetic:** The returned count must be reduced modulo $10^9+7$, especially near the maximum target.
