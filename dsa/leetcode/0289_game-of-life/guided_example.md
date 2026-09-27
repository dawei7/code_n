# Guided Example: Game of Life

We trace the step-by-step 2-bit state encoding protocol ($2$ for live-to-dead, $-1$ for dead-to-live), 8-neighbor Moore neighborhood aggregation with self-exclusion, and in-place transition resolution on representative cellular automaton grids:

- **Input:**
  $$
  \text{board} = \begin{bmatrix}
  0 & 1 & 0 \\
  0 & 0 & 1 \\
  1 & 1 & 1 \\
  0 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  0 & 0 & 0 \\
  1 & 0 & 1 \\
  0 & 1 & 1 \\
  0 & 1 & 0
  \end{bmatrix}
  $$
- **Under-Population:** Live cell $(0, 1)$ with $1$ live neighbor dies ($\to 0$)
- **Over-Population:** Live cell with $> 3$ live neighbors dies ($\to 0$)
- **Reproduction:** Dead cells $(1, 0)$ and $(3, 1)$ with exactly $3$ live neighbors become live ($\to 1$)
- **Survival:** Live cells with $2$ or $3$ live neighbors remain live ($\to 1$)

This instance demonstrates in-place matrix transformation with simultaneous state transitions, proves why intermediate markers ($2$ and $-1$) allow past and future states to coexist in the same memory word without race conditions, avoids $O(M \times N)$ auxiliary board allocation, and executes in strictly $O(M \times N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a 2D grid representing Conway's Game of Life:
Each cell is either $0$ (dead) or $1$ (live).
Every cell interacts with its **8 neighbors** (horizontal, vertical, diagonal).
Rules for the next generation:
1. **Under-population:** Live cell with $< 2$ live neighbors dies.
2. **Survival:** Live cell with $2$ or $3$ live neighbors lives.
3. **Over-population:** Live cell with $> 3$ live neighbors dies.
4. **Reproduction:** Dead cell with exactly $3$ live neighbors becomes live.

All state transitions occur **simultaneously**.
The challenge: Update the board **in-place** with $O(1)$ auxiliary memory.

```text
Initial board:
0  1  0
0  0  1
1  1  1
0  0  0

Next generation:
0  0  0
1  0  1
0  1  1
0  1  0
```

### The In-Place Overwrite Conflict
If we directly change cell $(0, 1)$ from $1$ to $0$, then when its neighbor $(0, 2)$ is processed later, $(0, 2)$ would read $0$ instead of $1$!
The subsequent cell would compute its neighbor count based on the *new* generation rather than the *current* generation.
To solve this in $O(1)$ extra space:
We encode **both past and future states** into each cell using temporary integer markers.

---

## 2. Conceptual Foundation & Invariants

### State Encoding Matrix
We use a 4-state encoding system during Pass 1:

| Original State | Next State | Encoded Marker | Interpreted as Old State |
|:---:|:---:|:---:|:---|
| Dead ($0$) | Dead ($0$) | **$0$** | Dead ($\le 0$) |
| Live ($1$) | Live ($1$) | **$1$** | Live ($> 0$) |
| Live ($1$) | Dead ($0$) | **$2$** | **Live ($> 0$)** |
| Dead ($0$) | Live ($1$) | **$-1$** | **Dead ($\le 0$)** |

### Key Decoding Invariant:
When cell $(i, j)$ queries a neighbor $(x, y)$:
- A neighbor was **originally live** if and only if:
  $$
  \text{board}[x][y] > 0 \quad (\text{values } 1 \text{ and } 2)
  $$
- A neighbor was **originally dead** if and only if:
  $$
  \text{board}[x][y] \le 0 \quad (\text{values } 0 \text{ and } -1)
  $$

Thus, even if a neighbor was already processed and modified to $2$ or $-1$, subsequent cells can still determine its exact original state without any ambiguity!

### Two-Pass Execution Protocol:
- **Pass 1 (Mark Transitions):**
  For each cell $(i, j)$, count original live neighbors:
  - If $\text{board}[i][j] == 1$ and $(\text{live} < 2 \text{ or } \text{live} > 3)$:
    $$
    \text{board}[i][j] \leftarrow 2
    $$
  - If $\text{board}[i][j] == 0$ and $\text{live} == 3$:
    $$
    \text{board}[i][j] \leftarrow -1
    $$
- **Pass 2 (Normalize):**
  - If $\text{board}[i][j] == 2 \implies \text{board}[i][j] \leftarrow 0$.
  - If $\text{board}[i][j] == -1 \implies \text{board}[i][j] \leftarrow 1$.

---

## 3. Step-by-Step Worked Execution

We trace the $4 \times 3$ grid through Pass 1 and Pass 2:

---

### Pass 1: Transition Marking

- **Cell $(0, 0)$ ($0$):**
  - Neighbors $> 0$: $(0, 1)=1$. Live count $= 1$.
  - State: Remains $0$.
- **Cell $(0, 1)$ ($1$):**
  - Neighbors $> 0$: $(1, 2)=1$. Live count $= 1$ ($< 2 \implies$ dies).
  - State: Marked **$2$** (was live, now dying).
- **Cell $(0, 2)$ ($0$):**
  - Neighbors $> 0$: $(0, 1)=2$ (counted as live!), $(1, 2)=1$. Live count $= 2 \ne 3$.
  - State: Remains $0$.
- **Cell $(1, 0)$ ($0$):**
  - Neighbors $> 0$: $(0, 1)=2$, $(2, 0)=1$, $(2, 1)=1$. Live count $= 3$ ($\implies$ reproduction!).
  - State: Marked **$-1$** (was dead, now born).
- **Cell $(1, 1)$ ($0$):**
  - Neighbors $> 0$: $(0, 1)=2, (1, 2)=1, (2, 0)=1, (2, 1)=1, (2, 2)=1$.
  - Note: $(1, 0) = -1 \le 0$ (correctly ignored as originally dead!).
  - Live count $= 5 \ne 3$.
  - State: Remains $0$.
- **Cell $(1, 2)$ ($1$):**
  - Neighbors $> 0$: $(0, 1)=2, (2, 1)=1, (2, 2)=1$. Live count $= 3$ ($\implies$ survives!).
  - State: Remains $1$.
- **Cell $(2, 0)$ ($1$):**
  - Neighbors $> 0$: $(2, 1)=1$.
  - Note: $(1, 0) = -1 \le 0$ (originally dead).
  - Live count $= 1$ ($< 2 \implies$ dies).
  - State: Marked **$2$**.
- **Cell $(2, 1)$ ($1$):**
  - Neighbors $> 0$: $(1, 2)=1, (2, 0)=2, (2, 2)=1$. Live count $= 3$ ($\implies$ survives!).
  - State: Remains $1$.
- **Cell $(2, 2)$ ($1$):**
  - Neighbors $> 0$: $(1, 2)=1, (2, 1)=1$. Live count $= 2$ ($\implies$ survives!).
  - State: Remains $1$.
- **Cell $(3, 0)$ ($0$):**
  - Neighbors $> 0$: $(2, 0)=2, (2, 1)=1$. Live count $= 2 \ne 3$.
  - State: Remains $0$.
- **Cell $(3, 1)$ ($0$):**
  - Neighbors $> 0$: $(2, 0)=2, (2, 1)=1, (2, 2)=1$. Live count $= 3$ ($\implies$ reproduction!).
  - State: Marked **$-1$**.
- **Cell $(3, 2)$ ($0$):**
  - Neighbors $> 0$: $(2, 1)=1, (2, 2)=1$. Live count $= 2 \ne 3$.
  - State: Remains $0$.

Board after Pass 1:
$$
\begin{bmatrix}
0 & \mathbf{2} & 0 \\
\mathbf{-1} & 0 & 1 \\
\mathbf{2} & 1 & 1 \\
0 & \mathbf{-1} & 0
\end{bmatrix}
$$

---

### Pass 2: Normalization
Replace $2 \to 0$ and $-1 \to 1$:
- Row 0: $[0, 2, 0] \implies [0, 0, 0]$
- Row 1: $[-1, 0, 1] \implies [1, 0, 1]$
- Row 2: $[2, 1, 1] \implies [0, 1, 1]$
- Row 3: $[0, -1, 0] \implies [0, 1, 0]$

Final grid:
$$
\begin{bmatrix}
0 & 0 & 0 \\
1 & 0 & 1 \\
0 & 1 & 1 \\
0 & 1 & 0
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

```text
Pass 1 (Transitions):
  (0, 1): live=1 < 2   -> set to 2
  (1, 0): dead, live=3 -> set to -1
  (2, 0): live=1 < 2   -> set to 2
  (3, 1): dead, live=3 -> set to -1

Intermediate Board:
  [ 0,  2, 0]
  [-1,  0, 1]
  [ 2,  1, 1]
  [ 0, -1, 0]

Pass 2 (Normalize):
  2 -> 0, -1 -> 1

Final Board:
  [0, 0, 0]
  [1, 0, 1]
  [0, 1, 1]
  [0, 1, 0]
```

| Coordinate $(r, c)$ | Initial State | Live Neighbors ($> 0$) | Conway Rule Triggered | Encoded State | Final Normalized State |
|:---:|:---:|:---:|:---|:---:|:---:|
| $(0, 0)$ | 0 | 1 | No change | 0 | 0 |
| **$(0, 1)$** | **1** | **1** | **Under-population ($< 2$)** | **$2$** | **$0$** |
| $(0, 2)$ | 0 | 2 | No change | 0 | 0 |
| **$(1, 0)$** | **0** | **3** | **Reproduction ($== 3$)** | **$-1$** | **$1$** |
| $(1, 1)$ | 0 | 5 | Overcrowded | 0 | 0 |
| $(1, 2)$ | 1 | 3 | Survival ($2$ or $3$) | 1 | 1 |
| **$(2, 0)$** | **1** | **1** | **Under-population ($< 2$)** | **$2$** | **$0$** |
| $(2, 1)$ | 1 | 3 | Survival ($2$ or $3$) | 1 | 1 |
| $(2, 2)$ | 1 | 2 | Survival ($2$ or $3$) | 1 | 1 |
| $(3, 0)$ | 0 | 2 | No change | 0 | 0 |
| **$(3, 1)$** | **0** | **3** | **Reproduction ($== 3$)** | **$-1$** | **$1$** |
| $(3, 2)$ | 0 | 2 | No change | 0 | 0 |

---

## 5. Algorithmic Correctness

**Soundness.** The predicate $\text{board}[x][y] > 0$ accurately reflects whether cell $(x, y)$ was live in the original generation, regardless of whether it has already been processed and marked as $2$ (dying) or $-1$ (newborn). Because every neighbor inspection retrieves the exact original generation status, the simultaneous transition semantics of cellular automata are strictly preserved.

**Completeness.** Pass 1 evaluates all $M \times N$ cells under the 4 Conway rules. Pass 2 restores all temporary encodings to canonical binary values $\{0, 1\}$, ensuring no temporary markers leak into the final output.

---

## 6. Traps This Instance Exposes

- **In-Place Mutation Race Condition:** Directly writing $0$ or $1$ immediately corrupts subsequent neighbor evaluations. Encoding states into intermediate integers ($2$ and $-1$) completely decouples the read phase from the write phase.
- **Counting Self as Neighbor:** The loop over $[i - 1, i + 1] \times [j - 1, j + 1]$ includes the cell $(i, j)$ itself. Initializing $\text{live} = -\text{board}[i][j]$ cancels out the cell's own contribution if live, leaving strictly the 8 external neighbors.
- **Boundary Checks:** Cells on the edges and corners have only 3 or 5 neighbors. The bounds check $0 \le x < m$ and $0 \le y < n$ prevents `IndexError` on grid perimeters.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Pass 1 checks at most 9 coordinates per cell ($O(1)$ work). Pass 2 visits each cell once. Total time is strictly $O(M \times N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. Transformations occur entirely in-place inside the existing board matrix.
