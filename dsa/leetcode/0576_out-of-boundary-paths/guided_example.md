# Guided Example: Out of Boundary Paths

We trace the step-by-step 3D state space decomposition ($dfs(i, j, k)$), absorbing out-of-bounds boundary termination ($i \notin [0, m) \lor j \notin [0, n) \implies 1$), move budget depletion ($k \le 0 \implies 0$), 4-directional transition summation, modular arithmetic aggregation ($10^9 + 7$), and path multiplicity accumulation on representative grid scenarios:

- **Input:** $m = 2, \quad n = 2, \quad maxMove = 2, \quad startRow = 0, \quad startColumn = 0$
- **Required output:** `6`
  - Dimensions: $2 \times 2$ grid with cells $(0, 0), (0, 1), (1, 0), (1, 1)$.
  - Move limit: At most $maxMove = 2$ moves.
  - Allowed movements: Up, down, left, right.
  - Goal: Count how many distinct sequences of at most $2$ moves lead the ball to step **outside the grid boundary**, modulo $10^9 + 7$.
- **Memoized DFS State Definition ($dfs(i, j, k)$):**
  - Parameter $(i, j)$: Current row and column of the ball.
  - Parameter $k$: Remaining move budget ($k \in [0, maxMove]$).
  - **Terminal Conditions:**
    1. **Boundary Escape (Success):** If the ball steps out of bounds ($i < 0 \lor i \ge m \lor j < 0 \lor j \ge n$):
       $$
       \text{Escaped!} \implies \text{return } 1
       $$
    2. **Budget Exhaustion (Failure):** If the ball is still inside the grid and $k \le 0$:
       $$
       \text{Trapped!} \implies \text{return } 0
       $$
  - **4-Way Recurrence:**
    $$
    dfs(i, j, k) = \sum_{(di, dj) \in \{(-1, 0), (1, 0), (0, -1), (0, 1)\}} dfs(i + di, \; j + dj, \; k - 1) \pmod{10^9 + 7}
    $$
