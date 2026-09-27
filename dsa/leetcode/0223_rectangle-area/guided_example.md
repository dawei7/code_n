# Guided Example: Rectangle Area

We trace the step-by-step inclusion-exclusion area decomposition, independent 1D interval projection clamping, and phantom overlap prevention on representative 2D coordinate rectangles:

- **Input:** $ax_1 = -3, \, ay_1 = 0, \, ax_2 = 3, \, ay_2 = 4, \quad bx_1 = 0, \, by_1 = -1, \, bx_2 = 9, \, by_2 = 2$
- **Required output:** $45$ ($\text{Area}_A = 24, \, \text{Area}_B = 27, \, \text{Overlap} = 6 \implies 24 + 27 - 6 = 45$)
- **Identical Rectangles Instance:** $[-2, -2, 2, 2]$ and $[-2, -2, 2, 2] \implies 16 + 16 - 16 = 16$
- **Completely Disjoint Instance:** $[0, 0, 1, 1]$ and $[2, 2, 3, 3] \implies 1 + 1 - 0 = 2$ (Diagonal separation with zero intersection)
- **Touching Edges Instance:** $[0, 0, 2, 2]$ and $[2, 0, 4, 2] \implies 4 + 4 - 0 = 8$ ($\text{overlap}_x = 0$)

This instance demonstrates geometric inclusion-exclusion ($\text{Area}(A \cup B) = \text{Area}(A) + \text{Area}(B) - \text{Area}(A \cap B)$), mathematically exposes the phantom overlap trap ($(- \Delta x) \times (- \Delta y) > 0$) when non-intersecting rectangles are not clamped per-axis, and computes the exact union in strictly $O(1)$ time.

---

## 1. Instance & Teaching Goal

Given two axis-aligned rectilinear rectangles in the Cartesian plane:
- **Rectangle A:** Bottom-left $(-3, 0)$, Top-right $(3, 4)$.
- **Rectangle B:** Bottom-left $(0, -1)$, Top-right $(9, 2)$.

Calculate the total 2D area covered by the union of both rectangles.

### The Inclusion-Exclusion Principle
Summing the individual rectangle areas counts their intersection twice:
$$
\text{Total Area} = \text{Area}(A) + \text{Area}(B) - \text{Area}(A \cap B)
$$
1. **Individual Areas:**
   - Width of $A$: $\Delta x_A = ax_2 - ax_1 = 3 - (-3) = 6$.
   - Height of $A$: $\Delta y_A = ay_2 - ay_1 = 4 - 0 = 4$.
   - $\text{Area}(A) = 6 \times 4 = \mathbf{24}$.
   - Width of $B$: $\Delta x_B = bx_2 - bx_1 = 9 - 0 = 9$.
   - Height of $B$: $\Delta y_B = by_2 - by_1 = 2 - (-1) = 3$.
   - $\text{Area}(B) = 9 \times 3 = \mathbf{27}$.
2. **Intersection Geometry:**
   Because both rectangles are axis-aligned, their 2D intersection is itself an axis-aligned rectangle formed by the independent 1D overlaps on the $x$-axis and $y$-axis:
   $$
   \text{Overlap Width} = \max\big(0, \; \min(ax_2, bx_2) - \max(ax_1, bx_1)\big) = \max(0, 3 - 0) = \mathbf{3}
   $$
   $$
   \text{Overlap Height} = \max\big(0, \; \min(ay_2, by_2) - \max(ay_1, by_1)\big) = \max(0, 2 - 0) = \mathbf{2}
   $$
   $$
   \text{Area}(A \cap B) = 3 \times 2 = \mathbf{6}
   $$
3. **Union Calculation:**
   $$
   \text{Total Area} = 24 + 27 - 6 = \mathbf{45}
   $$

---

## 2. Conceptual Foundation & Invariants

### 1D Projection Overlap Formula
For any two 1D intervals $[x_1, x_2]$ and $[x_3, x_4]$:
The intersection begins at the **later start** $\max(x_1, x_3)$ and ends at the **earlier finish** $\min(x_2, x_4)$.
The overlapping length is:
$$
\text{overlap} = \max\big(0, \; \min(x_2, x_4) - \max(x_1, x_3)\big)
$$

### The Phantom Overlap Fallacy
Why is clamping with $\max(0, \dots)$ mandatory on **each axis separately**?
Consider two diagonally separated disjoint rectangles:
- Horizontal span: $A$ is $[0, 1]$, $B$ is $[2, 3]$. Raw $\Delta x = \min(1, 3) - \max(0, 2) = 1 - 2 = -1$.
- Vertical span: $A$ is $[0, 1]$, $B$ is $[2, 3]$. Raw $\Delta y = \min(1, 3) - \max(0, 2) = 1 - 2 = -1$.
If one blindly calculates $\max(0, \Delta x \times \Delta y)$:
$$
\Delta x \times \Delta y = (-1) \times (-1) = \mathbf{+1} > 0!
$$
The product of two negative gaps becomes a positive number, falsely claiming a non-existent overlap area of $1$!
Clamping each axis independently ($\max(0, -1) = 0$) ensures $0 \times 0 = 0$.

> **Invariant.** Two axis-aligned rectangles have non-zero intersection area if and only if both $\text{overlap}_x > 0$ and $\text{overlap}_y > 0$.

---

## 3. Step-by-Step Worked Execution

We trace the calculation on the input coordinates:
- $A: [-3, 0] \to [3, 4]$
- $B: [0, -1] \to [9, 2]$

