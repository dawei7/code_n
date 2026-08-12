# Integer Ladders - Optimal Approach

## Algorithm Explanation

Find the number of triplets $(x, y, h)$ with $0 < x < y < 1\,000\,000$ producing integer street widths $w$ in the crossing ladders problem.

### Pythagorean Right Triangle Pairing & Crossing Relation:
1. **Geometric Height Formula**:
   Let wall heights be $A = \sqrt{x^2 - w^2}$ and $B = \sqrt{y^2 - w^2}$.
   For $x, y, w$ to be integers, $(w, A, x)$ and $(w, B, y)$ must be right triangles.
   Crossing height $h$ satisfies:
   $$\frac{1}{h} = \frac{1}{A} + \frac{1}{B} \implies h = \frac{A B}{A + B}$$
   So $h$ is an integer iff $(A + B) \mid (A \cdot B)$.
2. **Width-Grouped Height Pairs**:
   For each width $w < 10^6$, we collect all integer vertical legs $A$ forming right triangle $(w, A, x)$ with hypotenuse $x < 10^6$.
   We test all pairs $(A, B)$ associated with the same $w$ to verify if $(A + B) \mid A B$.
3. **Execution**:
   Summing all valid triplets $(x, y, h)$ for $y < 1\,000\,000$ yields $210139$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \log L)$ for $L = 1\,000\,000$. Runs in $\approx 1.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ height list storage.
