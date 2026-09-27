# Guided Example: Spiral Matrix II

We trace the step-by-step matrix generation and four-boundary contraction algorithm for an $n \times n$ grid:

- **Input:** $n = 3$
- **Required output:** $\begin{pmatrix} 1 & 2 & 3 \\ 8 & 9 & 4 \\ 7 & 6 & 5 \end{pmatrix}$

This instance demonstrates generating an $n \times n$ grid from values $1 \dots n^2$, synchronizing four directional boundaries ($\text{top}, \text{bottom}, \text{left}, \text{right}$), progressive inward winding, and handling odd-dimension center terminal cells.

---

## 1. Instance & Teaching Goal

Given a positive integer $n = 3$, generate an $n \times n$ matrix filled with elements from $1$ to $n^2 = 9$ in clockwise spiral order.

The target matrix is:
$$
\begin{pmatrix}
1 & 2 & 3 \\
8 & 9 & 4 \\
7 & 6 & 5
\end{pmatrix}
$$

Rather than testing for occupied non-zero cells and turning upon collisions, the four-boundary approach predefines the rectangular bounding box $[\text{top}, \text{bottom}] \times [\text{left}, \text{right}]$. Filling each side directly with a simple for-loop and contracting the boundary eliminates branching overhead and guarantees exactly $n^2$ writes in $O(n^2)$ time.

---

## 2. Conceptual Foundation & Invariants

### 4-Boundary Inward Winding
We allocate an $n \times n$ matrix initialized to zeroes and set boundaries:
$$
\text{top} = 0, \quad \text{bottom} = n - 1, \quad \text{left} = 0, \quad \text{right} = n - 1
$$
We maintain an incrementing counter $\text{val} = 1$.

While $\text{val} \le n^2$:
1. **Fill Top Row (Left to Right):**
   For $c \in [\text{left}, \text{right}]$: $\text{matrix}[\text{top}][c] \leftarrow \text{val}++$.
   Contract top boundary: $\text{top} \leftarrow \text{top} + 1$.
2. **Fill Right Column (Top to Bottom):**
   For $r \in [\text{top}, \text{bottom}]$: $\text{matrix}[r][\text{right}] \leftarrow \text{val}++$.
   Contract right boundary: $\text{right} \leftarrow \text{right} - 1$.
3. **Fill Bottom Row (Right to Left):**
   For $c \in [\text{right}, \text{left}]$ descending: $\text{matrix}[\text{bottom}][c] \leftarrow \text{val}++$.
   Contract bottom boundary: $\text{bottom} \leftarrow \text{bottom} - 1$.
4. **Fill Left Column (Bottom to Top):**
   For $r \in [\text{bottom}, \text{top}]$ descending: $\text{matrix}[r][\text{left}] \leftarrow \text{val}++$.
   Contract left boundary: $\text{left} \leftarrow \text{left} + 1$.

> **Invariant.** At any step, the boundary rectangle $[\text{top}, \text{bottom}] \times [\text{left}, \text{right}]$ encloses all and only the unfilled cells of the matrix.

---

## 3. Step-by-Step Worked Execution

We generate the $3 \times 3$ matrix with values $1 \dots 9$:

### Layer 1: Outer Perimeter ($\text{top}=0, \text{bottom}=2, \text{left}=0, \text{right}=2$)

- **Phase 1: Fill Row 0 from Left to Right ($c = 0 \to 2$):**
  - $\text{matrix}[0][0] = 1$
  - $\text{matrix}[0][1] = 2$
  - $\text{matrix}[0][2] = 3$
  - Values written: $1, 2, 3$. Contract: $\text{top} \leftarrow 1$.

- **Phase 2: Fill Column 2 from Top to Bottom ($r = 1 \to 2$):**
  - $\text{matrix}[1][2] = 4$
  - $\text{matrix}[2][2] = 5$
  - Values written: $4, 5$. Contract: $\text{right} \leftarrow 1$.

- **Phase 3: Fill Row 2 from Right to Left ($c = 1 \to 0$):**
  - $\text{matrix}[2][1] = 6$
  - $\text{matrix}[2][0] = 7$
  - Values written: $6, 7$. Contract: $\text{bottom} \leftarrow 1$.

- **Phase 4: Fill Column 0 from Bottom to Top ($r = 1 \to 1$):**
  - $\text{matrix}[1][0] = 8$
  - Values written: $8$. Contract: $\text{left} \leftarrow 1$.

---

### Layer 2: Center Cell ($\text{top}=1, \text{bottom}=1, \text{left}=1, \text{right}=1$)

- **Phase 1: Fill Row 1 from Left to Right ($c = 1 \to 1$):**
  - $\text{matrix}[1][1] = 9$
  - Value written: $9$. Contract: $\text{top} \leftarrow 2$.
  - $\text{val} = 10 > n^2 \implies$ Loop terminates.

Final generated matrix:
$$
\begin{pmatrix}
1 & 2 & 3 \\
8 & 9 & 4 \\
7 & 6 & 5
\end{pmatrix}
$$

---

## 4. Complete Execution Trace

