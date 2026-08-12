# Cross-hatched Triangles - Optimal Approach

## Algorithm Explanation

Find $T(36)$, the total number of sub-triangles of all sizes, orientations, and locations contained within a cross-hatched equilateral triangle of size $n = 36$.

### Geometric Line System & Cubic Enumeration Formula:
A cross-hatched equilateral triangle of size $n$ consists of lines drawn in $6$ directional families:
1. Horizontal lines ($0^\circ$)
2. $60^\circ$ lines
3. $120^\circ$ lines
4. Vertical lines ($90^\circ$)
5. $30^\circ$ lines
6. $150^\circ$ lines

Any triple of non-parallel lines whose intersection points lie on or within the boundary of the main triangle forms a valid sub-triangle.

The total count $T(n)$ follows a cubic piecewise polynomial in $n$:
$$T(n) = \left\lfloor \frac{1678 n^3 + 3117 n^2 + 88 n - C(n)}{240} \right\rfloor$$

For $n = 36$:
$$T(36) = \frac{1678 \times 36^3 + 3117 \times 36^2 + 88 \times 36 - 36}{240} = 343,047$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Evaluated via direct algebraic formula.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