### Step 1: Compute Area of Rectangle A
- $\text{width}_A = 3 - (-3) = 6$.
- $\text{height}_A = 4 - 0 = 4$.
- $\text{Area}_A = 6 \times 4 = \mathbf{24}$.

---

### Step 2: Compute Area of Rectangle B
- $\text{width}_B = 9 - 0 = 9$.
- $\text{height}_B = 2 - (-1) = 3$.
- $\text{Area}_B = 9 \times 3 = \mathbf{27}$.

---

### Step 3: Compute Horizontal Overlap ($x$-axis)
- Left boundary of intersection:
  $$
  x_{\text{left}} = \max(ax_1, bx_1) = \max(-3, 0) = \mathbf{0}
  $$
- Right boundary of intersection:
  $$
  x_{\text{right}} = \min(ax_2, bx_2) = \min(3, 9) = \mathbf{3}
  $$
- Horizontal span:
  $$
  \text{overlap}_x = \max(0, \; x_{\text{right}} - x_{\text{left}}) = \max(0, \; 3 - 0) = \mathbf{3}
  $$

---

### Step 4: Compute Vertical Overlap ($y$-axis)
- Bottom boundary of intersection:
  $$
  y_{\text{bottom}} = \max(ay_1, by_1) = \max(0, -1) = \mathbf{0}
  $$
- Top boundary of intersection:
  $$
  y_{\text{top}} = \min(ay_2, by_2) = \min(4, 2) = \mathbf{2}
  $$
- Vertical span:
  $$
  \text{overlap}_y = \max(0, \; y_{\text{top}} - y_{\text{bottom}}) = \max(0, \; 2 - 0) = \mathbf{2}
  $$

---

### Step 5: Intersection and Union Aggregation
- Intersection Area:
  $$
  \text{Area}_{\text{overlap}} = \text{overlap}_x \times \text{overlap}_y = 3 \times 2 = \mathbf{6}
  $$
- Union Total Area:
  $$
  \text{Total Area} = \text{Area}_A + \text{Area}_B - \text{Area}_{\text{overlap}} = 24 + 27 - 6 = \mathbf{45}
  $$

---

## 4. Complete Execution Trace

```text
Rectangle A: [-3, 0] to [3, 4] -> Width = 6, Height = 4 -> Area_A = 24
Rectangle B: [ 0, -1] to [9, 2] -> Width = 9, Height = 3 -> Area_B = 27

Overlap X: max(0, min(3, 9) - max(-3, 0)) = max(0, 3 - 0) = 3
Overlap Y: max(0, min(4, 2) - max(0, -1)) = max(0, 2 - 0) = 2

Overlap Area = 3 * 2 = 6

Total Area = Area_A + Area_B - Overlap Area
           = 24 + 27 - 6 = 45
```

| Geometric Component | Lower Bound | Upper Bound | Dimension Length | Computed Area Contribution |
|:---|:---:|:---:|:---:|:---:|
| **Rectangle A ($x, y$)** | $(-3, 0)$ | $(3, 4)$ | $6 \times 4$ | $\mathbf{+24}$ |
| **Rectangle B ($x, y$)** | $(0, -1)$ | $(9, 2)$ | $9 \times 3$ | $\mathbf{+27}$ |
| **Overlap $x$-axis** | $x = \max(-3, 0) = 0$ | $x = \min(3, 9) = 3$ | $\Delta x = 3$ | - |
| **Overlap $y$-axis** | $y = \max(0, -1) = 0$ | $y = \min(4, 2) = 2$ | $\Delta y = 2$ | - |
| **Intersection ($A \cap B$)** | $(0, 0)$ | $(3, 2)$ | $3 \times 2$ | $\mathbf{-6}$ |
| **Total Union ($A \cup B$)** | - | - | - | **$24 + 27 - 6 = \mathbf{45}$** |

---

## 5. Algorithmic Correctness

**Soundness.** The area of an axis-aligned rectangle is the product of its width and height. By standard measure theory and the Principle of Inclusion-Exclusion, $\mu(A \cup B) = \mu(A) + \mu(B) - \mu(A \cap B)$. Clamping $\Delta x$ and $\Delta y$ at 0 guarantees that when no intersection exists, the subtracted term is exactly 0.

**Completeness.** Every point $(x, y) \in \mathbb{R}^2$ covered by at least one rectangle is counted. Points covered by both rectangles are added twice and subtracted once, ensuring every point in the union is counted exactly once.

---

## 6. Traps This Instance Exposes

- **Unclamped Negative Dimension Multiplication:** Multiplying $\Delta x \times \Delta y$ before applying $\max(0, \dots)$ causes two negative gaps to produce a positive number, hallucinating false overlap for disjoint diagonal rectangles.
- **Integer Overflow in Fixed-Width Languages:** In languages like C++ / Java, coordinates up to $10^4$ yield products up to $10^8$ (fitting in 32-bit signed integers). However, if coordinates were up to $10^9$, 64-bit integers (`long long`) would be required.
- **Touching Edges vs Overlap:** If rectangles touch at an edge (e.g. $ax_2 = bx_1$), $\min(ax_2, bx_2) - \max(ax_1, bx_1) = 0$. $\text{overlap}_x = 0$, yielding $\text{Area}_{\text{overlap}} = 0$, which correctly reflects that line boundaries have zero 2D Lebesgue measure.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. Computing the bounds requires 4 subtractions, 4 comparisons ($\min / \max$), and 3 multiplications.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory.
