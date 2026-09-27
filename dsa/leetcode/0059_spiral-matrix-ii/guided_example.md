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
- **Pre-allocating Rows Correctly:** Using `matrix = [[0] * n for _ in range(n)]` creates independent row lists. Writing `[[0] * n] * n` creates $n$ references to the same underlying list, causing simultaneous overwrites across all rows.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Each of the $n^2$ cells is written exactly once.
- **Auxiliary Space Complexity:** $O(1)$ beyond the required $n \times n$ output matrix.
