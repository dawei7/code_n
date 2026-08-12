# Perfect Right-angled Triangles - Optimal Approach

## Algorithm Explanation

Find the number of perfect right-angled triangles with hypotenuse $c \le 10^{16}$ that are *not* super-perfect (i.e. whose area is not divisible by $6$ and $28$, $\operatorname{lcm}(6, 28) = 84$).

### Number Theory Proof:
1. **Parametrization**:
   For any primitive Pythagorean triple $(a, b, c)$ with $c = K^2$:
   $c = m^2 + n^2 = K^2 \implies (m, n, K)$ is itself a primitive Pythagorean triple!
   Thus $m = u^2 - v^2$ and $n = 2uv$ for coprime $u > v$ of opposite parity.
2. **Area Factorization**:
   The area $A = \frac{1}{2} a b = m n (m^2 - n^2)$:
   $$A = 2uv (u^2 - v^2)(u^2 - 2uv - v^2)(u^2 + 2uv - v^2)$$
3. **Divisibility Invariant**:
   - Modulo 3: $3 \mid A$ for all primitive triples $(u, v)$.
   - Modulo 4: $4 \mid A$ since $n = 2uv$ and $b = 2mn$.
   - Modulo 7: $7 \mid A$ identically for all primitive generators $(u, v)$ via Fermat's Little Theorem.
   Hence $84 \mid A$ for **every** perfect right-angled triangle.
4. **Execution**:
   Since all perfect right-angled triangles are super-perfect, the answer is $0$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ closed-form proof. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
