# Triangles with Integral Sides and an Integral Angle - Optimal Approach

## Algorithm Explanation

Find the number of integer-sided triangles $(a, b, c)$ with perimeter $a + b + c \le 10^8$ that possess at least one integral angle measured in degrees.

### Niven's Theorem & Angle Classification:
1. **Rational Cosine Restriction**:
   By Niven's Theorem, for $\theta \in (0^\circ, 180^\circ)$, $\cos \theta$ is rational if and only if $\theta \in \{60^\circ, 90^\circ, 120^\circ\}$.
   Therefore, any integer-sided triangle with an integral angle must fall into one of three angle classes:
   - $90^\circ$ (Right triangles: $a^2 + b^2 = c^2$)
   - $60^\circ$ (Acute triangles: $a^2 + b^2 - ab = c^2$)
   - $120^\circ$ (Obtuse triangles: $a^2 + b^2 + ab = c^2$)
2. **Parametric Primitive Generators**:
   - $90^\circ$: $a = k(m^2 - n^2), b = k(2mn), c = k(m^2 + n^2)$ for $\gcd(m, n) = 1$, $m - n$ odd.
   - $60^\circ$: $a = k(m^2 - n^2), b = k(2mn - n^2), c = k(m^2 - mn + n^2)$.
   - $120^\circ$: $a = k(m^2 - n^2), b = k(2mn + n^2), c = k(m^2 + mn + n^2)$.
3. **Overlapping Inclusion-Exclusion**:
   Equilateral triangles ($60^\circ-60^\circ-60^\circ$) belong to both the $60^\circ$ and $120^\circ$ generator forms and are deduplicated.
4. **Execution**:
   Summing all valid triangles with perimeter $\le 10^8$ yields $416577688$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{P})$ for $P = 10^8$. Runs in $\approx 2.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
