# Guided Example: Largest Triangle Area

We trace the step-by-step 2D Cartesian triangle area derivation via the exterior vector cross product (Shoelace formula $\frac{1}{2} |\vec{u} \times \vec{v}|$), triplet combination search ($\binom{N}{3}$ configurations), collinear degenerate triangle rejection ($\text{Area} = 0$), running maximum area convergence ($\max(ans, t)$), and global maximum area extraction on representative point clouds:

- **Input:**
  $$
  points = [[0, 0], \; [0, 1], \; [1, 0], \; [0, 2], \; [2, 0]]
  $$
- **Required output:** `2.0`
  - Geometric triangle specifications:
    - You are given $N$ points in the 2D Euclidean plane $\mathbb{R}^2$.
    - Any three distinct points $P_1 = (x_1, y_1)$, $P_2 = (x_2, y_2)$, and $P_3 = (x_3, y_3)$ form a triangle.
    - Objective: Find the **maximum area** of any triangle formed by three chosen points.
    - For the input set:
      - Consider points $(0, 0)$, $(0, 2)$, and $(2, 0)$:
        - Base along the x-axis: from $(0, 0)$ to $(2, 0)$, length $b = 2$.
        - Height along the y-axis: from $(0, 0)$ to $(0, 2)$, height $h = 2$.
        - Right-triangle area:
          $$
          \text{Area} = \frac{1}{2} \times 2 \times 2 = \mathbf{2.0}
          $$
      - No other triplet of points yields a larger area.
      - Maximum area: **`2.0`**.
- **Vector Cross Product & Shoelace Invariant:**
  - **The 2D Exterior Product Formula:**
    - Shift the coordinate origin to $P_1(x_1, y_1)$.
    - Construct the two displacement vectors:
      $$
      \vec{u} = P_2 - P_1 = (x_2 - x_1, \; y_2 - y_1)
      $$
      $$
      \vec{v} = P_3 - P_1 = (x_3 - x_1, \; y_3 - y_1)
      $$
    - The signed area of the parallelogram spanned by $\vec{u}$ and $\vec{v}$ is the determinant:
      $$
      \det(\vec{u}, \vec{v}) = u_x v_y - u_y v_x = (x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1)
      $$
    - The triangle area is exactly half the absolute value of the determinant:
      $$
      \text{Area}(P_1, P_2, P_3) = \frac{1}{2} |(x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1)|
      $$
  - **Exhaustive Triplet Bound ($N \le 50$):**
    - The total number of triplets from $N \le 50$ points is:
      $$
      \binom{N}{3} = \frac{N(N - 1)(N - 2)}{6} \le \frac{50 \times 49 \times 48}{6} = 19,600
      $$
    - Evaluating $19,600$ determinants takes fewer than $10^5$ operations, completing in $< 5$ ms.
- **Step-by-Step Worked Execution Trace on the 5-Point Cloud:**
  - Points:
    - $P_0 = (0, 0)$
    - $P_1 = (0, 1)$
    - $P_2 = (1, 0)$
    - $P_3 = (0, 2)$
    - $P_4 = (2, 0)$
  - Initialize maximum area: $ans = 0$.
  - **Evaluation of Selected Triplets:**
    - **Triplet $(P_0, P_1, P_2) \to (0, 0), (0, 1), (1, 0)$:**
      - $\vec{u} = (0 - 0, 1 - 0) = (0, 1)$
      - $\vec{v} = (1 - 0, 0 - 0) = (1, 0)$
      - Cross product: $|0(0) - 1(1)| = |-1| = 1$.
      - Area: $1 / 2 = \mathbf{0.5}$.
      - Update: $ans \leftarrow \max(0, 0.5) = \mathbf{0.5}$.
    - **Triplet $(P_0, P_1, P_3) \to (0, 0), (0, 1), (0, 2)$:**
      - All three points lie on the y-axis ($x = 0$) $\implies \mathbf{Collinear!}$
      - $\vec{u} = (0, 1), \vec{v} = (0, 2)$.
      - Cross product: $|0(2) - 1(0)| = 0$.
      - Area: $\mathbf{0.0}$.
    - **Triplet $(P_0, P_3, P_2) \to (0, 0), (0, 2), (1, 0)$:**
      - $\vec{u} = (0, 2), \vec{v} = (1, 0)$.
      - Cross product: $|0(0) - 2(1)| = |-2| = 2$.
      - Area: $2 / 2 = \mathbf{1.0}$.
      - Update: $ans \leftarrow \max(0.5, 1.0) = \mathbf{1.0}$.
    - **Triplet $(P_0, P_3, P_4) \to (0, 0), (0, 2), (2, 0)$:**
      - $\vec{u} = (0, 2), \vec{v} = (2, 0)$.
      - Cross product:
        $$
        |u_x v_y - u_y v_x| = |(0)(0) - (2)(2)| = |-4| = \mathbf{4}
        $$
      - Area:
        $$
        t = \frac{4}{2} = \mathbf{2.0}
        $$
      - Update: $ans \leftarrow \max(1.0, 2.0) = \mathbf{2.0}$.
    - **Triplet $(P_1, P_2, P_3) \to (0, 1), (1, 0), (0, 2)$:**
      - Area: $0.5$.
    - **Triplet $(P_3, P_2, P_4) \to (0, 2), (1, 0), (2, 0)$:**
      - Base on x-axis from $1$ to $2$ (length 1), height 2 $\implies$ Area: $1.0$.
  - After evaluating all $\binom{5}{3} = 10$ triplets:
    $$
    ans = \mathbf{2.0}
    $$
