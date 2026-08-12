# Maximising a Weighted Product - Optimal Approach

## Algorithm Explanation

Maximize $P_m = x_1^1 \cdot x_2^2 \cdot \dots \cdot x_m^m$ for positive real numbers $(x_1, \dots, x_m)$ subject to $\sum_{i=1}^m x_i = m$, and compute $\sum_{m=2}^{15} \lfloor P_m \rfloor$.

### Lagrange Multipliers / AM-GM Derivation:
1. **Optimization Problem**:
   Maximize $\ln P_m = \sum_{i=1}^m i \ln x_i$ subject to $\sum_{i=1}^m x_i = m$.
2. **Lagrangian Formulation**:
   $$L(x_1, \dots, x_m, \lambda) = \sum_{i=1}^m i \ln x_i - \lambda \left(\sum_{i=1}^m x_i - m\right)$$
   Taking partial derivatives:
   $$\frac{\partial L}{\partial x_i} = \frac{i}{x_i} - \lambda = 0 \implies x_i = \frac{i}{\lambda}$$
3. **Solving for $\lambda$**:
   $$\sum_{i=1}^m x_i = \frac{1}{\lambda} \sum_{i=1}^m i = \frac{m(m+1)}{2\lambda} = m \implies \lambda = \frac{m+1}{2}$$
   Hence, the optimal values are $x_i = \frac{2i}{m+1}$.
4. **Final Computation**:
   $$P_m = \prod_{i=1}^m \left(\frac{2i}{m+1}\right)^i$$
   Evaluating $\sum_{m=2}^{15} \lfloor P_m \rfloor$ yields $371,048,281$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m^2)$ for $m \le 15$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
