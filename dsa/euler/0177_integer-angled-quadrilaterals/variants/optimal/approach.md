# Integer Angled Quadrilaterals - Optimal Approach

## Algorithm Explanation

Find the total number of non-similar convex quadrilaterals $ABCD$ whose $8$ corner angles formed by diagonals $AC, BD$ and sides have integer values in degrees.

### Trigonometric Law of Sines Relation:
Label the $8$ corner angles $(a, b, c, d, e, f, g, h)$ where $a, b$ are at $A$, $c, d$ at $B$, $e, f$ at $C$, $g, h$ at $D$.

By Law of Sines in the $4$ central triangles:
$$\sin(a) \cdot \sin(c) \cdot \sin(e) \cdot \sin(g) = \sin(b) \cdot \sin(d) \cdot \sin(f) \cdot \sin(h)$$

Given $a, b, c, d$:
- $h = 180^\circ - a - b - c$
- $e = 180^\circ - b - c - d$
- $S = f + g = 180^\circ - d - e$

Ratio of sines $K$:
$$K = \frac{\sin a \cdot \sin c \cdot \sin e}{\sin b \cdot \sin d \cdot \sin h}$$

Using $\frac{\sin f}{\sin(S - f)} = K$:
$$f = \text{atan2}(K \sin S, 1 + K \cos S)$$
$g = S - f$.

### Symmetry Pruning & Canonical Equivalence:
1. **Minimum Angle Bound**:
   By dihedral symmetry ($4$ rotations $\times$ $2$ reflections), the canonical representative orbit minimum has $a \le \lfloor 360^\circ / 8 \rfloor = 45^\circ$.
2. **Bounds Enforcement**:
   Prune search loops $b \ge a, c \ge a, d \ge a, e \ge a, h \ge a$.
3. **Integral Angle Check**:
   Validate $|f - \text{round}(f)| < 10^{-8}$.
4. **Canonical Orbit Deduplication**:
   Store $\min(o_1 \dots o_8)$ in a hash set to count non-similar quadrilaterals.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(45 \cdot 180^3 / 24)$ trigonometric iterations. Runs in $\approx 12\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{Unique Quads}) = 129,325$ tuples stored in `set()`.
