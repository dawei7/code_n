# Guided Example: Valid Square

We trace the step-by-step pairwise Euclidean distance calculation ($\binom{4}{2} = 6$ distance segments), distance multiset frequency analysis (4 equal sides of length $s > 0$, 2 equal diagonals of length $2s$), isosceles right triangle verification via the Pythagorean theorem ($d_1 + d_2 = d_3$), degeneracy and zero-area non-collision checks, and order-invariant geometric validation on representative point quadrilaterals:

- **Input:**
  $$
  p_1 = [0, 0], \quad p_2 = [1, 1], \quad p_3 = [1, 0], \quad p_4 = [0, 1]
  $$
- **Required output:** `true`
  - Geometric definition: A square is a 4-sided polygon with:
    1. Four equal-length sides ($s > 0$).
    2. Four internal right angles ($90^\circ$).
    3. Two equal-length diagonals ($d = \sqrt{2} \cdot s$).
    4. Non-zero area (the four vertices must be distinct).
  - Note: The four input points may be provided in **any arbitrary permutation**.
- **Pairwise Distance Multiset Principle:**
  - Among 4 distinct points, there are exactly:
    $$
    \binom{4}{2} = \frac{4 \times 3}{2} = 6 \text{ pairwise distance segments}
    $$
  - Let $D(a, b) = (x_a - x_b)^2 + (y_a - y_b)^2$ denote the squared Euclidean distance.
  - In a planar square with side length squared $S > 0$:
    - The 4 sides have squared distance equal to $S$.
    - The 2 diagonals have squared distance equal to $2S$ (by the Pythagorean theorem: $S + S = 2S$).
  - Therefore, the multiset of all 6 squared distances must contain:
    - Exactly **two distinct values**: $\{S, 2S\}$.
    - Value $S$ with multiplicity **$4$**.
    - Value $2S$ with multiplicity **$2$**.
    - And $S > 0$ (preventing collapsed points).
- **Triangular Verification Method ($check(a, b, c)$):**
  - Any 3 vertices chosen from a square must form an **isosceles right triangle**!
  - For any triplet $(a, b, c)$ with pairwise squared distances $d_1, d_2, d_3$:
    $$
    (d_1 == d_2 \land d_1 + d_2 == d_3 \land d_1 > 0) \lor \text{permutations}
    $$
  - There are $\binom{4}{3} = 4$ such triplets. If all 4 triplets satisfy this condition, the shape is guaranteed to be a valid square!
- **Step-by-Step Execution Trace:**
  - Given points:
    - $p_1 = (0, 0)$
    - $p_2 = (1, 1)$
    - $p_3 = (1, 0)$
    - $p_4 = (0, 1)$
  - **Step 1: Compute All 6 Squared Distances:**
    - Segment $(p_1, p_2)$: $(1 - 0)^2 + (1 - 0)^2 = 1 + 1 = \mathbf{2}$ (Diagonal)
    - Segment $(p_1, p_3)$: $(1 - 0)^2 + (0 - 0)^2 = 1 + 0 = \mathbf{1}$ (Side)
    - Segment $(p_1, p_4)$: $(0 - 0)^2 + (1 - 0)^2 = 0 + 1 = \mathbf{1}$ (Side)
    - Segment $(p_2, p_3)$: $(1 - 1)^2 + (0 - 1)^2 = 0 + 1 = \mathbf{1}$ (Side)
    - Segment $(p_2, p_4)$: $(0 - 1)^2 + (1 - 1)^2 = 1 + 0 = \mathbf{1}$ (Side)
    - Segment $(p_3, p_4)$: $(0 - 1)^2 + (1 - 0)^2 = 1 + 1 = \mathbf{2}$ (Diagonal)
  - **Step 2: Inspect the Distance Multiset:**
    $$
    \text{Distances} = [1, \; 1, \; 1, \; 1, \; 2, \; 2]
    $$
    - Frequency of $1$: appears **4 times**.
    - Frequency of $2$: appears **2 times**.
    - Relation check:
      $$
      2 = 1 + 1 = 2 \times 1 \implies \mathbf{True}
      $$
    - Non-zero side check:
      $$
      1 > 0 \implies \mathbf{True}
      $$
  - **Step 3: Triplet Verification:**
    - Triplet $(p_1, p_2, p_3)$: sides are $1, 1, 2 \implies 1^2 + 1^2 = 2 \implies$ Isosceles right triangle.
    - Triplet $(p_2, p_3, p_4)$: sides are $1, 1, 2 \implies 1^2 + 1^2 = 2 \implies$ Isosceles right triangle.
    - Triplet $(p_1, p_3, p_4)$: sides are $1, 1, 2 \implies 1^2 + 1^2 = 2 \implies$ Isosceles right triangle.
    - Triplet $(p_1, p_2, p_4)$: sides are $1, 1, 2 \implies 1^2 + 1^2 = 2 \implies$ Isosceles right triangle.
  - All 4 triplet checks evaluate to `True`!
  - Final Result: **`true`**.
- **Non-Square Rectangle Instance ($p_1 = [0, 0], p_2 = [2, 1], p_3 = [2, 0], p_4 = [0, 1]$):**
  - Distances are: sides of length $1$ and $4$, diagonals of length $5$.
  - Three distinct distance values appear $\{1, 4, 5\}$ $\implies$ Fails side-equality $\implies \mathbf{false}$.
- **Degenerate Collapsed Points ($p_1 = p_2 = p_3 = p_4 = [0, 0]$):**
  - All distances are $0$.
  - Fails $S > 0 \implies \mathbf{false}$.
