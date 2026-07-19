## General
**A Pascal row is one complete binomial-coefficient sequence**

Entry `k` in zero-based row `n` is `C(n,k)`. Consecutive coefficients satisfy:

```text
C(n,k) = C(n,k-1) * (n-k+1) / k
```

This ratio derives by canceling common factors in the factorial definitions, so earlier Pascal rows are unnecessary.

**Generate each next coefficient from the previous exact integer**

Start with $\binom{n}{0} = 1$. For `k` from one through `n`, compute the next coefficient from the current one using the ratio and append it. Multiplication should occur before exact integer division in an arbitrary-precision implementation.

In a fixed-width language, intermediate multiplication can overflow even if a final coefficient fits; use the platform's guaranteed wider type or cancel factors safely.

**The current value is always the finalized coefficient just appended**

After iteration `k`, the result contains exactly `C(n, 0)` through `C(n, k)`, and the current value is the final integer coefficient `C(n, k)`.

**Trace symmetry emerging without special handling**

Starting from `1`, the recurrence produces `5`, `10`, `10`, `5`, and `1`, yielding `[1, 5, 10, 10, 5, 1]` without constructing earlier rows.

**Consecutive binomial ratios generate the row exactly**

Pascal row `n` consists of `C(n,0)` through `C(n,n)`, beginning with one. The identity

$\binom{n}{k+1} = \binom{n}{k} \cdot (n-k) / (k+1)$

maps each coefficient exactly to its successor; divisibility is guaranteed by the binomial formula. Repeating the ratio from $k = 0$ generates all $n + 1$ entries in order with no need for earlier rows.

## Complexity detail
The algorithm performs one exact arithmetic update for each of `row_index` remaining coefficients, giving $O(row_index)$ time. The returned row uses $O(row_index)$ space and auxiliary storage is $O(1)$.

## Alternatives and edge cases
- **Build all preceding rows:** takes $O(row_index^2)$ time and storage.
- **One-row in-place Pascal DP:** uses optimal output space but still takes quadratic time.
- **Factorials per coefficient:** repeats large multiplications and divisions unnecessarily.
- `row_index = 0` returns `[1]` without entering the loop.
- Coefficient symmetry appears naturally from the recurrence; copying the first half is optional and complicates odd/even center handling without improving the linear bound.
