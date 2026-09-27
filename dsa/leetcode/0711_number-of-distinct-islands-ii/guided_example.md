# Guided Example: Number of Distinct Islands II

We trace the step-by-step connected component exploration over binary grids, dihedral group $D_4$ geometric isometry actions (8 rigid symmetries: 4 rotations $\times$ 2 reflections), translation normalization to origin $(0, 0)$, lexicographical canonical form selection ($\min \text{orbit}$), hash set deduplication, and invariant island count evaluation on representative symmetric grids:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 1 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 1 & 1
  \end{bmatrix}
  $$
- **Required output:** `1`
  - Problem objective:
    - Identify all connected components of land (`1`s connected 4-directionally).
    - In this problem (unlike Distinct Islands I), two islands are considered **identical** if one can be transformed into the other via any combination of:
      - **Translation** (shifting in 2D space)
      - **Rotation** ($90^\circ, 180^\circ, 270^\circ$)
      - **Reflection** (horizontal, vertical, diagonal)
    - For the input grid:
      - Island 1 (top-left): cells $(0, 0), (0, 1), (1, 0)$ forming an L-tromino.
      - Island 2 (bottom-right): cells $(2, 4), (3, 3), (3, 4)$ forming an inverted L-tromino.
      - Rotating Island 1 by $180^\circ$ (or reflecting it across both axes) yields the exact shape of Island 2!
      - Under the full symmetry group, both islands are congruent.
      - Number of distinct islands is **1**.
- **The Dihedral Group $D_4$ & Canonicalization Invariant:**
  - **The 8 Symmetries of the 2D Grid Lattice:**
    - Any rigid isometry of the square lattice $\mathbb{Z}^2$ is an element of the dihedral group $D_4$, generating exactly 8 coordinate transformations for each point $(x, y)$:
      $$
      \begin{aligned}
      1. \quad & (+x, \; +y) \quad (\text{Identity}) \\
      2. \quad & (+x, \; -y) \quad (\text{Horizontal reflection}) \\
      3. \quad & (-x, \; +y) \quad (\text{Vertical reflection}) \\
      4. \quad & (-x, \; -y) \quad (180^\circ \text{ half-turn}) \\
      5. \quad & (+y, \; +x) \quad (\text{Diagonal reflection } y = x) \\
      6. \quad & (+y, \; -x) \quad (90^\circ \text{ clockwise rotation}) \\
      7. \quad & (-y, \; +x) \quad (90^\circ \text{ counter-clockwise rotation}) \\
      8. \quad & (-y, \; -x) \quad (\text{Anti-diagonal reflection } y = -x)
      \end{aligned}
      $$
  - **Translation Normalization:**
    - For each of the 8 transformed point sets:
      1. Sort the points lexicographically: $P_0, P_1, \dots, P_{k-1}$.
      2. Translate the set so that the anchor point $P_0$ is mapped to the origin $(0, 0)$:
         $$
         P_i' = (P_i.x - P_0.x, \; P_i.y - P_0.y)
         $$
  - **Canonical Orbit Representative:**
    - Each of the 8 normalized point lists forms a candidate shape signature.
    - Sort the 8 candidate signatures lexicographically and choose the **lexicographically smallest** signature as the canonical hashable key for the island:
      $$
      \text{Canonical}(Island) = \min_{g \in D_4} \text{normalize}(g(Island))
      $$
    - Two islands are congruent under $D_4$ if and only if their canonical representations are identical!
