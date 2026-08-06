## General

Fix one person in a noncrossing arrangement. Their handshake divides the remaining people into two disjoint arcs, and every person on either arc must be paired within that same arc. If one side contains $i$ pairs, the other contains $p-1-i$ pairs. Therefore the count is the $p$th Catalan number:

$$
C_p=\sum_{i=0}^{p-1}C_iC_{p-1-i},
\qquad C_0=1.
$$

Every valid arrangement has one unique partner for the fixed person, so it belongs to exactly one split in this sum. Conversely, combining valid arrangements from the two arcs cannot introduce a crossing because their handshake segments remain on opposite sides of the fixed segment.

**Use the closed form with one modular division**

The equivalent Catalan closed form is

$$
C_p=\frac{1}{p+1}\binom{2p}{p}
=\frac{(2p)!}{p!\,p!\,(p+1)}.
$$

Scan the integers through $2p$, maintaining their factorial product modulo $M$. Retain $p!$ when the scan reaches $p$—with the initialized value $1$ already representing $1!$ in the minimum case—and finish with $(2p)!$. Their quotient gives the desired Catalan number.

Division modulo the prime $M=10^9+7$ means multiplying by the denominator raised to $M-2$, by Fermat's little theorem. Since $2p\le1000<M$, none of the denominator factors is divisible by $M$, so the inverse exists. This modular evaluation is algebraically equal to the integer closed form and hence to the noncrossing-arrangement recurrence.

## Complexity detail

The factorial scan takes $O(p)$ time, and the single modular inverse takes $O(\log M)$ time by binary exponentiation. Total time is $O(p+\log M)$. The algorithm retains only the two factorial values, the denominator, and loop counters, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Quadratic Catalan DP:** Directly evaluating every split closely follows the combinatorial proof but takes $O(p^2)$ time and $O(p)$ space.
- **Successive Catalan ratios:** Updating $C_{k+1}=C_k\frac{2(2k+1)}{k+2}$ is compact, but computing each inverse separately costs $O(p\log M)$ time.
- **Precomputed modular inverses:** All required inverses can be prepared in linear time, but the table uses $O(p)$ space that the factorial form avoids.
- **Two people:** Here $p=1$, and the formula returns the single possible handshake.
- **Invertible denominator:** The source bound keeps every factor below $M$; without that guarantee, the factorial quotient would require different modular arithmetic.
- **Modulo reduction:** Reduce every multiplication so the method remains valid in languages with fixed-width integer types.
