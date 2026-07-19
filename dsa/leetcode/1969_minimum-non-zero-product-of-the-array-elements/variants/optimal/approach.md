## General
**Identify what bit swaps preserve**

For each bit position, exactly $2^{p-1}$ of the original integers contain a
one. A legal swap moves one such bit between elements but never changes that
per-position count. The all-ones value $Q$ can remain intact, consuming one
one from every bit position.

The remaining ones can be distributed among

$$
K=2^{p-1}-1
$$

pairs of positive elements. Within each pair, place a single one in the least
significant position of one element and all other bit-position ones in the
other. Each pair then has values $1$ and $Q-1$.

**Why the pairs give the minimum positive product**

Consider redistributing a one-bit within a complementary pair while both
values must stay positive. Moving value from the smaller member to the larger
member makes the two values more unequal while preserving their sum. For
positive integers with fixed sum, this decreases their product until the
smaller value reaches its minimum possible value, $1$. The partner must then
be $Q-1$.

Applying that polarization across all remaining bit counts produces $K$
copies of the pair $(1,Q-1)$ plus the single value $Q$. No element becomes
zero, every bit-position count is preserved, and any less polarized positive
pair has a product at least as large. The minimum product is therefore

$$
Q(Q-1)^K.
$$

Compute this expression modulo $10^9+7$ with binary modular exponentiation.
The exponent may be as large as $2^{59}-1$, so expanding the multiplication
one factor at a time is not feasible.

## Complexity detail
The exponent $K$ has $O(p)$ binary digits. Modular exponentiation processes
one digit per squaring step, giving $O(p)$ time. The values `Q`, `K`, the
modulus, and the exponentiation state occupy $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Repeated multiplication:** Multiplying by $Q-1$ exactly $K$ times is
  correct but takes $O(2^p)$ time.
- **Construct the transformed array:** Explicitly materializing all
  $2^p-1$ elements is unnecessary and becomes infeasible well before the
  maximum `p`.
- **Minimize the modular residue directly:** This solves a different problem.
  The true integer product must be minimized first, and only that result is
  reduced modulo $10^9+7$.
- For `p = 1`, $K=0$ and the formula correctly becomes
  $1\cdot 0^0=1$ under modular exponentiation's zero-exponent convention.
- Arbitrary bit swaps are not allowed: each exchanged pair of bits must occupy
  the same binary position in its two elements.
