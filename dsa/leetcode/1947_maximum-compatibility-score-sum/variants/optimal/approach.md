## General
**Precompute every pair score**

Build an $M$ by $M$ table where entry `(student, mentor)` counts equal answers
across the $Q$ questions. Once this table exists, assignment transitions need
only constant-time score lookups.

**Represent assigned mentors with a mask**

Use an $M$-bit mask. A set bit means that mentor has already been assigned.
If a mask contains $K$ set bits, it represents an optimal assignment for the
first $K$ students; therefore the next student index is
`mask.bit_count()`.

Let `dp[mask]` be the greatest score for that partial assignment. Start with
`dp[0] = 0`. For every unused mentor $j$, set bit $j$ and update

$$
\operatorname{dp}[\textit{mask}\cup\{j\}]
=
\max\left(
\operatorname{dp}[\textit{mask}\cup\{j\}],
\operatorname{dp}[\textit{mask}]
+\operatorname{score}[K][j]
\right).
$$

Every partial one-to-one assignment has exactly one used-mentor mask and one
score. Extending it by any unused mentor generates every valid assignment for
the next student. Keeping only the maximum for each mask is safe because all
future choices depend on which mentors remain, not on the order that produced
the mask. Induction on $K$ therefore makes the all-ones state the optimum over
all complete assignments.

## Complexity detail
Computing all $M^2$ pair scores examines $Q$ answers per pair, costing
$O(M^2Q)$. There are $2^M$ masks and at most $M$ mentor transitions per mask,
adding $O(M2^M)$ time. The score table uses $O(M^2)$ space and the dynamic
program uses $O(2^M)$ space.

## Alternatives and edge cases
- **Enumerate mentor permutations:** Score every one-to-one assignment
  directly. This is simple but costs $O(M!\,MQ)$ time without precomputation,
  or $O(M!\,M)$ after pair scores are built.
- **Backtracking with memoization:** Recurse by student and used-mentor mask.
  It has the same asymptotic complexity as iterative bitmask DP but adds call
  stack overhead.
- A single student has only one possible mentor, so the answer is that pair's
  score.
- Completely opposite response rows may contribute zero.
- Identical student or mentor rows remain separate people and must each be
  assigned exactly once.
- Several assignments may tie for the maximum; only the score is returned.
- The maximum possible result is $MQ$, achieved when every assigned pair
  agrees on all questions.
