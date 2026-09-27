# Guided Example: Spiral Matrix

We trace the step-by-step 4-boundary contraction simulation on a representative 2D matrix:

- **Input:** $\text{matrix} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$
- **Required output:** $[1, 2, 3, 6, 9, 8, 7, 4, 5]$

This instance demonstrates four-directional boundary maintenance ($\text{top}$, $\text{bottom}$, $\text{left}$, $\text{right}$), progressive inward contraction, boundary crossing checks to prevent redundant passes in non-square matrices, and linear-time collection.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ matrix with $M = 3$ rows and $N = 3$ columns:
$$
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
$$
return all elements in clockwise spiral order starting from top-left $(0, 0)$.

Instead of allocating an auxiliary 2D boolean array to track visited cells, the four-boundary method maintains four bounding markers:
- $\text{top}$ and $\text{bottom}$ (row boundaries)
- $\text{left}$ and $\text{right}$ (column boundaries)

Each phase traverses one full outer edge and then contracts the corresponding boundary inward by 1 unit. When opposite boundaries cross ($\text{top} > \text{bottom}$ or $\text{left} > \text{right}$), the spiral traversal is guaranteed complete.

---

## 2. Conceptual Foundation & Invariants

### The 4-Phase Cyclic Boundary Traversal
We initialize:
$$
\text{top} = 0, \quad \text{bottom} = M - 1, \quad \text{left} = 0, \quad \text{right} = N - 1
$$

While $\text{top} \le \text{bottom}$ and $\text{left} \le \text{right}$:
1. **Move Right across `top`:**
   Traverse $(r = \text{top}, c)$ for $c \in [\text{left}, \text{right}]$.
   Contract top boundary: $\text{top} \leftarrow \text{top} + 1$.
2. **Move Down along `right`:**
   Traverse $(r, c = \text{right})$ for $r \in [\text{top}, \text{bottom}]$.
   Contract right boundary: $\text{right} \leftarrow \text{right} - 1$.
3. **Move Left across `bottom` (if $\text{top} \le \text{bottom}$):**
   Traverse $(r = \text{bottom}, c)$ for $c \in [\text{right}, \text{left}]$ in descending order.
   Contract bottom boundary: $\text{bottom} \leftarrow \text{bottom} - 1$.
4. **Move Up along `left` (if $\text{left} \le \text{right}$):**
   Traverse $(r, c = \text{left})$ for $r \in [\text{bottom}, \text{top}]$ in descending order.
   Contract left boundary: $\text{left} \leftarrow \text{left} + 1$.

> **Invariant.** At each step, all visited cells lie strictly outside the active boundary rectangle $[\text{top}, \text{bottom}] \times [\text{left}, \text{right}]$, and all unvisited cells lie strictly within it.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ matrix:

### Layer 1: Outer Ring ($\text{top}=0, \text{bottom}=2, \text{left}=0, \text{right}=2$)

- **Phase 1: Move Right along Row 0 ($c = 0 \to 2$):**
  - Read $\text{matrix}[0][0] = 1$
  - Read $\text{matrix}[0][1] = 2$
  - Read $\text{matrix}[0][2] = 3$
  - Collected: $[1, 2, 3]$.
  - Contract top: $\text{top} \leftarrow 0 + 1 = 1$.

- **Phase 2: Move Down along Column 2 ($r = 1 \to 2$):**
  - Read $\text{matrix}[1][2] = 6$
  - Read $\text{matrix}[2][2] = 9$
  - Collected: $[1, 2, 3, 6, 9]$.
  - Contract right: $\text{right} \leftarrow 2 - 1 = 1$.

- **Phase 3: Move Left along Row 2 ($c = 1 \to 0$):**
  - Guard check: $\text{top} \le \text{bottom}$ ($1 \le 2$). Valid!
  - Read $\text{matrix}[2][1] = 8$
  - Read $\text{matrix}[2][0] = 7$
  - Collected: $[1, 2, 3, 6, 9, 8, 7]$.
  - Contract bottom: $\text{bottom} \leftarrow 2 - 1 = 1$.

- **Phase 4: Move Up along Column 0 ($r = 1 \to 1$):**
  - Guard check: $\text{left} \le \text{right}$ ($0 \le 1$). Valid!
  - Read $\text{matrix}[1][0] = 4$
  - Collected: $[1, 2, 3, 6, 9, 8, 7, 4]$.
  - Contract left: $\text{left} \leftarrow 0 + 1 = 1$.

---

### Layer 2: Center Element ($\text{top}=1, \text{bottom}=1, \text{left}=1, \text{right}=1$)

- **Phase 1: Move Right along Row 1 ($c = 1 \to 1$):**
  - Read $\text{matrix}[1][1] = 5$
  - Collected: $[1, 2, 3, 6, 9, 8, 7, 4, 5]$.
  - Contract top: $\text{top} \leftarrow 1 + 1 = 2$.

- **Phase 2: Move Down along Column 1 ($r = 2 \to 1$):**
  - $\text{top} > \text{bottom}$ ($2 > 1$). Loop does not execute.
  - Contract right: $\text{right} \leftarrow 1 - 1 = 0$.

- **Termination:**
  - $\text{top} = 2 > \text{bottom} = 1$ and $\text{left} = 1 > \text{right} = 0$.
  - Outer while-loop halts.

Final result: $[1, 2, 3, 6, 9, 8, 7, 4, 5]$.

---

## 4. Complete Execution Trace

