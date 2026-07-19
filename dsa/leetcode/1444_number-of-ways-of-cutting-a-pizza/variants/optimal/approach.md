## General
**Represent the only rectangle that remains cuttable**

The giving rule is directional: a horizontal cut permanently gives away the
upper part, and a vertical cut permanently gives away the left part. Therefore
the part available for future cuts is always a suffix rectangle whose top-left
corner is some cell $(r,c)$ and whose bottom-right corner remains the pizza's
original bottom-right corner.

This removes the need to represent four arbitrary rectangle boundaries. A
dynamic-programming state needs only $(r,c,p)$, where $p$ is the number of
pieces that still must be produced from the suffix rectangle beginning at
$(r,c)$.

**Answer rectangle apple queries in constant time**

Build a two-dimensional suffix-sum table $S$ such that $S_{r,c}$ is the number
of apples in the rectangle from $(r,c)$ through $(m-1,n-1)$. It follows the
inclusion-exclusion recurrence

$$
S_{r,c}
=
[\text{cell }(r,c)\text{ contains an apple}]
+S_{r+1,c}
+S_{r,c+1}
-S_{r+1,c+1}.
$$

The upper strip removed by a horizontal cut before row $r'$ contains
$S_{r,c}-S_{r',c}$ apples. Similarly, the left strip removed by a vertical cut
before column $c'$ contains $S_{r,c}-S_{r,c'}$ apples. Each candidate cut can
therefore be validated in $O(1)$ time.

**Define the state and its base conditions**

Let $F(r,c,p)$ be the number of valid cutting sequences that divide the suffix
rectangle at $(r,c)$ into exactly $p$ apple-containing pieces. If that
rectangle contains fewer than $p$ apples, the state is impossible because
every final piece needs a distinct apple; return zero. When $p=1$, return one
if the rectangle contains an apple, because giving the entire remaining
rectangle is the only valid completion.

The apple-count pruning is not merely an optimization. It also handles empty
pizzas and requests for more pieces than apples without inventing cuts or
silently reducing $k$.

**Transition over the next delivered piece**

For every row $r'$ strictly below $r$, consider a horizontal cut. It is legal
only if the upper strip being delivered contains an apple. When it does, the
remaining work is exactly $F(r',c,p-1)$.

Likewise, for every column $c'$ strictly to the right of $c$, a vertical cut
is legal only if its left strip contains an apple, and it contributes
$F(r,c',p-1)$. Sum all legal transitions modulo $10^9+7$ and memoize each
state.

Every valid cutting sequence has a unique first cut. That cut appears in
exactly one horizontal or vertical transition, its delivered piece passes the
apple test, and the rest of the sequence is counted by the corresponding
smaller state. Conversely, joining any legal first cut with a completion
counted by its child state produces exactly $p$ apple-containing pieces.
Induction on $p$ therefore proves that the recurrence counts every valid
sequence once and no invalid sequence.

## Complexity detail
There are at most $kmn$ states. A state considers at most $m-r-1$ horizontal
cuts and $n-c-1$ vertical cuts, for $O(m+n)$ transitions, and each transition
uses constant-time suffix-sum queries. The total time is
$O(kmn(m+n))$. The suffix table uses $O(mn)$ space, while memoization stores
at most $O(kmn)$ states; since $k \ge 1$, the combined auxiliary space is
$O(kmn)$.

## Alternatives and edge cases
- **Bottom-up dynamic programming:** The same state can be filled by increasing
  piece count instead of memoized recursion. It has identical asymptotic
  bounds and avoids call overhead, but the top-down form naturally skips
  unreachable suffix rectangles.
- **Scan cells for every proposed cut:** Directly checking whether each
  delivered strip has an apple preserves correctness but repeats rectangle
  scans inside every state and adds a large avoidable factor. The 2D suffix
  table is what keeps each validation constant-time.
- **Enumerate complete cut sequences:** Backtracking without memoizing
  $(r,c,p)$ recomputes the same remaining rectangle after many different
  prefixes and can grow exponentially.
- **No apples:** Even when $k=1$, the sole piece would violate the at-least-one-
  apple rule, so the answer is zero.
- **Fewer apples than pieces:** No cutting arrangement can place an apple in
  every piece; the state-level apple-count test returns zero immediately.
- **One requested piece:** The answer is one exactly when the entire pizza
  contains an apple, because there are no cuts to choose.
- **One row or one column:** Only one cut orientation is available, but the
  same recurrence works because the loop for the impossible orientation is
  empty.
- **Ordered giving semantics:** Only the lower or right remainder is cut
  again. Treating all final geometric partitions as unordered would solve a
  different problem and miscount the allowed cutting sequences.
- **Modulo arithmetic:** Apply the modulus while accumulating transitions so
  large intermediate counts remain bounded without changing the final
  residue.
