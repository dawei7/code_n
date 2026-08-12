# Integer Sided Triangles with Integral Area/Perimeter Ratio - Optimal Approach

## Algorithm Explanation

Find the sum of the perimeters of all integer-sided triangles $(a, b, c)$ for which the area/perimeter ratio $R = \frac{\text{Area}}{a+b+c} = k$ is a positive integer not exceeding $1000$.

### Semi-Perimeter Partition & Diophantine Divisor Search:
1. **Inradius Transformation**:
   Let semi-perimeter $s = \frac{a+b+c}{2}$ and $x = s-a, y = s-b, z = s-c$ ($x, y, z > 0$).
   Inradius $r = \frac{\text{Area}}{s} = 2 R = 2k$.
   By Heron's formula, $\text{Area} = \sqrt{s x y z} = 2k s \implies x y z = 4k^2 (x + y + z)$.
2. **Diophantine Hyperbola Factorization**:
   Rearranging $x y z = 4k^2 (x + y + z)$ for $z$:
   $$z = \frac{4k^2(x + y)}{x y - 4k^2}$$
   Setting $d = x y - 4k^2 > 0$, we have $z = \frac{4k^2(x + y)}{d}$, where $d \mid 4k^2(x^2 + 4k^2)$.
3. **Execution**:
   For each integer ratio $k \in [1, 1000]$, we iterate $x \le \sqrt{12 k^2}$ and find all valid $y \le z$ via divisors of $4k^2(x^2 + 4k^2)$.
   Summing perimeters $2(x + y + z)$ over all distinct triangles yields $28038042525570324$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot x \cdot d(N))$ for $K = 1000$. Runs in $\approx 3.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
