## General

**Identify a cost that does not depend on the split choice**

Define

$$
F(x)=\frac{x(x-1)}{2}.
$$

The value is zero for `x = 1`, matching the fact that a one needs no split. Suppose a current part `x` is divided into positive parts `a` and `b`. If each child is then completely split into ones, the operation and child costs total

$$
ab+F(a)+F(b)
=ab+\frac{a(a-1)}{2}+\frac{b(b-1)}{2}
=\frac{(a+b)(a+b-1)}{2}
=F(x).
$$

Thus the complete cost below a part depends only on the part's value, not on how it is divided. Induction over the split tree proves that every complete sequence starting from `n` costs exactly $F(n)$. The minimum is therefore that same value, computed directly as `n * (n - 1) // 2`.

This also explains the hint's repeated split into `1` and `x - 1`: its costs are `n - 1, n - 2, ..., 1`, whose sum is the same triangular number. That strategy witnesses attainability, while the algebra proves no other strategy can cost less.

## Complexity detail

The formula performs a constant number of integer operations, so it takes $O(1)$ time and $O(1)$ auxiliary space.

The benchmark defines size as $N$, the input integer, and spans the legal domain. The accepted formula is $O(1)$. The correct slower control explicitly performs the valid sequence `x -> 1 + (x - 1)` and accumulates each cost, taking $O(N)$ time.

## Alternatives and edge cases

- **Sequential one-off splits:** Repeatedly separating one from the current remainder is correct and easy to simulate, but requires $N-1$ iterations instead of using the closed form.
- **Split dynamic programming:** Computing every `dp[x]` from all positive `a + b = x` pairs takes $O(N^2)$ time and $O(N)$ space; it is useful as an independent oracle but obscures the invariant cost.
- **Balanced splits:** Dividing near the middle creates a larger immediate product, yet later child costs compensate exactly, so the final total is unchanged.
- **`n = 1`:** No operation is performed, and the formula correctly returns zero.
- **Maximum input:** For `n = 500`, the answer is `124750`, which fits comfortably in standard integer types.
