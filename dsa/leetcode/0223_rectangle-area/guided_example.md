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

The failure is not a matter of degree: it happens for exactly one sign pattern of the two raw gaps. The table walks every pattern, using the package's own cases where one supplies the geometry.

| Raw gaps $(\Delta x, \Delta y)$ before clamping | Geometry used | Clamped overlap | $\max\big(0, \Delta x \cdot \Delta y\big)$ | Verdict |
|:---|:---|:---:|:---:|:---|
| $(+, +) = (3, 2)$ | The main instance: A $(-3,0)$–$(3,4)$ against B $(0,-1)$–$(9,2)$ | $3 \times 2 = 6$ | 6 | The two rules agree, and this is the only pattern in which a genuine overlap exists |
| $(0, +) = (0, 2)$ | Package case `trial-touching`: A $(-2,-2)$–$(0,1)$ against B $(0,-1)$–$(3,2)$ | $0 \times 2 = 0$ | $\max(0, 0) = 0$ | Agree: one zero gap already destroys the area, and the unclamped product follows only because one factor is zero |
| $(+, 0) = (1, 0)$ | A $(0,0)$–$(2,2)$ against B $(1,2)$–$(3,4)$ (constructed) | $1 \times 0 = 0$ | 0 | Agree by the mirrored argument: the shared horizontal line carries no area |
| $(0, 0)$ | A $(0,0)$–$(1,1)$ against B $(1,1)$–$(2,2)$ (constructed) | $0 \times 0 = 0$ | 0 | Agree: a single shared corner point has zero 2D measure |
| $(-, +) = (-2, 2)$ | A $(0,0)$–$(1,2)$ against B $(3,0)$–$(4,2)$ (constructed) | $0 \times 2 = 0$ | $\max(0, -4) = 0$ | Agree, but by luck: the product is negative, so the clamp is not the safeguard here |
| $(+, -) = (2, -1)$ | A $(0,0)$–$(2,1)$ against B $(0,2)$–$(2,3)$ (constructed) | $2 \times 0 = 0$ | $\max(0, -2) = 0$ | Agree by the mirrored argument |
| $(-, -) = (-1, -1)$ | The phantom pair of this section: A $[0,1]$ against B $[2,3]$ on both axes | $0 \times 0 = 0$ | $\max(0, +1) = 1$ | **Disagree.** Only when *both* gaps are negative does the product turn positive, so per-axis clamping is the single change that removes the fabricated overlap |

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

**Every shape the two-rectangle input can take.** Each row below is a full evaluation of the closed form, so the union can be read off directly. The first five rows are the package's own cases; the contained row is a constructed extreme.

| Case | Rectangles, as $[x_1, y_1]$–$[x_2, y_2]$ | Raw gaps $(\Delta x, \Delta y)$ | $\text{overlap}_x \times \text{overlap}_y$ | Union | What the row demonstrates |
|:---|:---|:---:|:---:|:---:|:---|
| Sample: partial overlap | A $(-3,0)$–$(3,4)$, B $(0,-1)$–$(9,2)$ | $(3, 2)$ | $3 \times 2 = 6$ | $24 + 27 - 6 = 45$ | Both projections overlap, and the subtracted term is genuinely needed |
| Sample: identical squares | A $(-2,-2)$–$(2,2)$, B $(-2,-2)$–$(2,2)$ | $(4, 4)$ | $4 \times 4 = 16$ | $16 + 16 - 16 = 16$ | Full containment in both axes: the overlap equals one whole rectangle, so the union is one rectangle |
| Trial: identical small squares | A $(0,0)$–$(2,2)$, B $(0,0)$–$(2,2)$ | $(2, 2)$ | $2 \times 2 = 4$ | $4 + 4 - 4 = 4$ | The same identity at a smaller scale, and the smallest input whose overlap is non-zero |
| Trial: diagonal separation | A $(0,0)$–$(1,1)$, B $(2,2)$–$(4,4)$ | $(-1, -1)$ | $0 \times 0 = 0$ | $1 + 4 = 5$ | The phantom-overlap pattern: the rectangles are disjoint in both axes and yet the unclamped product would be $+1$ |
| Trial: touching along a vertical edge | A $(-2,-2)$–$(0,1)$, B $(0,-1)$–$(3,2)$ | $(0, 2)$ | $0 \times 2 = 0$ | $6 + 9 = 15$ | $x = 0$ is shared as a boundary, which is a line of zero area even though the vertical projections genuinely overlap |
| Contained (constructed) | A $(0,0)$–$(4,4)$, B $(1,1)$–$(2,2)$ | $(1, 1)$ | $1 \times 1 = 1$ | $16 + 1 - 1 = 16$ | The union collapses to the outer rectangle whenever one rectangle contains the other; any answer other than 16 means the subtraction term was mis-signed |

