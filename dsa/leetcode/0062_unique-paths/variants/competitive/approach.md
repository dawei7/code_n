## General

**Describe a path by the order of its moves**

To travel from the top-left to the bottom-right of an $m \times n$ grid, the robot must move down exactly $m-1$ times and right exactly $n-1$ times. Every valid path has exactly

$$
(m-1)+(n-1)=m+n-2
$$

moves. The only choice is how to arrange the downs and rights in that sequence.

Choose which $n-1$ move positions contain right moves; the rest automatically contain down moves. The number of choices is

$$
\binom{m+n-2}{n-1}.
$$

This gives a one-to-one correspondence: each chosen position set produces one path, and each path produces one chosen position set.

**Use the smaller binomial side**

The identity

$$
\binom{N}{r}=\binom{N}{N-r}
$$

means selecting right-move positions or down-move positions gives the same count. Inside `nCr`, if `n-r < r`, the source replaces `r` with `n-r`.

For the grid call, total `n` inside the helper is $m+n-2$, and initial `r` is $n-1$ from the outer method's column count. Its complement is $m-1$. The loop therefore runs only $\min(m-1,n-1)$ times.

The helper parameter named `n` is the combinatorial total, not necessarily the grid column count. Keeping those scopes distinct avoids confusing the formula.

**Build the coefficient multiplicatively**

The recurrence

$$
\binom{N}{k}=\binom{N}{k-1}\cdot\frac{N-k+1}{k}
$$

allows the coefficient to be computed without factorials. Starting with `c = 1`, which is $\binom{N}{0}$, each loop multiplies by `n-k+1` and then integer-divides by `k`. After iteration `k`, `c` equals $\binom{N}{k}$.

Although the division is performed at every step, it is exact. The binomial recurrence guarantees the product before division is divisible by `k`; `//` does not truncate away a fractional answer.

Computing incrementally also avoids separately constructing three huge factorials. Python integers can still grow beyond machine width internally, but no BigInteger library or floating-point approximation is used explicitly.

**Trace for a three-by-seven grid**

The robot needs 2 down moves and 6 right moves, for 8 total. The helper is called as `nCr(8,6)` and switches `r` to 2 by symmetry.

Starting from 1, iteration 1 multiplies by 8 and divides by 1, giving 8. Iteration 2 multiplies by 7 and divides by 2, giving 28. This is $\binom{8}{2}$, the expected number of paths.

**Correctness of the complete method**

The move-sequence correspondence proves that the path count equals the binomial coefficient passed to `nCr`. The loop invariant proves `nCr(N,r)` returns that exact coefficient. Combining the two facts proves the returned integer is exactly the number of unique grid paths.

No path can contain a different number of moves: every down increases the row by one and every right increases the column by one, so the required counts are fixed by the destination coordinates.

**The selected class and unused DP alternative**

`Solution2` in the same file uses a one-dimensional dynamic-programming row. The harness selects class `Solution`, whose combinatorial calculation is described here. Its complexity should not be confused with the unused $O(mn)$ DP traversal.

**Why the calculation stays exact in Python**

No floating-point conversion occurs. `c` begins as an integer, multiplication produces an integer, and `//` applies an exact division justified by the recurrence. Python also expands integer storage automatically, so intermediate products cannot wrap around as fixed-width machine integers might. The problem's answer bound controls the final value, but the algorithm's correctness does not depend on approximate arithmetic or a manual overflow workaround.

## Complexity detail

After symmetry reduction, the loop executes $\min(m-1,n-1)$ times. Under the standard unit-cost integer arithmetic model, time is $O(\min(m,n))$, matching the manifest and improving on the source comment's looser $O(m+n)$.

Only `c`, loop index, and scalar parameters are stored. No factorial table, grid, or recursion stack is allocated, so auxiliary space is $O(1)$, matching the manifest. Python's arbitrary-precision integer object may use more machine words as values grow, but conventional problem analysis treats the result integer as scalar.

## Alternatives and edge cases

- **Full two-dimensional DP:** Sum counts from above and left at every cell. It is intuitive but uses $O(mn)$ time and space.
- **Rolling one-dimensional DP:** It retains the same recurrence with $O(mn)$ time and $O(\min(m,n))$ space.
- **Direct factorial quotient:** Compute `N! // (r! * (N-r)!)`. It is concise but constructs larger intermediate integers and repeats multiplication work.
- **Floating-point combination:** It risks rounding and should not be used when an exact integer is required.
- **One row or one column:** Symmetry reduces `r` to zero, the loop is empty, and `c = 1` correctly represents the only straight path.
- **One-by-one grid:** There are zero moves and exactly one empty move sequence.
- **Exact division:** Multiplying before `// k` follows the binomial recurrence and preserves integrality at every iteration.
- **Swapped dimensions:** The binomial symmetry makes the result and loop length unchanged.
- **Answer bound:** The stated cases keep the returned value within $2 \times 10^9$, though Python would handle larger integers.
- **No mutation:** Both grid dimensions are scalar inputs, and the method allocates no caller-visible structure.
