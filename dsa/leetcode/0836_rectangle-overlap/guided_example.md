# Guided Example: Rectangle Overlap

We trace the step-by-step 2D Cartesian orthogonal projection decomposition, 1D open interval intersection testing ($\max(a_1, b_1) < \min(a_2, b_2)$), Separating Axis Theorem non-overlap boundary conditions ($x_3 \ge x_2 \lor x_4 \le x_1 \lor y_3 \ge y_2 \lor y_4 \le y_1$), degenerate boundary contact rejection (zero-area edge/corner touch), and boolean overlap evaluation on representative axis-aligned rectangles:

- **Input:**
  $$
  rec1 = [0, 0, 2, 2], \quad rec2 = [1, 1, 3, 3]
  $$
- **Required output:** `true`
  - Rectangle geometry specifications:
    - Rectangles are axis-aligned and defined by their bottom-left corner $(x_1, y_1)$ and top-right corner $(x_2, y_2)$.
    - Two rectangles **overlap** if and only if the **area of their intersection is strictly positive**:
      $$
      \text{Area}(rec1 \cap rec2) > 0
      $$
    - Contact along an edge or at a single corner vertex has zero area and is **not** considered an overlap.
    - For $rec1 = [0, 0, 2, 2]$ and $rec2 = [1, 1, 3, 3]$:
      - $X$-axis projection of $rec1$: interval $(0, 2)$.
      - $X$-axis projection of $rec2$: interval $(1, 3)$.
      - $X$-axis overlap: $(\max(0, 1), \min(2, 3)) = (1, 2)$ with width $2 - 1 = \mathbf{1 > 0}$.
      - $Y$-axis projection of $rec1$: interval $(0, 2)$.
      - $Y$-axis projection of $rec2$: interval $(1, 1)$ to $(1, 3) \implies (1, 3)$.
      - $Y$-axis overlap: $(\max(0, 1), \min(2, 3)) = (1, 2)$ with height $2 - 1 = \mathbf{1 > 0}$.
      - Overlap region is the rectangle $[1, 1, 2, 2]$ with area $1 \times 1 = \mathbf{1 > 0}$.
      - Result: **`true`**.
- **Separating Axis Theorem & 1D Projection Invariant:**
  - **The Dimension Independence Principle:**
    - A 2D axis-aligned rectangle is the Cartesian product of two independent 1D intervals:
      $$
      rec = [x_{\min}, x_{\max}] \times [y_{\min}, y_{\max}]
      $$
    - The intersection of two such rectangles is also a rectangle:
      $$
      rec1 \cap rec2 = \big([x_1, x_2] \cap [x_3, x_4]\big) \times \big([y_1, y_2] \cap [y_3, y_4]\big)
      $$
    - The area is strictly positive if and only if **both 1D interval intersections have strictly positive length**:
      $$
      \text{Width} = \min(x_2, x_4) - \max(x_1, x_3) > 0
      $$
      $$
      \text{Height} = \min(y_2, y_4) - \max(y_1, y_3) > 0
      $$
  - **The Four Non-Overlap Separation Conditions:**
    - By De Morgan's laws, $rec2$ fails to overlap $rec1$ if and only if $rec2$ is separated along at least one cardinal direction:
      1. **Separated to the Right:** $x_3 \ge x_2$ (all of $rec2$ lies on or to the right of $rec1$).
      2. **Separated to the Left:** $x_4 \le x_1$ (all of $rec2$ lies on or to the left of $rec1$).
      3. **Separated Above:** $y_3 \ge y_2$ (all of $rec2$ lies on or above $rec1$).
      4. **Separated Below:** $y_4 \le y_1$ (all of $rec2$ lies on or below $rec1$).
    - If **none** of these 4 separation conditions hold, the rectangles must have a positive interior intersection!
      $$
      \text{Overlap} \iff \neg(x_3 \ge x_2 \lor x_4 \le x_1 \lor y_3 \ge y_2 \lor y_4 \le y_1)
      $$
- **Step-by-Step Worked Execution Trace on the Sample Pair:**
  - Coordinates:
    - $rec1$: $x_1 = 0, y_1 = 0, x_2 = 2, y_2 = 2$
    - $rec2$: $x_3 = 1, y_3 = 1, x_4 = 3, y_4 = 3$
  - **Check Separation Condition 1 (Right Separation, $x_3 \ge x_2$):**
    - $1 \ge 2 \implies \mathbf{False.}$
  - **Check Separation Condition 2 (Left Separation, $x_4 \le x_1$):**
    - $3 \le 0 \implies \mathbf{False.}$
  - **Check Separation Condition 3 (Top Separation, $y_3 \ge y_2$):**
    - $1 \ge 2 \implies \mathbf{False.}$
  - **Check Separation Condition 4 (Bottom Separation, $y_4 \le y_1$):**
    - $3 \le 0 \implies \mathbf{False.}$
  - **Disjunction Evaluation:**
    $$
    \text{Separated} = \text{False} \lor \text{False} \lor \text{False} \lor \text{False} = \mathbf{False}
    $$
  - **Overlap Determination:**
    $$
    \text{Overlap} = \neg(\text{False}) = \mathbf{True}
    $$
- **Shared Edge Touch Trace ($rec1 = [0, 0, 1, 1], rec2 = [1, 0, 2, 1]$):**
  - $rec1$ right edge is $x_2 = 1$. $rec2$ left edge is $x_3 = 1$.
  - Evaluate right separation:
    $$
    x_3 \ge x_2 \iff 1 \ge 1 \implies \mathbf{True!}
    $$
  - The shared line segment $x = 1, y \in [0, 1]$ has width $0$, yielding area $0$.
  - Output: **`false`** (non-overlapping).