- **Collinear Points Trace ($points = [[0, 0], [1, 1], [2, 2]]$):**
  - All three points lie on line $y = x$.
  - Determinant is $0 \implies$ Area is $0.0$.
- **Unit Square Points Trace ($points = [[0, 0], [0, 1], [1, 0], [1, 1]]$):**
  - Any 3 points form half the square $\implies$ Area is $0.5$.

This instance demonstrates wedge product symplectic area calculation on discrete affine varieties and combinatorial extreme value search, mathematically proves why the shoelace determinant compute signed Lebesgue measure in constant time per triplet, and derives $O(N^3)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given points in the 2D plane:
Find the **maximum area** of a triangle formed by any three points.

```text
points = [ (0, 0), (0, 1), (1, 0), (0, 2), (2, 0) ]

Take points (0, 0), (0, 2), and (2, 0):
  Base on x-axis = 2
  Height on y-axis = 2
  Area = 0.5 * 2 * 2 = 2.0

Result: 2.0
```

### The Invariant of the 2D Cross Product Area
- Triangle area for $(x_1, y_1), (x_2, y_2), (x_3, y_3)$:
  $$
  \text{Area} = \frac{1}{2} |(x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1)|
  $$
- Collinear points automatically yield area 0.
- With $N \le 50$, $\binom{50}{3} = 19,600$ triplets; checking all triplets runs in $< 5$ ms.

---

## 2. Conceptual Foundation & Invariants

### 1. Exterior Product Determinant:
$$
\vec{u} = P_2 - P_1, \quad \vec{v} = P_3 - P_1
$$
$$
\text{Area}(P_1, P_2, P_3) = \frac{1}{2} |u_x v_y - u_y v_x|
$$

### 2. Triplet Extremum Search:
$$
ans = \max_{\{P_1, P_2, P_3\} \subseteq points} \text{Area}(P_1, P_2, P_3)
$$

> **Convex Hull Extremum Invariant.** The maximum area triangle of any planar point set $S$ has all three vertices on the convex hull $\text{CH}(S)$. While a rotating caliper approach yields $O(N^2)$, the small constraint $N \le 50$ makes $O(N^3)$ brute force unconditionally optimal and branch-free.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Triplet $( (0, 0), (0, 1), (1, 0) )$
- $\vec{u} = (0, 1), \vec{v} = (1, 0) \implies \frac{1}{2} |0 - 1| = 0.5$.

---

### Step 2: Triplet $( (0, 0), (0, 1), (0, 2) )$
- Collinear along y-axis $\implies \text{Area} = 0.0$.

---

### Step 3: Triplet $( (0, 0), (0, 2), (1, 0) )$
- $\vec{u} = (0, 2), \vec{v} = (1, 0) \implies \frac{1}{2} |0 - 2| = 1.0$.

---

### Step 4: Triplet $( (0, 0), (0, 2), (2, 0) )$
- $\vec{u} = (0, 2), \vec{v} = (2, 0) \implies \frac{1}{2} |0 - 4| = \mathbf{2.0}$.

---

### Step 5: Output
- Global maximum area: **`2.0`**.

---

## 4. Complete Execution Trace

| Point $P_1$ | Point $P_2$ | Point $P_3$ | Displacement $\vec{u}, \vec{v}$ | Determinant $\lvert u_x v_y - u_y v_x \rvert$ | Triangle Area | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | $(0, 1)$ | $(1, 0)$ | $(0, 1), (1, 0)$ | $1$ | $0.5$ | $0.5$ |
| $(0, 0)$ | $(0, 1)$ | $(0, 2)$ | $(0, 1), (0, 2)$ | $0$ | $0.0$ | $0.5$ |
| $(0, 0)$ | $(0, 2)$ | $(1, 0)$ | $(0, 2), (1, 0)$ | $2$ | $1.0$ | $1.0$ |
| **$(0, 0)$** | **$(0, 2)$** | **$(2, 0)$** | **$(0, 2), (2, 0)$** | **$4$** | **$2.0$** | **`2.0`** |

---

## 5. Boundary Cases & Failure Modes

- **All Points Collinear:** Every determinant is 0 $\implies ans = 0.0$.
- **Only 3 Points ($N = 3$):** Exactly 1 triangle $\implies$ computes area of that triangle.
- **Negative Coordinates:** Displacement vectors $x_2 - x_1$ handle negative coordinates with identical algebra.
- **Floating Point Precision:** Division by 2 at the end preserves exact precision.

---

## 6. Traps & Common Anti-Patterns

- **Heron's Formula with Square Roots:** Using $s = (a+b+c)/2$ with $\sqrt{s(s-a)(s-b)(s-c)}$ introduces floating-point square root overhead and catastrophic numerical cancellation on thin triangles. The cross product Shoelace formula is exact and uses integer arithmetic until the final division by 2.
- **Forgetting Absolute Value:** Vector cross product is signed (positive or negative depending on orientation); always wrap in `abs(...)`.
- **Selecting Duplicate Points:** Points in the triplet must be distinct; choose $i < j < k$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Triplet combinations: $\binom{N}{3} = \frac{N(N-1)(N-2)}{6} = \mathcal{O}(N^3)$.
  - Constant-time arithmetic per triplet: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(N^3)$ where $N \le 50 \implies \le 19,600$ iterations. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
