# Guided Example: Convex Polygon

We trace the step-by-step 2D vector difference formulation, determinant cross product sign calculation ($x_1 y_2 - x_2 y_1$), turn orientation consistency (left turn vs right turn), collinear point handling ($cross == 0$), and reflex angle detection on representative ordered polygon vertices:

- **Input:** $points = [[0, 0], [0, 5], [5, 5], [5, 0]]$
- **Required output:** `true`
  - Number of vertices: $n = 4$
  - Geometric condition: A polygon is convex if and only if all turns along its boundary follow the exact same orientation (either strictly clockwise or strictly counterclockwise, allowing collinear straight segments).
- **Vector cross product execution trace:**
  - Let $P_i = points[i], \; P_{i+1} = points[(i+1)\%n], \; P_{i+2} = points[(i+2)\%n]$
  - Vector 1: $\vec{v}_1 = P_{i+1} - P_i = (x_1, y_1)$
  - Vector 2: $\vec{v}_2 = P_{i+2} - P_i = (x_2, y_2)$
  - Cross product determinant: $cur = x_1 y_2 - x_2 y_1$
  - Initial state: $pre = 0$
  - **Vertex 0 ($i = 0$): $P_0(0, 0), P_1(0, 5), P_2(5, 5)$**
    - $\vec{v}_1 = (0 - 0, 5 - 0) = (0, 5)$
    - $\vec{v}_2 = (5 - 0, 5 - 0) = (5, 5)$
    - $cur = (0)(5) - (5)(5) = 0 - 25 = \mathbf{-25}$ (Clockwise turn, Right)
    - Set reference sign: $pre \leftarrow -25$
  - **Vertex 1 ($i = 1$): $P_1(0, 5), P_2(5, 5), P_3(5, 0)$**
    - $\vec{v}_1 = (5 - 0, 5 - 5) = (5, 0)$
    - $\vec{v}_2 = (5 - 0, 0 - 5) = (5, -5)$
    - $cur = (5)(-5) - (5)(0) = -25 - 0 = \mathbf{-25}$
    - Sign check: $cur \times pre = (-25) \times (-25) > 0$ (**Consistent!**)
  - **Vertex 2 ($i = 2$): $P_2(5, 5), P_3(5, 0), P_0(0, 0)$**
    - $\vec{v}_1 = (5 - 5, 0 - 5) = (0, -5)$
    - $\vec{v}_2 = (0 - 5, 0 - 5) = (-5, -5)$
    - $cur = (0)(-5) - (-5)(-5) = 0 - 25 = \mathbf{-25}$
    - Sign check: $cur \times pre > 0$ (**Consistent!**)
  - **Vertex 3 ($i = 3$): $P_3(5, 0), P_0(0, 0), P_1(0, 5)$**
    - $\vec{v}_1 = (0 - 5, 0 - 0) = (-5, 0)$
    - $\vec{v}_2 = (0 - 5, 5 - 0) = (-5, 5)$
    - $cur = (-5)(5) - (-5)(0) = -25 - 0 = \mathbf{-25}$
    - Sign check: $cur \times pre > 0$ (**Consistent!**)
  - All 4 corners have identical negative cross products. Zero reflex angles exist.
  - Return **`true`**.
- **Concave Polygon Instance:** $points = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]$
  - Inward dent at $(5, 5)$ produces a positive cross product ($+50$) while preceding turns are negative ($-50$).
  - Sign product: $(-50) \times (+50) < 0 \implies$ **Reflex angle $\implies$ `false`**
- **Collinear Edge Points:** Three points along a straight edge produce $cur = 0$. Zero cross products do not indicate turns and are safely skipped.

This instance demonstrates orientation tests in 2D computational geometry, mathematically proves why uniform cross product signs characterize convexity, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of points representing the vertices of a polygon in ordered traversal:
Determine if the polygon is **convex**.
A polygon is convex if and only if all interior angles are strictly $\le 180^\circ$, meaning the path never turns "inward" (no reflex vertices).

