# Guided Example: Diagonal Traverse

We trace the step-by-step anti-diagonal grouping invariant ($i + j = k$), alternating serpentine direction control (even $k$: up-right, odd $k$: down-left), boundary clamping ($k < n$ vs $k \ge n$), and flattening on representative 2D matrices:

- **Input:**
  $$
  mat = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
  $$
- **Required output:** `[1, 2, 4, 7, 5, 3, 6, 8, 9]`
  - Matrix dimensions: $m = 3, \; n = 3$
  - Total diagonals: $m + n - 1 = 3 + 3 - 1 = \mathbf{5}$ diagonals ($k \in [0, 4]$)
  - Key Invariant: Every cell $(i, j)$ on the $k$-th diagonal satisfies:
    $$
    i + j = k
    $$
  - Serpentine parity rule:
    - If diagonal index $k$ is **even**: travel **Up-Right** ($\nearrow$)
    - If diagonal index $k$ is **odd**: travel **Down-Left** ($\swarrow$)
- **Diagonal-by-diagonal execution trace:**
  - **Diagonal $k = 0$ (Even $\implies$ Up-Right):**
    - Cells with $i + j = 0$: $(0, 0)$
    - Value: `[1]`
    - Emitted: `[1]`
  - **Diagonal $k = 1$ (Odd $\implies$ Down-Left):**
    - Cells with $i + j = 1$: $(0, 1), (1, 0)$
    - Travel down-left: $(0, 1) \to (1, 0)$
    - Values: `[2, 4]`
    - Emitted: `[2, 4]`
  - **Diagonal $k = 2$ (Even $\implies$ Up-Right):**
    - Cells with $i + j = 2$: $(0, 2), (1, 1), (2, 0)$
    - Travel up-right: $(2, 0) \to (1, 1) \to (0, 2)$
    - Values: `[7, 5, 3]`
    - Emitted: `[7, 5, 3]`
  - **Diagonal $k = 3$ (Odd $\implies$ Down-Left):**
    - Cells with $i + j = 3$: $(1, 2), (2, 1)$
    - Travel down-left: $(1, 2) \to (2, 1)$
    - Values: `[6, 8]`
    - Emitted: `[6, 8]`
  - **Diagonal $k = 4$ (Even $\implies$ Up-Right):**
    - Cells with $i + j = 4$: $(2, 2)$
    - Value: `[9]`
    - Emitted: `[9]`
  - Concatenated final sequence:
    $$
    [1, \; 2, \; 4, \; 7, \; 5, \; 3, \; 6, \; 8, \; 9]
    $$
- **Non-Square Matrix Instance ($2 \times 3$):**
  - $mat = [[1, 2, 3], [4, 5, 6]]$
  - $k=0: [1]$
  - $k=1: [2, 4]$
  - $k=2: [5, 3]$ (reverses $[3, 5]$ to go up-right $\implies [5, 3]$)
  - $k=3: [6]$
  - Output: `[1, 2, 4, 5, 3, 6]`
- **Single Element Matrix:** $mat = [[5]] \implies [5]$

This instance demonstrates index-sum planar transformations, mathematically proves why parity-based reversals generate serpentine zig-zag trajectories without explicit boundary bouncing state machines, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ matrix $mat$:
Return an array of all elements of the matrix in **diagonal order** (serpentine zig-zag).

```text
3 x 3 Matrix:
  [ 1,  2,  3 ]
  [ 4,  5,  6 ]
  [ 7,  8,  9 ]

Zig-Zag Traverse Path:
  Diagonal 0 (k=0, Even):  (0, 0)               -> [1]
  Diagonal 1 (k=1, Odd):   (0, 1) -> (1, 0)     -> [2, 4]
  Diagonal 2 (k=2, Even):  (2, 0) -> (1, 1) -> (0, 2) -> [7, 5, 3]
  Diagonal 3 (k=3, Odd):   (1, 2) -> (2, 1)     -> [6, 8]
  Diagonal 4 (k=4, Even):  (2, 2)               -> [9]

Result: [ 1,  2,  4,  7,  5,  3,  6,  8,  9 ]
```

### The Invariant of Anti-Diagonals
In any 2D grid:
- Every cell $(i, j)$ on the same top-right to bottom-left anti-diagonal shares the **exact same sum of coordinates**:
  $$
  i + j = k
  $$
- The diagonal index $k$ ranges from $0$ (the top-left corner $(0, 0)$) to $m + n - 2$ (the bottom-right corner $(m-1, n-1)$).
- There are exactly $m + n - 1$ diagonals.
- By alternating the direction of travel based on the parity of $k$ ($k \pmod 2$), the zig-zag pattern emerges naturally.

---

## 2. Conceptual Foundation & Invariants

### 1. Starting Coordinates for Diagonal $k$:
To collect cells on diagonal $k$ ($i + j = k$):
- Starting row:
  $$
  i =
  \begin{cases}
  0 & \text{if } k < n \\
  k - n + 1 & \text{if } k \ge n
  \end{cases}
  $$
- Starting column:
  $$
  j =
  \begin{cases}
  k & \text{if } k < n \\
  n - 1 & \text{if } k \ge n
  \end{cases}
  $$
- Traverse down-left by stepping: $i \leftarrow i + 1, \; j \leftarrow j - 1$.
- Continue while $i < m$ and $j \ge 0$.