| Value Written | Target Coordinate $(r, c)$ | Direction Phase | Active Boundaries $(\text{top}, \text{bottom}, \text{left}, \text{right})$ | Boundary Updated After Phase |
|:---:|:---:|:---:|:---:|:---|
| 1 | $(0, 0)$ | Right | $0, 2, 0, 2$ | - |
| 2 | $(0, 1)$ | Right | $0, 2, 0, 2$ | - |
| 3 | $(0, 2)$ | Right | $0, 2, 0, 2$ | $\text{top} \leftarrow 1$ |
| 4 | $(1, 2)$ | Down | $1, 2, 0, 2$ | - |
| 5 | $(2, 2)$ | Down | $1, 2, 0, 2$ | $\text{right} \leftarrow 1$ |
| 6 | $(2, 1)$ | Left | $1, 2, 0, 1$ | - |
| 7 | $(2, 0)$ | Left | $1, 2, 0, 1$ | $\text{bottom} \leftarrow 1$ |
| 8 | $(1, 0)$ | Up | $1, 1, 0, 1$ | $\text{left} \leftarrow 1$ |
| **9** | **$(1, 1)$** | **Right** | **$1, 1, 1, 1$** | **$\text{top} \leftarrow 2$ (Exit)** |

---

## 5. Algorithmic Correctness

**Soundness.** Each of the four phases fills a distinct segment along the perimeter of the active boundary box and immediately contracts that boundary. Consequently, no coordinate $(r, c)$ can be written to more than once.

**Completeness.** Since the boundaries shrink by 1 after each edge, the area of the rectangle decreases monotonically until $\text{top} > \text{bottom}$ or $\text{left} > \text{right}$. Exactly $n^2$ values are written, guaranteeing every cell in the $n \times n$ matrix is filled.

---

## 6. Traps This Instance Exposes

- **Odd $n$ Center Overwrite:** For odd $n$ (like $n = 3$), the center cell $(1, 1)$ is written during the final "Right" pass. Checking $\text{val} \le n^2$ prevents subsequent "Down", "Left", or "Up" steps from executing on already-crossed boundaries.
- **Pre-allocating Rows Correctly:** The grid must be built from $n$ independent row lists. Constructing it by repeating one row $n$ times makes every row an alias of the same underlying storage, so a single write would appear in all $n$ rows at once.

### How the Winding Ends for Each Size

The parity of $n$ decides the shape of the final block: an odd side length leaves a $1 \times 1$ centre written by the rightward phase, while an even side length leaves a $2 \times 2$ block whose last entry is written by the leftward phase of the bottom row. Every row below was checked against the verified matrices.

| Size $n$ | Rings fully traversed first | Final block | Phase that writes the last value | Verified last value and block |
|---|---|---|---|---|
| 1 | 0 | the single cell | Phase 1, which is the entire matrix | $1$ at $(0,0)$; `[[1]]` |
| 2 | 0 | the whole $2 \times 2$ grid | Phase 3 (bottom row); phase 4 spans the empty range from $\text{bottom} = 0$ up to $\text{top} = 1$ | $4$ at $(1,0)$; `[[1,2],[4,3]]` |
| 3 | 1 | $1 \times 1$ centre | Phase 1 of the centre layer | $9$ at $(1,1)$; `[[1,2,3],[8,9,4],[7,6,5]]` |
| 4 | 1 | $2 \times 2$ centre | Phase 3 of the centre layer | $16$ at $(2,1)$; centre block $\begin{pmatrix}13&14\\16&15\end{pmatrix}$ |
| 5 | 2 | $1 \times 1$ centre | Phase 1 of the centre layer | $25$ at $(2,2)$; `[[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]` |
| 20 | 9 | $2 \times 2$ centre | Phase 3 of the centre layer | $400$ at $(10,9)$; centre block $\begin{pmatrix}397&398\\400&399\end{pmatrix}$ |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Each of the $n^2$ cells is written exactly once.
- **Auxiliary Space Complexity:** $O(1)$ beyond the required $n \times n$ output matrix.

### Comparison of Candidate Methods

Each method below produces the same grid; they differ in what they track between writes and in which layer exposes their weakness.

| Method | Time | Auxiliary space | Tradeoff or failure mode |
|---|---|---|---|
| Four-boundary contraction driven by the value counter (this lesson) | $O(n^{2})$ | $O(1)$ beyond the output | The value counter is what makes guards on phases 3 and 4 unnecessary; driving the loop by the boundary test alone repeats the centre coordinate once a layer shrinks to one cell. |
| Rotating heading with a zero test on the grid | $O(n^{2})$ | $O(1)$ beyond the output, because unwritten cells already record occupancy | The turn must be decided before the step by testing both the grid edge and the candidate cell, and the new heading has to be committed only after that test. |
| Layer-by-layer recursion | $O(n^{2})$ | $O(n)$ call frames, one per ring | Depth grows with $n$ — ten frames at the maximum $n = 20$ — and each level must re-derive its own offsets. |
| Closed-form mapping from the counter to a coordinate | $O(n^{2})$ | $O(1)$ | Four piecewise branches, one per side, and each corner belongs to the side that reaches it first; an off-by-one at a corner silently swaps two values. |
