## General

**Exploit balance within complete decimal blocks**

In every block `10q` through `10q + 9`, the leading digits contribute the
fixed digit sum of `q`. The final digit contributes each value from $0$ to
$9$, exactly five even and five odd values. Consequently, exactly five
numbers in every complete block of ten have even digit sums.

For an incomplete final block, the valid final digits alternate according to
the parity of the fixed leading-digit sum. Writing the endpoint as
`num = 10 * q + r`, the complete blocks and this alternating suffix simplify
to one of two adjacent counts:

$$
\left\lfloor\frac{\texttt{num}}2\right\rfloor
\quad\text{or}\quad
\left\lfloor\frac{\texttt{num}-1}2\right\rfloor.
$$

The lower count is needed exactly when the digit sum of `num` is odd. Thus, if
$s$ is that digit sum, both cases are represented by

$$
\left\lfloor\frac{\texttt{num}-(s\bmod 2)}2\right\rfloor.
$$

The excluded integer zero is already accounted for in this simplification:
the formula counts only positive integers. Computing the endpoint's digit sum
and applying the expression therefore gives the complete answer without
examining every smaller integer.

## Complexity detail

Extracting the decimal digits of `num` takes $O(\log\texttt{num})$ time. The
calculation keeps only the remaining quotient and a running sum, so it uses
$O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every integer:** Compute the digit sum of each value from `1`
  through `num`. This mirrors the definition but takes
  $O(\texttt{num}\log\texttt{num})$ time.
- **Count by decimal blocks explicitly:** Add five for every complete decade
  and scan the final partial block. This is correct in $O(\texttt{num}/10)$
  time but misses the constant-sized algebraic reduction.
- `num = 1` has no qualifying positive integer and returns zero.
- Powers of ten have digit sum one, so the endpoint itself does not qualify.
- The upper endpoint is included whenever its digit sum is even.