### 2. Parity Direction Inversion:
Collect all elements of diagonal $k$ into a temporary list $t$:
- If $k$ is **odd**: The natural traversal order (down-left) is already correct.
- If $k$ is **even**: Reverse the list $t \leftarrow t[::-1]$ to produce the upward-right order!
- Append $t$ to the answer array.

> **Parity Direction Invariant.** Even diagonals are traversed up-right ($\Delta i = -1, \Delta j = +1$), while odd diagonals are traversed down-left ($\Delta i = +1, \Delta j = -1$).

---

## 3. Step-by-Step Worked Execution

We trace $mat = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$ ($m = 3, n = 3$):
Diagonals $k \in [0, 4]$.

---

### Step 1: Diagonal $k = 0$
- $k = 0 < 3 \implies i = 0, j = 0$.
- Gather: $(0, 0) \to 1$.
- List $t = [1]$.
- Parity: $k = 0$ is even $\implies$ reverse $[1] = [1]$.
- Output buffer: `[1]`.

---

### Step 2: Diagonal $k = 1$
- $k = 1 < 3 \implies i = 0, j = 1$.
- Gather down-left:
  - $(0, 1) \to 2$. Step: $i = 1, j = 0$.
  - $(1, 0) \to 4$. Step: $i = 2, j = -1$ (stop).
- List $t = [2, 4]$.
- Parity: $k = 1$ is odd $\implies$ keep as is: `[2, 4]`.
- Output buffer: `[1, 2, 4]`.

---

### Step 3: Diagonal $k = 2$
- $k = 2 < 3 \implies i = 0, j = 2$.
- Gather down-left:
  - $(0, 2) \to 3$
  - $(1, 1) \to 5$
  - $(2, 0) \to 7$
- List $t = [3, 5, 7]$.
- Parity: $k = 2$ is even $\implies$ reverse:
  $$
  t = [7, \; 5, \; 3]
  $$
- Output buffer: `[1, 2, 4, 7, 5, 3]`.

---

### Step 4: Diagonal $k = 3$
- $k = 3 \ge 3 \implies i = 3 - 3 + 1 = 1, \; j = 2$.
- Gather down-left:
  - $(1, 2) \to 6$
  - $(2, 1) \to 8$
- List $t = [6, 8]$.
- Parity: $k = 3$ is odd $\implies$ keep: `[6, 8]`.
- Output buffer: `[1, 2, 4, 7, 5, 3, 6, 8]`.

---

### Step 5: Diagonal $k = 4$
- $k = 4 \ge 3 \implies i = 4 - 3 + 1 = 2, \; j = 2$.
- Gather: $(2, 2) \to 9$.
- List $t = [9]$.
- Parity: $k = 4$ is even $\implies [9]$.
- Output buffer: `[1, 2, 4, 7, 5, 3, 6, 8, 9]`.

---

## 4. Complete Execution Trace

| Diagonal Index $k$ | Sum $i + j$ | Initial Top Cell $(i, j)$ | Cells Traversed Down-Left | Raw Values $t$ | Parity $k \pmod 2$ | Direction Order | Elements Appended |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **$0$** | $0$ | $(0, 0)$ | $(0, 0)$ | `[1]` | Even | Up-Right | `[1]` |
| **$1$** | $1$ | $(0, 1)$ | $(0, 1) \to (1, 0)$ | `[2, 4]` | Odd | Down-Left | `[2, 4]` |
| **$2$** | $2$ | $(0, 2)$ | $(0, 2) \to (1, 1) \to (2, 0)$ | `[3, 5, 7]` | Even | Up-Right | `[7, 5, 3]` |
| **$3$** | $3$ | $(1, 2)$ | $(1, 2) \to (2, 1)$ | `[6, 8]` | Odd | Down-Left | `[6, 8]` |
| **$4$** | $4$ | $(2, 2)$ | $(2, 2)$ | `[9]` | Even | Up-Right | `[9]` |

---

## 5. Boundary Cases & Failure Modes

- **Single Row Matrix ($1 \times N$):** All diagonals have size 1 $\implies$ elements emitted in straight horizontal order.
- **Single Column Matrix ($M \times 1$):** All diagonals have size 1 $\implies$ elements emitted in vertical order.
- **$1 \times 1$ Matrix:** Emits `[mat[0][0]]`.
- **Large Rectangular Matrix ($1000 \times 10$):** Number of diagonals is $1009$, boundary clamping dynamically adjusts starting coordinates.

---

## 6. Traps & Common Anti-Patterns

- **Complex Boundary Bounce State Machines:** Trying to maintain $(r, c, \Delta r, \Delta c)$ and writing separate `if` conditions for hitting top, bottom, left, and right borders often results in 50+ lines of bug-prone code with corner-case crashes. Grouping by $i + j = k$ with parity reversal is 10 lines of robust code.
- **Hardcoding Square Bounds ($m == n$):** In non-square matrices ($2 \times 4$), $k$ exceeds $m$ before $n$ or vice-versa. Clamping with `k - n + 1` and `n - 1` prevents index out of bounds.
- **Allocating Full Diagonal Hash Tables:** Using a dictionary `defaultdict(list)` indexed by $i + j$ works, but uses unnecessary hashing overhead. Direct loop iteration computes diagonals in order with zero hash overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every element $(i, j)$ belongs to exactly one diagonal $k = i + j$.
  - Each cell is visited and copied once.
  - Reversing lists of length $L$ takes $O(L)$ time.
  - Total Time: $\sum L_k = \mathcal{O}(M \cdot N)$. For $10^4$ cells, executes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ to store the output array.
