## General

**Turn the interval into two prefix counts.** For an integer boundary $t$, let $C(t)$ be the number of nonnegative perfect $k$th powers no greater than $t$. The requested interval count is

$$
C(\texttt{r})-C(\texttt{l}-1).
$$

This subtraction includes both endpoints automatically and also makes the `l = 0` boundary precise by defining $C(t)=0$ for $t<0$.

**Count bases instead of materializing powers.** On the nonnegative integers, the map $x\mapsto x^k$ is strictly increasing. Thus, if $q$ is the largest nonnegative integer satisfying $q^k\le t$, the qualifying bases are exactly $0,1,\ldots,q$ and $C(t)=q+1$. Negative bases add no new nonnegative powered values: they either produce a negative value for odd $k$ or duplicate a positive base for even $k$.

When `k == 1`, every integer is its own first power, so the answer is immediately `r - l + 1`. For $k\ge2$, find $q$ with binary search over the nonnegative candidates from `0` through `t`. If `middle ** k <= t`, `middle` is feasible and the search continues to its right; otherwise it continues to the left. All exponentiation is exact integer arithmetic, avoiding rounding at perfect-power boundaries.

At termination, `low` is the first infeasible base, hence it equals $q+1=C(t)$. Applying this independently to `r` and `l - 1` and subtracting removes precisely the powers below the interval while retaining every power inside it, which proves the returned count.

## Complexity detail

Use $R=\max(2,\texttt{r}+1)$ and $K=\max(2,\texttt{k})$. Each of the two binary searches performs $O(\log R)$ comparisons. Exact integer exponentiation by squaring takes $O(\log K)$ multiplications, so the total is $O(\log R\log K)$ arithmetic operations. The `k = 1` branch takes $O(1)$ time. The algorithm keeps only search bounds and scalar intermediates, using $O(1)$ auxiliary space under the source-bounded integer model.

The benchmark defines its size as $B=\lfloor\sqrt{\texttt{r}}\rfloor$ on square-power inputs. Since `r = B ** 2` and `k = 2`, the accepted method grows as $O(\log B)$ on those tiers. Enumerating every candidate base through $B$ is a correct but genuine $O(B)$ slower class.

## Alternatives and edge cases

- **Enumerate candidate bases:** Generate `x ** k` for increasing nonnegative `x` until the value exceeds `r`, counting those at least `l`. This follows the source hint and is legal because square roots are at most $31{,}622$, but its worst case is $O(\sqrt{r}\log k)$ rather than logarithmic in the range boundary.
- **Use floating-point roots:** Computing `r ** (1 / k)` and rounding can cross an exact-power boundary because binary floating point is approximate. An integer binary search avoids corrective guesswork.
- **Exponent one:** Every integer is a perfect first power, including every value in a large interval; do not iterate through the range.
- **Lower endpoint zero:** Include $0=0^k$. The prefix below `l` is empty when `l = 0`.
- **Even exponents and negative bases:** The values from `x` and `-x` coincide, so count the powered value once rather than counting witnesses.
- **Exact endpoints:** The comparison is inclusive. If `l` or `r` equals a perfect power, that value belongs to the answer.
- **Intervals without a perfect power:** Prefix subtraction naturally returns zero when consecutive root cutoffs are equal.
