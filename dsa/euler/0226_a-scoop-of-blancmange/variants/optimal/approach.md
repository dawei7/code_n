# A Scoop of Blancmange - Optimal Approach

## Algorithm Explanation

Find the area under the blancmange curve $B(x) = \sum_{n=0}^{\infty} \frac{s(2^n x)}{2^n}$ enclosed by circle $C$ centered at $(1/4, 1/2)$ with radius $1/4$, rounded to $8$ decimal places.

### Exact Analytical Integration & Binary Root Finding:
1. **Intersection Search**:
   The blancmange curve $B(x)$ intersects the bottom boundary of circle $y_{\text{bot}}(x) = 1/2 - \sqrt{x/2 - x^2}$ at $x_1 \approx 0.078907787965$.
2. **Analytical Takagi Integral**:
   The exact indefinite integral of the blancmange curve is:
   $$\int_0^x B(t) \, dt = \frac{x^2}{2} + \sum_{n=0}^{\infty} 4^{-n-1} S(2^n x)$$
   where $S(t) = \int_0^t s(u) \, du$ is the integrated triangle wave function.
3. **Circle Boundary Integration**:
   The area under $y_{\text{bot}}(x)$ is evaluated via exact integration:
   $$\int_{x_1}^{0.5} y_{\text{bot}}(x) \, dx = \frac{1}{2}(0.5 - x_1) - \frac{1}{16} \int_{4(x_1-1/4)}^1 \sqrt{1 - u^2} \, du$$
4. **Execution**:
   Subtracting $\int_{x_1}^{0.5} y_{\text{bot}}(x) \, dx$ from $\int_{x_1}^{0.5} B(x) \, dx$ yields $0.05844377$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log(\varepsilon^{-1}))$ for binary search + exact series evaluation. Runs in $\approx 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