- **Step-by-Step Execution Trace from $(0, 0)$ with $k = 2$ moves:**
  - Initial call: $dfs(0, 0, 2)$
  - 4 directions from $(0, 0)$ with 1 move spent ($k' = 1$ remaining):
    - **Direction 1 (Up: $(-1, 0)$):**
      - New position: $(-1, 0)$.
      - Out of bounds!
      - Contributes:
        $$
        dfs(-1, 0, 1) = \mathbf{1} \text{ path (1-step escape)}
        $$
    - **Direction 2 (Left: $(0, -1)$):**
      - New position: $(0, -1)$.
      - Out of bounds!
      - Contributes:
        $$
        dfs(0, -1, 1) = \mathbf{1} \text{ path (1-step escape)}
        $$
    - **Direction 3 (Right: $(0, 1)$):**
      - New position: $(0, 1)$ (inside grid).
      - Evaluate $dfs(0, 1, 1)$ (1 move remaining):
        - Direction Up: $(-1, 1) \to$ out of bounds $\implies \mathbf{+1}$
        - Direction Down: $(1, 1) \to$ inside, budget becomes $0 \implies 0$
        - Direction Left: $(0, 0) \to$ inside, budget becomes $0 \implies 0$
        - Direction Right: $(0, 2) \to$ out of bounds $\implies \mathbf{+1}$
        - Total escapes from $(0, 1)$: $1 + 0 + 0 + 1 = \mathbf{2}$ paths.
      - Contributes:
        $$
        dfs(0, 1, 1) = \mathbf{2} \text{ paths}
        $$
    - **Direction 4 (Down: $(1, 0)$):**
      - New position: $(1, 0)$ (inside grid).
      - Evaluate $dfs(1, 0, 1)$ (1 move remaining):
        - Direction Up: $(0, 0) \to$ inside, budget becomes $0 \implies 0$
        - Direction Down: $(2, 0) \to$ out of bounds $\implies \mathbf{+1}$
        - Direction Left: $(1, -1) \to$ out of bounds $\implies \mathbf{+1}$
        - Direction Right: $(1, 1) \to$ inside, budget becomes $0 \implies 0$
        - Total escapes from $(1, 0)$: $0 + 1 + 1 + 0 = \mathbf{2}$ paths.
      - Contributes:
        $$
        dfs(1, 0, 1) = \mathbf{2} \text{ paths}
        $$
  - **Summing All Escape Trajectories:**
    $$
    \text{Total} = dfs(-1, 0, 1) + dfs(0, -1, 1) + dfs(0, 1, 1) + dfs(1, 0, 1)
    $$
    $$
    \text{Total} = 1 + 1 + 2 + 2 = \mathbf{6}
    $$
- **Paths Breakdown by Sequence:**
  1. `[Up]` (escapes in 1 move)
  2. `[Left]` (escapes in 1 move)
  3. `[Right, Up]` (escapes in 2 moves)
  4. `[Right, Right]` (escapes in 2 moves)
  5. `[Down, Down]` (escapes in 2 moves)
  6. `[Down, Left]` (escapes in 2 moves)
  - Total valid paths: **`6`**.
- **Center of Single Row Instance ($m = 1, n = 3, maxMove = 3, start = (0, 1)$):**
  - Up and down moves escape immediately in 1 step; left and right escape after 2 or 3 steps $\implies \mathbf{12}$ total paths.
- **Zero Move Allowance ($maxMove = 0$):**
  - $k \le 0$ inside grid $\implies \mathbf{0}$.

This instance demonstrates random walk boundary absorption dynamic programming, mathematically proves why memoizing across spatial coordinates and remaining moves compresses exponential branching into linear grid sweeps, and derives $O(M \cdot N \cdot K)$ runtime and $O(M \cdot N \cdot K)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ grid, a starting cell $(startRow, startColumn)$, and a budget of at most $maxMove$ steps:
Find the **total number of paths** that move the ball out of the grid boundary, modulo $10^9 + 7$.

```text
Grid (2 x 2), Ball at (0, 0), maxMove = 2:

1-Step Escapes (2 paths):
  - Move Up   -> Escapes top boundary
  - Move Left -> Escapes left boundary

2-Step Escapes (4 paths):
  - Move Right -> then Up
  - Move Right -> then Right
  - Move Down  -> then Down
  - Move Down  -> then Left

Total Paths = 2 + 4 = 6
```

### Absorbing Boundary Conditions
- When the ball moves outside the grid, it does **not** bounce back or continue moving; it immediately scores as $1$ successful out-of-bounds path.
- When the move budget runs out ($k = 0$) while still inside the grid, that path scores $0$.
- Because multiple branches reach the same cell with the same remaining moves, memoization over state $(i, j, k)$ prevents repeated subtree explorations.

---

## 2. Conceptual Foundation & Invariants

### 1. State Definition:
Let $dfs(i, j, k)$ be the number of valid escape paths starting from $(i, j)$ with $k$ moves remaining.

### 2. Base Cases:
$$
dfs(i, j, k) =
\begin{cases}
1 & \text{if } i < 0 \lor i \ge m \lor j < 0 \lor j \ge n \\
0 & \text{if } k \le 0 \land (0 \le i < m \land 0 \le j < n)
\end{cases}
$$

### 3. Transition:
$$
dfs(i, j, k) = \sum_{(di, dj)} dfs(i + di, \; j + dj, \; k - 1) \pmod{10^9 + 7}
$$
across the four unit vectors $\{(-1, 0), (1, 0), (0, -1), (0, 1)\}$.

> **Non-Decreasing Step Invariant.** Decrementing $k$ on each step guarantees that the state space is a Directed Acyclic Graph (DAG) with no cycles, ensuring well-founded termination.

---

## 3. Step-by-Step Worked Execution

We trace $m = 2, n = 2, maxMove = 2$ from $(0, 0)$:

---

### Step 1: Base Calls ($k = 1$)
- From $(0, 1)$ with $k = 1$:
  - Up $(-1, 1)$: out $\implies 1$
  - Down $(1, 1)$: inside, $k=0 \implies 0$
  - Left $(0, 0)$: inside, $k=0 \implies 0$
  - Right $(0, 2)$: out $\implies 1$
  - $dfs(0, 1, 1) = 1 + 0 + 0 + 1 = \mathbf{2}$.
- From $(1, 0)$ with $k = 1$:
  - Symmetrically: $dfs(1, 0, 1) = \mathbf{2}$.

---

### Step 2: Main Call $dfs(0, 0, 2)$
- Move Up: $(-1, 0)$ out $\implies \mathbf{1}$.
- Move Left: $(0, -1)$ out $\implies \mathbf{1}$.
- Move Right: $dfs(0, 1, 1) \implies \mathbf{2}$.
- Move Down: $dfs(1, 0, 1) \implies \mathbf{2}$.

---

### Step 3: Sum and Modulo
$$
1 + 1 + 2 + 2 = \mathbf{6} \pmod{10^9 + 7} = \mathbf{6}
$$

---

## 4. Complete Execution Trace

| Call | Position $(i, j)$ | Moves Remaining $k$ | Immediate Escape Edges | Sub-Calls Made | Returned Escape Count |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $dfs(-1, 0, 1)$ | $(-1, 0)$ | $1$ | Out of bounds | None | $1$ |
| $dfs(0, -1, 1)$ | $(0, -1)$ | $1$ | Out of bounds | None | $1$ |
| $dfs(0, 1, 1)$ | $(0, 1)$ | $1$ | Up, Right ($2$) | Down, Left ($0$) | $2$ |
| $dfs(1, 0, 1)$ | $(1, 0)$ | $1$ | Down, Left ($2$) | Up, Right ($0$) | $2$ |
| **$dfs(0, 0, 2)$** | **$(0, 0)$** | **$2$** | **Up, Left ($2$)** | **Right ($2$), Down ($2$)** | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **$maxMove = 0$:** Never leaves the initial cell $\implies \mathbf{0}$.
- **Ball in a Corner Cell ($0, 0$):** Has 2 immediate 1-step exits.
- **Ball in an Edge Cell:** Has 1 immediate 1-step exit.
- **Ball in an Interior Cell ($m, n \ge 3$):** Has 0 immediate 1-step exits; requires at least 2 steps to escape.

---

## 6. Traps & Common Anti-Patterns

- **Allowing the Ball to Move After Leaving the Grid:** Once the ball steps out of bounds, it has escaped; continuing to make moves from out-of-bounds positions artificially duplicates path counts.
- **Forgetting Modulo in Intermediate Additions:** The number of paths grows by a factor of up to 4 per move ($4^{50} \approx 1.26 \times 10^{30}$). All additions must apply modulo $10^9 + 7$.
- **Redundant State Recomputation:** Without memoization `@cache`, exponential branching leads to catastrophic TLE for $maxMove = 50$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Distinct states $(i, j, k)$: $m \times n \times (maxMove + 1)$.
  - Each state performs 4 additions taking $O(1)$ operations.
  - Total Time: $\mathcal{O}(M \cdot N \cdot K)$ where $K = maxMove$.
  - For $M = 50, N = 50, K = 50$, $50 \times 50 \times 50 = 1.25 \times 10^5$ operations, completing in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N \cdot K)$ space for the memoization cache table.