```text
Convex Square (All Right Turns):
  (0, 5) ------ (5, 5)
    ^             |
    |             v
  (0, 0) <----- (5, 0)
  Every turn is clockwise -> Consistent sign -> Convex (true)

Concave Polygon (With Inward Dent):
  (0, 10) ----- (10, 10)
    ^              |
    |    (5, 5)    v
    |     /  \     |
  (0, 0)      (10, 0)
  The vertex (5, 5) turns the opposite way (reflex angle) -> false
```

### The 2D Cross Product Orientation Test
In 2D planar geometry:
Given three ordered points $A(x_0, y_0), B(x_1, y_1), C(x_2, y_2)$:
Form the two directional vectors from $A$:
$$
\vec{v}_1 = \vec{AB} = (x_1 - x_0, \; y_1 - y_0)
$$
$$
\vec{v}_2 = \vec{AC} = (x_2 - x_0, \; y_2 - y_0)
$$
Their 2D cross product (determinant of the $2 \times 2$ matrix) is:
$$
\text{cross}(\vec{v}_1, \vec{v}_2) = v_{1x} v_{2y} - v_{1y} v_{2x}
$$
- If $\text{cross} > 0$: $\vec{v}_2$ is counterclockwise from $\vec{v}_1$ (Left turn).
- If $\text{cross} < 0$: $\vec{v}_2$ is clockwise from $\vec{v}_1$ (Right turn).
- If $\text{cross} == 0$: $A, B, C$ are collinear.
**Convexity Criterion:** All non-zero cross products along the polygon's perimeter must have the **exact same sign**. If any turn changes direction (from clockwise to counterclockwise, or vice versa), the polygon is concave.

---

## 2. Conceptual Foundation & Invariants

### 1. Cyclic Modular Neighbor Access:
For an $n$-vertex polygon:
At each index $i \in [0, n - 1]$, inspect the triplet:
$$
P_i = points[i], \quad P_{i+1} = points[(i + 1) \pmod n], \quad P_{i+2} = points[(i + 2) \pmod n]
$$

### 2. Sign Invariance Tracking:
Maintain a variable $pre$ initialized to $0$:
- Compute $cur = (P_{i+1}.x - P_i.x)(P_{i+2}.y - P_i.y) - (P_{i+2}.x - P_i.x)(P_{i+1}.y - P_i.y)$.
- If $cur \ne 0$:
  - If $cur \times pre < 0$: The current turn has the opposite orientation of previous turns. Return `False`.
  - Update: $pre \leftarrow cur$.
- If the loop completes without sign contradiction, return `True`.

> **Orientation Invariant.** A simple polygon is convex if and only if its signed curvature has constant sign throughout its boundary.

---

## 3. Step-by-Step Worked Execution

We trace $points = [(0, 0), (0, 5), (5, 5), (5, 0)]$ ($n = 4$):
Initialize $pre = 0$.

---

### Step 1: Triplet at $i = 0$
- Points: $P_0(0, 0), \; P_1(0, 5), \; P_2(5, 5)$.
- Vectors:
  $$
  \vec{v}_1 = (0 - 0, 5 - 0) = (0, 5)
  $$
  $$
  \vec{v}_2 = (5 - 0, 5 - 0) = (5, 5)
  $$
- Cross product:
  $$
  cur = (0)(5) - (5)(5) = 0 - 25 = \mathbf{-25}
  $$
- Sign check: $pre = 0$, so no prior sign. Set $pre \leftarrow -25$.

---

### Step 2: Triplet at $i = 1$
- Points: $P_1(0, 5), \; P_2(5, 5), \; P_3(5, 0)$.
- Vectors:
  $$
  \vec{v}_1 = (5 - 0, 5 - 5) = (5, 0)
  $$
  $$
  \vec{v}_2 = (5 - 0, 0 - 5) = (5, -5)
  $$
- Cross product:
  $$
  cur = (5)(-5) - (5)(0) = -25 - 0 = \mathbf{-25}
  $$
- Sign check:
  $$
  cur \times pre = (-25) \times (-25) = 625 > 0 \quad (\text{Pass})
  $$

