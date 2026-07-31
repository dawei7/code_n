## General

For every integer $x > 2$, choosing `i = x - 1` satisfies `x % i == 1`. Starting from `n`, the process therefore adds `n - 1`, then `n - 2`, and continues down to 2. This chain needs at most $n - 2$ days, far fewer than the available $10^9$ days.

**Why 1 never appears**

For every integer `x`, `x % 1 == 0`, so no board value can add 1. When $n > 1$, the final distinct values are consequently exactly the integers from 2 through `n`, a set of size $n - 1$. When $n = 1$, the initial 1 remains on the board even though no new number can be added. Both cases are expressed by `max(1, n - 1)`.

## Complexity detail

The formula uses a constant number of arithmetic operations, so it takes $O(1)$ time and $O(1)$ auxiliary space. The legal domain contains only the 100 values from 1 through 100; the package therefore uses a bounded-domain certificate with exhaustive simulation rather than a misleading runtime-scaling claim.

## Alternatives and edge cases

- **Simulate every day:** The board stabilizes quickly, but iterating through $10^9$ days is unnecessary and infeasible.
- **Simulate until stable:** A set-based process is correct for this small domain, but it still obscures the direct descending-chain argument.
- **Return `n - 1` unconditionally:** This fails at `n = 1`, where the initial board still contains one distinct value.
- **Expect 1 to be generated:** Modulo 1 is always zero, never one; the value 1 appears only when it is the initial `n`.
- **Boundary `n = 2`:** No new number is added, and the board contains only 2, so the answer is 1.
- **Finite day count:** At most 98 additions along the descending chain are needed for legal inputs, so $10^9$ days always suffice.