- **Rhombus (Non-Square):**
  - 4 equal sides, but diagonals have different lengths $\implies 3$ distinct distance values $\implies \mathbf{false}$.

This instance demonstrates invariant geometric classification via distance spectrum analysis, mathematically proves why a 6-distance spectrum of $\{S: 4, 2S: 2\}$ uniquely identifies planar squares without angular calculation, and derives $O(1)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given coordinates of 4 points $p_1, p_2, p_3, p_4$ in arbitrary order:
Determine whether they form the vertices of a **valid square**.

```text
Points:
  p4 (0, 1) --------- p2 (1, 1)
      |                   |
      |   Side = 1        |
      |   Diagonal = √2   |
      |                   |
  p1 (0, 0) --------- p3 (1, 0)

6 pairwise distances:
  4 sides with length^2 = 1
  2 diagonals with length^2 = 2

Result: true
```

### The Power of Metric Spectrum Analysis
- Trying to order the points clockwise or calculate slope tangents is prone to division-by-zero errors (vertical lines) and coordinate ordering edge cases.
- In contrast, the **distance spectrum** (the set of all 6 pairwise squared Euclidean distances) is completely invariant to:
  - Point ordering (permutations).
  - Translation.
  - Rotation at any angle in the 2D plane.

---

## 2. Conceptual Foundation & Invariants

### 1. Distance Metric (Squared Euclidean):
$$
D(a, b) = (x_a - x_b)^2 + (y_a - y_b)^2
$$
Using squared distances avoids floating-point square roots and retains exact integer precision.

### 2. The Square Invariant:
A set of 4 points forms a non-degenerate square if and only if:
1. Exactly 2 distinct distance values exist: $\{S, D\}$.
2. $S > 0$ and $D > 0$ (all points distinct).
3. The frequency of $S$ is 4 (the four sides).
4. The frequency of $D$ is 2 (the two diagonals).
5. The Pythagorean relationship holds: $D = 2S$.

> **Orthogonal Spectrum Invariant.** A planar quadrangle is a square if and only if its 6-edge metric graph decomposes into $K_4$ with 4 edges of weight $S$ and 2 antipodal edges of weight $2S > 0$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute All 6 Squared Distances
- $D(p_1, p_2) = (1-0)^2 + (1-0)^2 = 2$
- $D(p_1, p_3) = (1-0)^2 + (0-0)^2 = 1$
- $D(p_1, p_4) = (0-0)^2 + (1-0)^2 = 1$
- $D(p_2, p_3) = (1-1)^2 + (0-1)^2 = 1$
- $D(p_2, p_4) = (0-1)^2 + (1-1)^2 = 1$
- $D(p_3, p_4) = (0-1)^2 + (1-0)^2 = 2$

---

### Step 2: Tally Frequencies
- Value $1$: count = 4
- Value $2$: count = 2

---

### Step 3: Check Geometric Constraints
- Distinct values count: $2$.
- Ratio: $2 = 2 \times 1 \implies D = 2S$.
- Positivity: $S = 1 > 0$.
- All criteria satisfied $\implies$ **`True`**.

---

## 4. Complete Execution Trace

| Point Pair | Coordinate Delta $(\Delta x, \Delta y)$ | Squared Distance $\Delta x^2 + \Delta y^2$ | Structural Role |
|:---:|:---:|:---:|:---:|
| $(p_1, p_3)$ | $(1, 0)$ | $1$ | Bottom Edge |
| $(p_1, p_4)$ | $(0, 1)$ | $1$ | Left Edge |
| $(p_2, p_3)$ | $(0, -1)$ | $1$ | Right Edge |
| $(p_2, p_4)$ | $(-1, 0)$ | $1$ | Top Edge |
| $(p_1, p_2)$ | $(1, 1)$ | $2$ | Main Diagonal |
| $(p_3, p_4)$ | $(-1, 1)$ | $2$ | Anti-Diagonal |
| **Conclusion** | **4 sides of $1$, 2 diagonals of $2$** | **$2 = 1 + 1$** | **Valid Square (`True`)** |

---

## 5. Boundary Cases & Failure Modes

- **All Points Overlapping ($[0,0], [0,0], [0,0], [0,0]$):** $S = 0 \implies \mathbf{false}$.
- **Rhombus with Non-Right Angles:** Diagonals have different lengths ($d_1 \ne d_2$) $\implies$ yields 3 distinct distances $\implies \mathbf{false}$.
- **Collinear Points ($[0,0], [0,1], [0,2], [0,3]$):** Distances include $1, 4, 9 \implies \mathbf{false}$.
- **Rotated / Tilted Squares:** Points at $[1, 2], [2, 4], [4, 3], [3, 1]$ evaluate identically without coordinate alignment.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Points are Given in Clockwise Order:** Input points arrive in completely random permutations. Checking adjacent array elements directly ($p_1 \to p_2 \to p_3 \to p_4$) fails when vertices cross diagonally.
- **Using Floating-Point Division for Slopes:** Dividing by $\Delta x$ triggers ZeroDivisionError on vertical edges, and floating-point comparison fails due to numerical imprecision.
- **Checking Only That 4 Sides Are Equal:** A rhombus has 4 equal sides but is not a square. Checking that diagonals are equal and satisfy $D = 2S$ is mandatory.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Exactly 6 pairwise distance computations: $\mathcal{O}(1)$ operations.
  - Sorting or grouping the 6 numbers: $\mathcal{O}(1)$ time.
  - Total Time: strictly constant $\mathcal{O}(1)$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space for storing the 6 distance values.
