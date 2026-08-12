# Laser Beam Reflections - Optimal Approach

## Algorithm Explanation

Find the total number of internal reflections a laser beam makes inside an elliptical white cell $4x^2 + y^2 = 100$ before escaping through a top hole $-0.01 \le x \le 0.01$ ($y > 0$).

### Vector Physics Reflection & Ellipse Intersection:
1. **Normal Gradient Vector**:
   The gradient of $F(x, y) = 4x^2 + y^2 - 100 = 0$ at $(x_1, y_1)$ is $\nabla F = (8x_1, 2y_1) \parallel (4x_1, y_1)$.
   Unit normal vector:
   $$\hat{N} = \frac{(4x_1, y_1)}{\|(4x_1, y_1)\|}$$
2. **Reflected Unit Direction Vector**:
   For normalized incident vector $\hat{V} = \frac{(x_1 - x_0, y_1 - y_0)}{\|(x_1 - x_0, y_1 - y_0)\|}$:
   $$\hat{R} = \hat{V} - 2(\hat{V} \cdot \hat{N})\hat{N}$$
3. **Ray-Ellipse Intersection**:
   Line equation: $(x(t), y(t)) = (x_1 + t R_x, y_1 + t R_y)$.
   Substituting into $4x(t)^2 + y(t)^2 = 100$ (with $4x_1^2 + y_1^2 = 100$) yields non-zero root:
   $$t = \frac{-2(4x_1 R_x + y_1 R_y)}{4 R_x^2 + R_y^2}$$
   Next impact point: $(x_2, y_2) = (x_1 + t R_x, y_1 + t R_y)$.
4. Repeat until exit condition $-0.01 \le x_1 \le 0.01$ and $y_1 > 0$ is satisfied.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(B)$ where $B = 354$ bounces ($4$ floating-point operations per bounce). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant memory.