| Step | Motion Direction | Traversed Cells $(r, c)$ | Values Harvested | Boundary State After Step $(\text{top}, \text{bottom}, \text{left}, \text{right})$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Right | $(0, 0), (0, 1), (0, 2)$ | $1, 2, 3$ | $\text{top} = 1, \text{bottom} = 2, \text{left} = 0, \text{right} = 2$ |
| 2 | Down | $(1, 2), (2, 2)$ | $6, 9$ | $\text{top} = 1, \text{bottom} = 2, \text{left} = 0, \text{right} = 1$ |
| 3 | Left | $(2, 1), (2, 0)$ | $8, 7$ | $\text{top} = 1, \text{bottom} = 1, \text{left} = 0, \text{right} = 1$ |
| 4 | Up | $(1, 0)$ | $4$ | $\text{top} = 1, \text{bottom} = 1, \text{left} = 1, \text{right} = 1$ |
| 5 | Right | $(1, 1)$ | **5** | $\text{top} = 2, \text{bottom} = 1, \text{left} = 1, \text{right} = 1$ (Exit) |

---

## 5. Algorithmic Correctness

**Soundness.** Because each edge traversal moves along the boundary of the unvisited interior and immediately increments or decrements that boundary, no cell can ever be visited twice.

**Completeness.** The boundary rectangle strictly shrinks with every completed edge. The while condition $\text{top} \le \text{bottom} \land \text{left} \le \text{right}$ ensures all $M \times N$ cells are included before termination.

---

## 6. Traps This Instance Exposes

- **Missing Guards on Left and Up:** In non-square matrices (e.g., $1 \times 4$ or $3 \times 1$), the top boundary increment can cause $\text{top} > \text{bottom}$ before Phase 3 executes. Without the condition `if top <= bottom:` before moving left, the bottom row would be traversed backwards again, causing duplicate element readings.
- **Empty Matrix:** If $\text{matrix} = []$ or $\text{matrix}[0] = []$, returning `[]` upfront prevents index errors when initializing boundaries.

### Degenerate Shapes and the Sweeps They Suppress

The same four phases serve every legal shape, because $1 \le m, n \le 10$ guarantees an outer ring always exists. What changes is which later sweep has an empty range, and only the guards keep that empty range from turning into a re-read of cells already collected.

| Shape | Instance | Rectangle before the first phase | Sweep that must contribute nothing | Verified output |
|---|---|---|---|---|
| Single cell $1 \times 1$ | `[[-100]]` | $\text{top}=0, \text{bottom}=0, \text{left}=0, \text{right}=0$ | Every phase after the first: $\text{top}$ becomes $1$, so the downward sweep and both guarded sweeps are empty. | `[-100]` |
| Single row $1 \times 4$ | `[[1,2,3,4]]` | $\text{top}=0, \text{bottom}=0, \text{left}=0, \text{right}=3$ | The leftward sweep: after the top row is read, $\text{top}=1 > \text{bottom}=0$, so sweeping row $0$ backwards would repeat $3, 2, 1$. | `[1,2,3,4]` |
| Single column $4 \times 1$ | `[[1],[2],[3],[4]]` | $\text{top}=0, \text{bottom}=3, \text{left}=0, \text{right}=0$ | The upward sweep: after the right column is read, $\text{right}=-1 < \text{left}=0$, so climbing column $0$ would repeat $4, 3, 2$. | `[1,2,3,4]` |
| Wide $3 \times 4$ | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | $\text{top}=0, \text{bottom}=2, \text{left}=0, \text{right}=3$ | The second-layer leftward sweep: the rectangle is one row tall with $\text{top}=2 > \text{bottom}=1$, so moving left along row $1$ would repeat $6$. | `[1,2,3,4,8,12,11,10,9,5,6,7]` |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. Every element is visited exactly once.
- **Auxiliary Space Complexity:** $O(1)$. Boundary pointers (`top`, `bottom`, `left`, `right`) require constant extra storage beyond the returned output list.

### Comparison of Candidate Traversals

Every method below emits the same permutation on this instance; they differ in what they must remember between steps and in which shape breaks them.

| Method | What it maintains | Time | Auxiliary space | Tradeoff or failure mode |
|---|---|---|---|---|
| Boundary contraction (this lesson) | Four integers: $\text{top}, \text{bottom}, \text{left}, \text{right}$ | $O(m \cdot n)$ | $O(1)$ beyond the output | The leftward and upward sweeps need the $\text{top} \le \text{bottom}$ and $\text{left} \le \text{right}$ guards, or single-row and single-column shapes duplicate their edge cells. |
| Visited grid with a rotating direction vector | An $m \times n$ boolean grid plus the current heading | $O(m \cdot n)$ | $O(m \cdot n)$ | Bounds alone cannot decide a turn: the walker must test whether the candidate cell was already collected, otherwise it re-enters a spent ring instead of turning. |
| Peel-and-rotate | A fresh matrix holding the remaining ring unrolled | $O(m \cdot n)$ | $O(m \cdot n)$ | Reading the top row and reversing the remainder is easy to state, but every rotation copies all surviving elements, and the coordinate meaning of rows and columns swaps at each layer. |
| Recursive layer peeling | One call frame per ring | $O(m \cdot n)$ | $O(\min(m, n))$ stack depth | Clean and short, yet it consumes stack proportional to the number of rings; with $m, n \le 10$ that is at most five frames, so the risk here is conceptual rather than practical. |
