# Perfect Square Collection - Optimal Approach

## Algorithm Explanation

Find the smallest sum $x + y + z$ for positive integers $x > y > z > 0$ such that all six expressions $x+y, x-y, x+z, x-z, y+z, y-z$ are simultaneously perfect squares.

### Square Parameterization & Parity Constraints:
Let:
- $x + y = A^2$
- $x - y = B^2$
- $x + z = C^2$
- $x - z = D^2$
- $y + z = E^2$
- $y - z = F^2$

Solving for $x, y$:
$$x = \frac{A^2 + B^2}{2}, \quad y = \frac{A^2 - B^2}{2}$$

For $x, y$ to be integers, $A^2$ and $B^2$ must have the same parity (same parity for $A$ and $B$).

### Search Strategy:
1. Outer loop $A \in [3, \dots]$:
2. Inner loop $B \in [A \bmod 2, A-2, \dots]$ with same parity as $A$.
3. Compute candidate $x = \frac{A^2 + B^2}{2}$ and $y = \frac{A^2 - B^2}{2}$.
4. Loop candidate $C \in [\lfloor \sqrt{y} \rfloor + 1, A - 1]$ ($C^2 = x + z$):
   - Set $z = C^2 - x$. Filter $0 < z < y$.
   - Test if $D^2 = x - z$, $E^2 = y + z$, and $F^2 = y - z$ are all perfect squares using integer square root checks.
5. Return the first valid combination $x + y + z$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(A^2 \cdot C)$ bounded search ($A \le 1000$). Runs in $< 5.0\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
