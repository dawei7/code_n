# Right Triangles with Integer Coordinates - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

The points $P(x_1, y_1)$ and $Q(x_2, y_2)$ are plotted at integer coordinates and are joined to the origin $O(0, 0)$ to form $\triangle OPQ$.
The coordinates satisfy $0 \le x_1, y_1, x_2, y_2 \le N$.

For $N = 2$, there are exactly fourteen ($14$) right-angled triangles that can be formed.

The objective is to find the number of **right-angled triangles $\triangle OPQ$** that can be formed for $N = 50$:
$$N_{\text{right}} = \left| \left\{ \{P, Q\} \subset ([0, N] \times [0, N]) \setminus \{O\} \;\middle|\; P \neq Q \land \triangle OPQ \text{ has a right angle} \right\} \right|$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### 4D Coordinate Cartesian Loop
A naive algorithm loops through all $P(x_1, y_1)$ and $Q(x_2, y_2)$ in $\mathcal{O}(N^4)$ time:
```python
def naive_right_triangles(n):
    # checks 50^4 = 6.25 million point pairs with vector dot products
    # ...
```

### Geometric Vertex Case Classification
1. **Case 1 (Right angle at origin $O(0,0)$):**
   - $P$ must lie on the x-axis ($N$ choices) and $Q$ on the y-axis ($N$ choices) $\implies N^2$ triangles.
2. **Case 2 (Right angle on the coordinate axes at $P$ or $Q$):**
   - $P$ on x-axis ($x_1 > 0, y_1 = 0$), $Q$ directly vertical $(x_1, y_2)$ with $y_2 > 0$ ($N^2$ triangles).
   - $P$ on y-axis ($x_1 = 0, y_1 > 0$), $Q$ directly horizontal $(x_2, y_1)$ with $x_2 > 0$ ($N^2$ triangles).
   - Total axis right-angle triangles $= 2N^2$.
3. **Case 3 (Right angle at interior point $P(x_1, y_1)$ with $x_1, y_1 > 0$):**
   - Vector $\vec{OP} = (x_1, y_1)$ has perpendicular direction $(\Delta x, \Delta y) = (y_1 / g, x_1 / g)$ where $g = \gcd(x_1, y_1)$.
   - Stepping in both perpendicular directions within the bounding box $[0, N] \times [0, N]$ counts points $Q$ in $\mathcal{O}(1)$ time per point $P$.

---

## 3. Core Intuition & Mathematical Structure

### Geometric Case Breakdown of Right-Angled Triangles $\triangle OPQ$

| Case | Right Angle Vertex Location | Geometry & Configuration | Count Formula | Count for $N = 2$ |
| :---: | :---: | :--- | :---: | :---: |
| **Case 1** | Origin $O(0, 0)$ | $P$ on x-axis, $Q$ on y-axis | $N^2$ | $4$ |
| **Case 2** | On Axes ($P$ or $Q$) | Vertical from x-axis + Horizontal from y-axis | $2N^2$ | $8$ |
| **Case 3** | Interior $P(x_1, y_1)$ | Perpendicular vector stepping $(\pm \Delta x, \mp \Delta y)$ | $\sum \left( k_1 + k_2 \right)$ | $2$ |
| **Total** | — | Sum of all 3 geometric cases | — | **$14$ (Sample)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Perpendicular Direction Stepping Formula
For each point $P(x_1, y_1) \in [1, N]^2$:
1. $g = \gcd(x_1, y_1), \, \Delta x = y_1 / g, \, \Delta y = x_1 / g$.
2. **Direction 1 (Down-Right):** $(x_1 + k \Delta x, y_1 - k \Delta y) \in [0, N]^2$:
   $$k_1 = \min\left( \left\lfloor \frac{N - x_1}{\Delta x} \right\rfloor, \, \left\lfloor \frac{y_1}{\Delta y} \right\rfloor \right)$$
3. **Direction 2 (Up-Left):** $(x_1 - k \Delta x, y_1 + k \Delta y) \in [0, N]^2$:
   $$k_2 = \min\left( \left\lfloor \frac{x_1}{\Delta x} \right\rfloor, \, \left\lfloor \frac{N - y_1}{\Delta y} \right\rfloor \right)$$
4. Total right-angled triangles:
   $$N_{\text{right}} = 3N^2 + \sum_{x_1=1}^N \sum_{y_1=1}^N (k_1 + k_2)$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $N = 2$
- Case 1 (Origin): $2^2 = \mathbf{4}$.
- Case 2 (Axes): $2 \times 2^2 = \mathbf{8}$.
- Case 3 (Interior):
  - $(1, 2) \implies g = 1, \Delta x = 2, \Delta y = 1$: $k_1 = \min(0, 2) = 0, k_2 = \min(0, 0) = 0$.
  - $(2, 1) \implies g = 1, \Delta x = 1, \Delta y = 2$: $k_1 = \min(0, 0) = 0, k_2 = \min(2, 0) = 0$.
  - $(1, 1) \implies g = 1, \Delta x = 1, \Delta y = 1$:
    - $k_1 = \min(1, 1) = \mathbf{1} \implies Q = (2, 0)$.
    - $k_2 = \min(1, 1) = \mathbf{1} \implies Q = (0, 2)$.
    - Sum for $(1, 1) = \mathbf{2}$.
- Total for $N = 2$: $4 + 8 + 2 = \mathbf{14}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $N = 50$
- Summing all 3 cases up to $N = 50$:
  $$N_{\text{right}} = \mathbf{14\,234}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Axis Base** | `count = 3 * n * n` | $\mathcal{O}(1)$ |
| **Stage 2** | **Interior Loop $x_1, y_1$** | For $x_1 \in [1, N]$, for $y_1 \in [1, N]$ | $N^2$ iterations |
| **Stage 3** | **GCD Step Vectors** | $g = \gcd(x_1, y_1), \, \Delta x = y_1 // g, \, \Delta y = x_1 // g$ | $\mathcal{O}(\log N)$ |
| **Stage 4** | **Boundary Bounds** | Add $\min((N-x_1)//\Delta x, y_1//\Delta y) + \min(x_1//\Delta x, (N-y_1)//\Delta y)$ | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return scalar integer $14234$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2)$ where $N = 50$ ($2500$ points) | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar integer registers |
| **Dynamic Execution** | $100\%$ Inline | Geometric vector perpendicular projection |

### Critical Invariants & Edge Cases Handled:
1. **Unordered Point Pair Invariance**: Evaluating right-angles specifically at $P(x_1, y_1)$ naturally avoids counting the same triangle $\triangle OPQ$ multiple times.
2. **Boundary Precision**: The $\min$ expressions enforce that $Q$ strictly remains within the bounding box $[0, N] \times [0, N]$.
