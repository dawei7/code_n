# Guided Example: Erect the Fence

We trace the step-by-step lexicographical coordinate sorting ($(x, y)$), 2D vector cross-product orientation evaluation ($\vec{AB} \times \vec{BC}$), Andrew's monotone chain convex hull construction, collinear boundary point retention ($cross \ge 0$), lower and upper hull stack assembly, and interior tree exclusion on representative point sets:

- **Input:** $trees = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]$
- **Required output:** $[[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]$ (in any order)
  - Geometric objective: Find the convex hull enclosing all given tree coordinates.
  - Special boundary condition: Any tree located **on the fence line** (including points lying directly along straight edges between hull vertices) must be included.
  - Only trees strictly situated in the **interior** of the perimeter (e.g. $[2, 2]$) are excluded.
- **Andrew's Monotone Chain Algorithm & Collinear Orientation:**
  - **The 2D Vector Cross Product:**
    - Given three ordered points $A, B, C$:
      $$
      \vec{AB} = (x_B - x_A, \; y_B - y_A), \quad \vec{BC} = (x_C - x_B, \; y_C - y_B)
      $$
      $$
      \text{cross}(A, B, C) = (x_B - x_A)(y_C - y_B) - (y_B - y_A)(x_C - x_B)
      $$
    - $\text{cross} > 0$: Strict counter-clockwise turn (left turn).
    - $\text{cross} = 0$: Collinear (points lie on the exact same line).
    - $\text{cross} < 0$: Strict clockwise turn (right turn).
  - **Inclusion of Collinear Points:**
    - Standard convex hull algorithms pop points when $\text{cross} \le 0$ to discard flat edges.
    - Here, because perimeter trees must be kept, we only pop when:
      $$
      \text{cross}(stk[-2], stk[-1], i) < 0 \quad (\text{Strict right turn})
      $$
    - Collinear points with $\text{cross} == 0$ are **retained**!
- **Step-by-Step Execution Trace:**
  - **Step 1: Sort Points Lexicographically:**
    - Sort primarily by $x$, secondarily by $y$:
      - Point $0$: $[1, 1]$
      - Point $1$: $[2, 0]$
      - Point $2$: $[2, 2]$
      - Point $3$: $[2, 4]$
      - Point $4$: $[3, 3]$
      - Point $5$: $[4, 2]$
  - **Step 2: Construct Lower Hull (Left to Right):**
    - Start with $stk = [0]$ ($[1, 1]$).
    - **Add Point 1 ($[2, 0]$):**
      - $stk = [0, 1]$.
    - **Add Point 2 ($[2, 2]$):**
      - Check cross product with $A = [1, 1], B = [2, 0], C = [2, 2]$:
        $$
        \vec{AB} = (1, -1), \quad \vec{BC} = (0, 2)
        $$
        $$
        \text{cross} = (1)(2) - (-1)(0) = 2 > 0 \quad (\text{Left turn, valid!})
        $$
      - $stk = [0, 1, 2]$.
    - **Add Point 3 ($[2, 4]$):**
      - Check with $A = [2, 0], B = [2, 2], C = [2, 4]$:
        $$
        \vec{AB} = (0, 2), \quad \vec{BC} = (0, 2) \implies \text{cross} = 0 \quad (\text{Collinear, valid!})
        $$
      - $stk = [0, 1, 2, 3]$.
    - **Add Point 4 ($[3, 3]$):**
      - Check with $A = [2, 2], B = [2, 4], C = [3, 3]$:
        $$
        \vec{AB} = (0, 2), \quad \vec{BC} = (1, -1) \implies \text{cross} = (0)(-1) - (2)(1) = -2 < 0
        $$
        - Strict right turn! Pop Point $3$ ($[2, 4]$).
      - Check with $A = [2, 0], B = [2, 2], C = [3, 3]$:
        $$
        \vec{AB} = (0, 2), \quad \vec{BC} = (1, 1) \implies \text{cross} = -2 < 0
        $$
        - Right turn! Pop Point $2$ ($[2, 2]$).
      - Check with $A = [1, 1], B = [2, 0], C = [3, 3]$:
        $$
        \vec{AB} = (1, -1), \quad \vec{BC} = (1, 3) \implies \text{cross} = (1)(3) - (-1)(1) = 4 > 0
        $$
        - Left turn! Stop popping.
      - Push Point 4: $stk = [0, 1, 4]$.
    - **Add Point 5 ($[4, 2]$):**
      - Check with $A = [2, 0], B = [3, 3], C = [4, 2]$:
        $$
        \vec{AB} = (1, 3), \quad \vec{BC} = (1, -1) \implies \text{cross} = (1)(-1) - (3)(1) = -4 < 0
        $$
        - Right turn! Pop Point 4 ($[3, 3]$).
      - Check with $A = [1, 1], B = [2, 0], C = [4, 2]$:
        $$
        \vec{AB} = (1, -1), \quad \vec{BC} = (2, 2) \implies \text{cross} = (1)(2) - (-1)(2) = 4 > 0
        $$
        - Left turn! Push Point 5.
    - Final Lower Hull: $stk = [0, 1, 5] \to [[1, 1], [2, 0], [4, 2]]$.
  - **Step 3: Construct Upper Hull (Right to Left):**
    - Starting size $m = 3$.
    - Iterate backwards through points $4, 3, 2, 1, 0$:
      - **Point 4 ($[3, 3]$):**
        - Cross with $B = [4, 2], A = [2, 0]$: Left turn $\implies$ push Point 4.
        - $stk = [0, 1, 5, 4]$.
      - **Point 3 ($[2, 4]$):**
        - Cross with $B = [3, 3], A = [4, 2]$:
          $$
          \vec{AB} = (-1, 1), \quad \vec{BC} = (-1, 1) \implies \text{cross} = 0 \quad (\text{Collinear, keep!})
          $$
        - $stk = [0, 1, 5, 4, 3]$.
      - **Point 2 ($[2, 2]$):**
        - Interior point; strictly inside upper boundary $\implies$ popped or skipped.
      - **Point 0 ($[1, 1]$):**
        - Completes the loop back to the start.
  - **Step 4: Hull Assembly and Interior Exclusion:**
    - Nodes surviving in stack:
      - Point 0: $[1, 1]$
      - Point 1: $[2, 0]$
      - Point 5: $[4, 2]$
      - Point 4: $[3, 3]$
      - Point 3: $[2, 4]$
    - Notice that Point 2 ($[2, 2]$) was rejected from both lower and upper hulls, correctly identifying it as an **interior tree**.
    - Resulting perimeter fence:
      $$
      [[1, 1], \; [2, 0], \; [4, 2], \; [3, 3], \; [2, 4]]
      $$
- **Collinear Flat Line Instance ($[[1, 1], [2, 2], [3, 3]]$):**
  - $n < 4$ or all points collinear $\implies$ all points lie on the fence $\implies$ return all input points.

This instance demonstrates computational geometry convex hull construction via monotone chains, mathematically proves why relaxing cross-product tests from strict positive to non-negative preserves collinear perimeter elements, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given coordinates of trees in a 2D plane:
Find all trees that lie on the **perimeter of the fence** (the convex hull).
Trees lying along straight fence segments between corners **must be included**.
Return the perimeter trees in any order.

```text
Trees:
      [2, 4] -- [3, 3]
     /                \
  [1, 1]     [2, 2]    [4, 2]
     \       (interior)  /
      \                 /
        --- [2, 0] ---

Perimeter Trees: [1, 1], [2, 0], [4, 2], [3, 3], [2, 4]
Interior Tree: [2, 2] is enclosed and excluded.
```

### The Difference in Collinear Handling
- In standard convex hull problems, points lying on a straight line between two vertices are discarded as redundant.
- Here, trees on the fence are physical obstacles that must be enclosed, so **collinear perimeter trees must be preserved**.
- In Andrew's Monotone Chain:
  - We pop point $B$ only if making a **strict right turn**:
    $$
    \text{cross}(A, B, C) < 0
    $$
  - If $\text{cross}(A, B, C) == 0$, the points are collinear, so $B$ is **kept** on the stack.

---

## 2. Conceptual Foundation & Invariants

### 1. Vector Cross Product:
$$
\text{cross}(A, B, C) = (x_B - x_A)(y_C - y_B) - (y_B - y_A)(x_C - x_B)
$$
- Positive: Counter-clockwise turn.
- Zero: Collinear.
- Negative: Clockwise turn (violates convexity).

### 2. Andrew's Algorithm:
1. Sort points by $x$ ascending, then $y$ ascending.
2. Build lower hull from left to right, maintaining monotonic counter-clockwise/collinear turns.
3. Build upper hull from right to left.
4. Concatenate both hulls and deduplicate endpoints.

> **Convexity Invariant.** At every step of the monotone chain, the sequence of edges forms a convex polygonal chain with non-negative cross products, ensuring no exterior point is excluded.

---

## 3. Step-by-Step Worked Execution

We trace the 6 points:

---

### Step 1: Lexicographical Sort
Sorted coordinates:
`[1, 1], [2, 0], [2, 2], [2, 4], [3, 3], [4, 2]`

---

### Step 2: Build Lower Hull
- Add $[1, 1], [2, 0]$.
- Processing $[2, 2], [2, 4], [3, 3]$: right turns pop interior nodes $[2, 2]$.
- Arriving at $[4, 2]$:
  Lower hull stack locks in:
  $$
  [[1, 1], \; [2, 0], \; [4, 2]]
  $$

---

### Step 3: Build Upper Hull
- Backward scan checks points from right to left.
- Adds $[3, 3]$ and $[2, 4]$ (collinear on upper boundary).
- Skips visited $[2, 0]$ and rejects interior $[2, 2]$.
- Connects back to $[1, 1]$.

---

### Step 4: Collect Vertices
All perimeter trees:
$$
[[1, 1], \; [2, 0], \; [4, 2], \; [3, 3], \; [2, 4]]
$$

---

## 4. Complete Execution Trace

| Point | $(x, y)$ | Lower Hull Action | Upper Hull Action | On Final Fence? |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | $[1, 1]$ | Added to base | Closes loop | **Yes (Corner)** |
| $1$ | $[2, 0]$ | Kept in lower hull | Skipped (visited) | **Yes (Bottom)** |
| $2$ | $[2, 2]$ | Popped (right turn) | Popped (interior) | **No (Interior)** |
| $3$ | $[2, 4]$ | Popped in lower | Kept in upper | **Yes (Top)** |
| $4$ | $[3, 3]$ | Popped in lower | Kept in upper | **Yes (Edge)** |
| $5$ | $[4, 2]$ | Kept in lower hull | Start of upper | **Yes (Right)** |

---

## 5. Boundary Cases & Failure Modes

- **Fewer than 4 Trees ($N < 4$):** All trees are automatically on the fence $\implies$ return input directly.
- **All Trees on a Single Line ($x_1 = x_2 = \dots$):** All cross products are 0 $\implies$ returns all trees along the line.
- **All Trees Form a Convex Polygon:** All points retained in either lower or upper hull.
- **Identical Coordinates:** Deduplicated during monotone construction.

---

## 6. Traps & Common Anti-Patterns

- **Popping on `cross <= 0`:** Using `<=` instead of `<` pops collinear points, discarding trees that sit legitimately on straight fence segments.
- **Forgetting Backward Pass (`Upper Hull`):** A single scan only constructs the lower envelope; the reverse pass is required to seal the top boundary.
- **Floating-Point Coordinates:** Cross product uses pure integer multiplication, completely avoiding floating-point precision issues or rounding errors.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Lexicographical sorting: $\mathcal{O}(N \log N)$ time.
  - Each point is pushed and popped at most twice across lower and upper hull passes: $\mathcal{O}(N)$ operations.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 3000$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the stack and visited array.