- **Step-by-Step Worked Execution Trace on the $4 \times 5$ Grid:**
  - **Step 1: Discover Island 1 at $(0, 0)$:**
    - DFS gathers cells of top-left L-shape:
      $$
      \text{Cells}_1 = [(0, 0), \; (0, 1), \; (1, 0)]
      $$
    - Sink cells in grid ($grid[i][j] \leftarrow 0$).
  - **Step 2: Canonicalize Island 1:**
    - Apply 8 transformations and normalize each to origin:
      - Transformation 1 $(+x, +y)$:
        - Points: $(0, 0), (0, 1), (1, 0)$.
        - Already starts at $(0, 0)$.
        - Normalized list:
          $$
          [(0, 0), \; (0, 1), \; (1, 0)]
          $$
      - Transformation 4 $(-x, -y)$:
        - Points: $(0, 0), (0, -1), (-1, 0)$.
        - Sorted: $(-1, 0), (0, -1), (0, 0)$.
        - Subtract anchor $(-1, 0)$:
          - $(-1 - (-1), 0 - 0) = (0, 0)$
          - $(0 - (-1), -1 - 0) = (1, -1)$
          - $(0 - (-1), 0 - 0) = (1, 0)$
        - Normalized list:
          $$
          [(0, 0), \; (1, -1), \; (1, 0)]
          $$
      - Evaluating all 8 transformations and sorting candidates finds the unique minimal signature:
        $$
        K_1 = \text{Canonical}(\text{Cells}_1) = ((0, 0), \; (0, 1), \; (1, 0))
        $$
    - Add to set: $s \leftarrow \{ K_1 \}$.
  - **Step 3: Discover Island 2 at $(2, 4)$:**
    - Scan continues to row 2, col 4.
    - DFS gathers cells of bottom-right L-shape:
      $$
      \text{Cells}_2 = [(2, 4), \; (3, 3), \; (3, 4)]
      $$
    - Sink cells in grid.
  - **Step 4: Canonicalize Island 2:**
    - Apply 8 transformations and normalize each to origin:
      - Under Transformation 4 (a $180^\circ$ rotation about origin) and anchor subtraction:
        - Points: $(-2, -4), (-3, -3), (-3, -4)$.
        - Sorted: $(-3, -4), (-3, -3), (-2, -4)$.
        - Subtract anchor $(-3, -4)$:
          - $(-3 - (-3), -4 - (-4)) = (0, 0)$
          - $(-3 - (-3), -3 - (-4)) = (0, 1)$
          - $(-2 - (-3), -4 - (-4)) = (1, 0)$
        - Resulting normalized list:
          $$
          [(0, 0), \; (0, 1), \; (1, 0)]
          $$
      - Notice that this matches $K_1$ identically!
      - Minimal signature among all 8 transformations:
        $$
        K_2 = ((0, 0), \; (0, 1), \; (1, 0)) == K_1
        $$
    - Add to set:
      $$
      s \cup \{ K_2 \} = \{ K_1 \} \quad (|s| = \mathbf{1})
      $$
      - Duplicate shape absorbed!
  - **Step 5: Output Distinct Count:**
    $$
    ans = |s| = \mathbf{1}
    $$
- **Horizontal Domino vs Vertical Domino ($[[1, 1, 0, 1], [0, 0, 0, 1]]$):**
  - Island 1: $[(0, 0), (0, 1)]$ (horizontal 2-cell domino).
  - Island 2: $[(0, 3), (1, 3)]$ (vertical 2-cell domino).
  - Rotating Island 1 by $90^\circ$ maps it to a vertical domino.
  - Canonical representations for both evaluate to $((0, 0), (0, 1))$.
  - Returns **`1`**.
- **Chirality / Reflection Equivalence ($[[1, 0, 0, 1, 1], [1, 1, 0, 0, 1]]$):**
  - Corner shapes facing opposite directions match under reflection.
  - Returns **`1`**.

This instance demonstrates polyomino congruence classification under the dihedral group action $D_4 \curvearrowright \mathbb{Z}^2$, mathematically proves why orbit minimization over 8 affine transformations partitions grid components into rigid congruence classes, and derives $O(M \cdot N + K \cdot S \log S)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ binary grid:
Find the number of **distinct island shapes**.
Two islands are the same if one can be **translated, rotated, or reflected** to match the other.

```text
grid:
  1 1 0 0 0
  1 0 0 0 0
  0 0 0 0 1
  0 0 0 1 1

Island 1 (top-left):
  1 1
  1 .

Island 2 (bottom-right):
  . 1
  1 1

Rotating Island 1 by 180 degrees gives Island 2!
Under rotation/reflection, they are the same island!
Distinct islands = 1
```