- **Corner Touch Trace ($rec1 = [0, 0, 1, 1], rec2 = [1, 1, 2, 2]$):**
  - $x_3 = 1 \ge x_2 = 1$ is True; $y_3 = 1 \ge y_2 = 1$ is True.
  - Intersection is a single point $(1, 1)$ with zero area.
  - Output: **`false`**.

This instance demonstrates hyper-rectangle intersection in Euclidean space and the Separating Hyperplane Theorem for convex polytopes, mathematically proves why factoring orthogonal constraints eliminates geometric boundary case combinatorics, and derives $O(1)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two axis-aligned rectangles:
$$
rec1 = [x_1, y_1, x_2, y_2], \quad rec2 = [x_3, y_3, x_4, y_4]
$$
Return `true` if they overlap with **positive area**, and `false` if they are disjoint or only touch along an edge/corner.

```text
rec1: [0, 0, 2, 2]
rec2: [1, 1, 3, 3]

X-interval overlap: [0, 2] and [1, 3] -> width = 1 > 0
Y-interval overlap: [0, 2] and [1, 3] -> height = 1 > 0
Area = 1 * 1 = 1 > 0

Result: true
```

### The Invariant of the Separating Axes
- Rectangles do NOT overlap if $rec2$ is completely to the right, left, above, or below $rec1$:
  - $x_3 \ge x_2$ (right)
  - $x_4 \le x_1$ (left)
  - $y_3 \ge y_2$ (above)
  - $y_4 \le y_1$ (below)
- Overlap is the logical negation: none of these 4 conditions hold.

---

## 2. Conceptual Foundation & Invariants

### 1. Cartesian Product Intersection:
$$
\text{Area}(R_1 \cap R_2) = \max(0, \min(x_2, x_4) - \max(x_1, x_3)) \times \max(0, \min(y_2, y_4) - \max(y_1, y_3))
$$

### 2. Separating Axis Predicate:
$$
\text{Separated}(R_1, R_2) \iff (x_3 \ge x_2) \lor (x_4 \le x_1) \lor (y_3 \ge y_2) \lor (y_4 \le y_1)
$$
$$
\text{Overlap}(R_1, R_2) \iff \neg \text{Separated}(R_1, R_2)
$$

> **Convex Separation Invariant.** By the Separating Axis Theorem, two disjoint convex sets in $\mathbb{R}^d$ possess a separating hyperplane. For axis-aligned boxes, the outward surface normals align with the standard basis vectors $\{\pm e_x, \pm e_y\}$, reducing existence to four 1D scalar inequalities.

---

## 3. Step-by-Step Worked Execution

We trace $rec1 = [0, 0, 2, 2], rec2 = [1, 1, 3, 3]$:

---

### Step 1: Check Horizontal Separation
- $x_3 \ge x_2 \iff 1 \ge 2$ (False).
- $x_4 \le x_1 \iff 3 \le 0$ (False).

---

### Step 2: Check Vertical Separation
- $y_3 \ge y_2 \iff 1 \ge 2$ (False).
- $y_4 \le y_1 \iff 3 \le 0$ (False).

---

### Step 3: Negate Disjunction
- $\neg(\text{False}) = \mathbf{\text{True}}.$

---

### Step 4: Output
$$
\mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

| Test Case | $rec1$ | $rec2$ | Separation Test True? | Overlap Result |
|:---:|:---:|:---:|:---:|:---:|
| Overlapping Squares | $[0, 0, 2, 2]$ | $[1, 1, 3, 3]$ | None are true | **`true`** |
| Shared Edge | $[0, 0, 1, 1]$ | $[1, 0, 2, 1]$ | $x_3 \ge x_2$ ($1 \ge 1$) | **`false`** |
| Shared Corner | $[0, 0, 1, 1]$ | $[1, 1, 2, 2]$ | $x_3 \ge x_2$ and $y_3 \ge y_2$ | **`false`** |
| Completely Disjoint | $[0, 0, 1, 1]$ | $[2, 2, 3, 3]$ | $x_3 \ge x_2$ ($2 \ge 1$) | **`false`** |

---

## 5. Boundary Cases & Failure Modes

- **Shared Edge ($x_3 = x_2$ or $y_3 = y_2$):** Weak inequality $\ge$ correctly treats edge contact as non-overlapping (area 0).
- **Corner Contact:** Both $x$ and $y$ inequalities meet equality $\implies$ returns `false`.
- **Nested Rectangles ($rec2$ entirely inside $rec1$):** All separation tests false $\implies$ returns `true`.
- **Negative Coordinates ($rec1 = [-2, -2, -1, -1]$):** Cartesian inequalities hold universally across all four quadrants.

---

## 6. Traps & Common Anti-Patterns

- **Using Strict Inequalities ($>$ instead of $\ge$):** If $x_3 > x_2$ is used, an edge-touching rectangle where $x_3 == x_2$ will falsely report `true`! Rectangles that touch only at the edge have area 0 and do not overlap.
- **Checking Only Corner Inclusion:** One rectangle can cross through another without any of its corners lying inside the other (e.g. a tall narrow cross through a wide short rectangle). Checking 1D intervals handles cross configurations correctly.
- **Calculating Area Directly (Potential Overflow):** Multiplying large coordinates can trigger integer overflow; checking 1D interval inequalities uses only simple comparisons without multiplication.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Exactly 4 scalar comparisons and boolean logic: $\mathcal{O}(1)$.
  - Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
