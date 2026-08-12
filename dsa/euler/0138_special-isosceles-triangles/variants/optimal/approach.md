# Special Isosceles Triangles - Optimal Approach

## Algorithm Explanation

Find $\sum L$ for the $12$ smallest isosceles triangles with base $b$, equal leg lengths $L$, and height $h = b \pm 1$.

### Pell Equation Reduction:
Let $b = 2x$. Height $h = 2x \pm 1$.
Applying Pythagorean theorem:
$$h^2 + (b/2)^2 = L^2 \implies (2x \pm 1)^2 + x^2 = L^2 \implies 5x^2 \pm 4x + 1 = L^2$$

Multiplying by $5$ and completing the square:
$$(5x \pm 2)^2 - 5L^2 = -1$$

Letting $y = 5x \pm 2$, this reduces to the negative Pell equation $y^2 - 5L^2 = -1$.

### Linear Recurrence Relation:
The fundamental generator $(9 + 4\sqrt{5})$ produces the linear recurrence for leg lengths $L_k$:
$$L_k = 18 L_{k-1} - L_{k-2}$$

Starting with initial values $L_1 = 17$ and $L_2 = 305$, iterate $12$ terms and return $\sum_{k=1}^{12} L_k$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ where $K = 12$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
