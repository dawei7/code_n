## General

Let the triangular total through `n` be

$$
T = \frac{n(n+1)}{2}.
$$

If $x$ is a pivot, the left inclusive sum is $x(x+1)/2$. The right inclusive sum contains the whole range through $n$ except the values strictly before $x$, so it is

$$
T - \frac{(x-1)x}{2}.
$$

Equating the two sides and cancelling the shared linear terms gives

$$
\frac{x(x+1)}{2}
=
T-\frac{(x-1)x}{2}
\quad\Longleftrightarrow\quad
x^2=T.
$$

Therefore a pivot exists exactly when the triangular total $T$ is a perfect square, and its only possible value is $\sqrt{T}$. Compute the integer square root of $T$ and verify that squaring it reproduces $T$. This explicit check distinguishes a genuine integer root from a truncated non-square root and also proves uniqueness because a nonnegative integer has at most one nonnegative square root.

## Complexity detail

The triangular sum, integer square root, and verification use a fixed number of arithmetic operations, so the running time is $O(1)$ under the problem's bounded integer model. Only `total` and `pivot` are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Running prefix sum:** Check every candidate $x$ while updating the left sum and deriving the right sum from $T$. This is straightforward and uses $O(1)$ space, but takes $O(n)$ time.
- **Binary search:** Because $x^2$ is increasing for nonnegative $x$, binary search can find a possible root in $O(\log n)$ time, but integer square root already performs the exact operation directly.
- **Floating-point square root:** Converting to a floating-point root and truncating is unnecessary and can introduce rounding concerns outside the small stated range; integer square root is exact.
- **`n = 1`:** The triangular total is $1$, so the sole integer is correctly returned as its own pivot.
- **No perfect square:** If `pivot * pivot` differs from $T$, no integer can satisfy the derived necessary and sufficient equation, so the answer is `-1`.