---

## 6. Traps This Instance Exposes

- **Unclamped Negative Dimension Multiplication:** Multiplying $\Delta x \times \Delta y$ before applying $\max(0, \dots)$ causes two negative gaps to produce a positive number, hallucinating false overlap for disjoint diagonal rectangles.
- **Integer Overflow in Fixed-Width Languages:** In languages like C++ / Java, each side can be as long as $2 \times 10^4$ (from $-10^4$ to $10^4$), so a single rectangle's area reaches $4 \times 10^8$ and the sum before subtraction reaches $8 \times 10^8$; both still fit in a 32-bit signed integer, whose limit is $2.1 \times 10^9$. If coordinates were up to $10^9$, the intermediate $a + b$ could reach $8 \times 10^{18}$ and 64-bit integers (`long long`) would be required.
- **Touching Edges vs Overlap:** If rectangles touch at an edge (e.g. $ax_2 = bx_1$), $\min(ax_2, bx_2) - \max(ax_1, bx_1) = 0$. $\text{overlap}_x = 0$, yielding $\text{Area}_{\text{overlap}} = 0$, which correctly reflects that line boundaries have zero 2D Lebesgue measure.

**Alternative formulations, and the scale each one suits.** The closed form is exact only because there are exactly two rectangles; the methods below trade that for generality.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or when it is the right choice |
|:---|:---|:---:|:---:|:---|
| Per-axis clamp plus inclusion–exclusion (this lesson) | Multiply each rectangle's own width by its height, then subtract $\max(0, \min - \max)$ applied separately on each axis | $O(1)$ | $O(1)$ | Optimal for two rectangles and impossible to beat; it cannot be extended to a third rectangle without subtracting the pairwise overlaps and adding back the triple overlap |
| Unit-cell marking over the coordinate range | Mark every covered integer cell in a grid and count the marked cells | $O(\text{range}^2)$ | $O(\text{range}^2)$ | At the stated limit the grid spans $2 \times 10^4$ in each direction, so the marking array alone would hold about $4 \times 10^8$ entries; it also answers a different question, namely the number of integer cells rather than the covered area |
| Coordinate compression with a difference array | Collect the distinct $x$ and $y$ boundaries and test each elementary cell for membership in either rectangle | $O(K^2)$ for $K$ distinct coordinates | $O(K^2)$ | With two rectangles there are only $9$ elementary cells, so it works, but the cell count grows quadratically and the method becomes impractical as rectangles are added |
| Sweep line over $x$ with an active $y$-interval union | Sort the $2N$ vertical edges, maintain the total length of the union of active $y$-intervals, and accumulate that length times each $dx$ | $O(N \log N)$ | $O(N)$ | This is the general answer for $N$ rectangles and the natural reply to the follow-up question; for two rectangles it is far more machinery than the closed form needs, and the interval union must merge touching intervals so that shared edges are not double-counted |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. The work is a fixed number of scalar operations regardless of the coordinates: 4 subtractions for the two rectangles' own dimensions, 4 comparisons to form the intersection bounds, 2 further subtractions and 2 further comparisons for the per-axis clamps, 3 multiplications, and 2 additions. No step depends on the magnitude of the coordinates.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory.
