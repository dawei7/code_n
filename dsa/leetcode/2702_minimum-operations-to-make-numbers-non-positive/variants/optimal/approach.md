## General

**Separate the shared and selected decrements**

Suppose exactly $k$ operations are performed. Every array element receives the decrement $k y$ regardless of which indices are selected. Choosing a particular index during an operation gives that element an additional decrement of $x-y$ beyond the shared amount.

For a value $v$, only the positive residual $v-k y$ needs extra selections. The minimum number required for that element is

$$
\max\left(0, \left\lceil \frac{v-k y}{x-y} \right\rceil\right).
$$

There are exactly $k$ selections across $k$ operations. Thus $k$ operations are feasible precisely when the sum of these per-element requirements is at most $k$. If fewer than $k$ selections are essential, the unused selections may target arbitrary indices and only decrease values further.

**Binary-search the first feasible count**

Feasibility is monotone: any plan that works in $k$ operations can be extended with another operation without making a value positive. Zero is a valid lower search bound. Applying the shared decrement alone for $\lceil M/y \rceil$ operations, where $M=\max(\texttt{nums})$, makes every value non-positive, so that count is a valid upper bound.

At each midpoint, scan `nums`, compute the required extra selections with integer ceiling division, and stop early if their sum already exceeds the candidate count. When the sum fits, keep the midpoint as the upper half's boundary; otherwise discard it and every smaller count. The converged boundary is feasible, while every smaller count has been proved infeasible, so it is the minimum.

## Complexity detail

Let $n$ be the length of `nums` and $M=\max(\texttt{nums})$. Each feasibility check takes $O(n)$ time and the search examines $O(\log M)$ candidate counts, giving $O(n\log M)$ time. Only scalar counters and search bounds are stored, so auxiliary space is $O(1)$. The benchmark scales both $n$ and $M$ and compares binary search with a correct candidate-by-candidate scan.

## Alternatives and edge cases

- **Try operation counts sequentially:** Reusing the same feasibility test from zero upward is correct, but may require $\Theta(M/y)$ scans and becomes quadratic on the benchmark family.
- **Always select the current maximum:** A heap simulation can construct a plan, but it processes every operation and adds heap overhead; the count can be enormous.
- **Use only the shared decrement:** The bound $\lceil M/y \rceil$ is always feasible but often not minimal because selected elements receive the larger decrement.
- A single-element array still receives `x`, not `y`, because its only index is selected in every operation.
- Values with `value <= operations * y` require no extra selections.
- Integer ceiling division must be applied only to a positive residual.
- The early exit when required selections exceed the candidate prevents unnecessary work without changing feasibility.
- Python integers safely represent products such as `operations * y`; fixed-width implementations need 64-bit arithmetic.