### The Invariant of the 8 Dihedral Group Symmetries
- In 2D plane geometry, there are exactly 8 combinations of 4 rotations and reflections.
- For each island, generate all 8 transformed coordinate sets, translate each to start at $(0, 0)$, sort them, and select the lexicographically smallest set.
- This creates an unambiguous canonical signature that is completely invariant under translation, rotation, and reflection.

---

## 2. Conceptual Foundation & Invariants

### 1. The 8 Group Actions on Coordinates $(i, j)$:
$$
(i, j), \quad (i, -j), \quad (-i, j), \quad (-i, -j), \quad (j, i), \quad (j, -i), \quad (-j, i), \quad (-j, -i)
$$

### 2. Normalization Function:
For transformed point set $E = [P_0, P_1, \dots, P_{k-1}]$ sorted lexicographically:
$$
\text{normalize}(E) = [(P_i.x - P_0.x, \; P_i.y - P_0.y) \mid 0 \le i < k]
$$
$$
\text{Canonical}(Island) = \min_{g \in D_4} \text{normalize}(g(Island))
$$

> **Dihedral Quotient Space Invariant.** The isometry group of the square tiling $\text{Isom}(\mathbb{Z}^2) \cong \mathbb{Z}^2 \rtimes D_4$ partitions connected polyominoes into discrete orbits, with each orbit uniquely represented by the lexicographical minimum of its origin-translated elements.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Island 1 Cells
- $(0, 0), (0, 1), (1, 0)$.
- Minimal canonical form: `((0, 0), (0, 1), (1, 0))`.
- Insert into set $s$.

---

### Step 2: Island 2 Cells
- $(2, 4), (3, 3), (3, 4)$.
- Under $180^\circ$ rotation:
  - $(0, 0), (0, 1), (1, 0)$.
- Minimal canonical form matches Island 1!
- Duplicate in set $s$.

---

### Step 3: Output
- $|s| = \mathbf{1}$.

---

## 4. Complete Execution Trace

| Island Found | Original Cells | Symmetry Action Applied | Sorted & Origin-Shifted | Canonical Signature Chosen | Set Size $|s|$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Island 1 | $(0, 0), (0, 1), (1, 0)$ | Identity $(+x, +y)$ | `[(0, 0), (0, 1), (1, 0)]` | `((0, 0), (0, 1), (1, 0))` | $1$ |
| Island 2 | $(2, 4), (3, 3), (3, 4)$ | Half-turn $(-x, -y)$ | `[(0, 0), (0, 1), (1, 0)]` | `((0, 0), (0, 1), (1, 0))` | $1$ |
| **Total** | — | — | — | — | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell ($[[1]]$):** All 8 transformations produce `((0, 0))` $\implies 1$.
- **All Water ($[[0]]$):** 0 islands $\implies 0$.
- **Domino Shapes (Horizontal vs Vertical):** $90^\circ$ rotation maps one to the other $\implies 1$.
- **Asymmetric Polyominoes:** Chiral pairs that cannot be rotated without reflection are considered equal because reflections are permitted.

---

## 6. Traps & Common Anti-Patterns

- **Only Checking Rotations (Neglecting Reflections):** The problem explicitly allows reflections; checking only 4 rotations will treat mirror images as distinct. All 8 transformations must be generated.
- **Forgetting to Re-sort Before Normalizing:** Points after transformation must be re-sorted so that $P_0$ is the true lexicographical minimum before subtracting.
- **Using Hash of Area or Perimeter:** Incomplete invariants (like area or perimeter) produce false positives on non-congruent polyominoes. Full coordinate list comparison is required.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding islands via DFS: $\mathcal{O}(M \cdot N)$ time.
  - For each island of $S$ cells: generates 8 forms, sorts $S$ points ($8 \cdot S \log S$).
  - Total Time: $\mathcal{O}(M \cdot N + \sum S_i \log S_i)$. For $M = N = 50$, executes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ memory for grid traversal and shape signature storage.