---

### Step 3: Triplet at $i = 2$
- Points: $P_2(5, 5), \; P_3(5, 0), \; P_0(0, 0)$.
- Vectors:
  $$
  \vec{v}_1 = (5 - 5, 0 - 5) = (0, -5)
  $$
  $$
  \vec{v}_2 = (0 - 5, 0 - 5) = (-5, -5)
  $$
- Cross product:
  $$
  cur = (0)(-5) - (-5)(-5) = 0 - 25 = \mathbf{-25}
  $$
- Sign check:
  $$
  cur \times pre = 625 > 0 \quad (\text{Pass})
  $$

---

### Step 4: Triplet at $i = 3$
- Points: $P_3(5, 0), \; P_0(0, 0), \; P_1(0, 5)$.
- Vectors:
  $$
  \vec{v}_1 = (0 - 5, 0 - 0) = (-5, 0)
  $$
  $$
  \vec{v}_2 = (0 - 5, 5 - 0) = (-5, 5)
  $$
- Cross product:
  $$
  cur = (-5)(5) - (-5)(0) = -25 - 0 = \mathbf{-25}
  $$
- Sign check:
  $$
  cur \times pre = 625 > 0 \quad (\text{Pass})
  $$

---

### Termination:
All 4 vertices evaluated with zero sign reversals.
Return **`true`**.

---

## 4. Complete Execution Trace

| Triplet Center $i$ | Vertices Inspected | Vector $\vec{v}_1$ | Vector $\vec{v}_2$ | Cross Product $cur$ | Turn Direction | Sign Product $cur \times pre$ | Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $(0,0) \to (0,5) \to (5,5)$ | $(0, 5)$ | $(5, 5)$ | **$-25$** | Clockwise | Initial | Pass |
| **$1$** | $(0,5) \to (5,5) \to (5,0)$ | $(5, 0)$ | $(5, -5)$ | **$-25$** | Clockwise | $+625 > 0$ | Pass |
| **$2$** | $(5,5) \to (5,0) \to (0,0)$ | $(0, -5)$ | $(-5, -5)$ | **$-25$** | Clockwise | $+625 > 0$ | Pass |
| **$3$** | $(5,0) \to (0,0) \to (0,5)$ | $(-5, 0)$ | $(-5, 5)$ | **$-25$** | Clockwise | $+625 > 0$ | Pass |
| **Final** | All 4 checked | — | — | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Polygon ($n = 3$, Triangle):** Any non-degenerate triangle is strictly convex $\implies \mathbf{true}$.
- **Collinear Intermediate Points ($[(0, 0), (0, 2), (0, 5), (5, 5), (5, 0)]$):** Triplet $(0,0) \to (0,2) \to (0,5)$ has $cur = 0$. Handled by `if cur != 0`, ignoring straight edges without flagging errors.
- **Reflex Vertex ($cur$ flips sign):** When cross products mix positive and negative signs, `cur * pre < 0` triggers immediately $\implies \mathbf{false}$.
- **Reversed Traversal Order:** A counterclockwise polygon produces all positive cross products ($cur > 0$), which is equally valid and returns `true`.

---

## 6. Traps & Common Anti-Patterns

- **Using Division or Slopes ($y / x$):** Dividing by $\Delta x$ causes ZeroDivisionError on vertical lines. Using cross products ($x_1 y_2 - x_2 y_1$) relies purely on integer multiplication, with zero division risks.
- **Integer Overflow in Cross Products:** If coordinates reach $10^4$, cross products can reach $2 \times 10^8$, and their product $cur \times pre$ can reach $4 \times 10^{16}$. In languages with 32-bit integers (C++), using 64-bit integers (`long long`) prevents signed overflow.
- **Treating $cur == 0$ as a Direction Change:** Collinear points lie on the same straight edge and do not bend the boundary. Resetting or comparing signs on zero cross products causes false negatives on polygons with collinear vertices.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop iterates through all $N$ vertices once.
  - Each iteration performs $O(1)$ scalar multiplications and subtractions.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ using scalar coordinate and sign variables.
