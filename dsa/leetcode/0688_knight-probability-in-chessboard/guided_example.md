# Guided Example: Knight Probability in Chessboard

We trace the step-by-step stochastic Markov state space transitions, uniform random walk branching ($\frac{1}{8}$ per legal move), dynamic programming step induction ($h \in [0, k]$), chessboard boundary absorption (probability 0 when off-board), and exact survivorship probability aggregation on representative knight walks:

- **Input:** $n = 3, \quad k = 2, \quad row = 0, \quad column = 0$
- **Required output:** `0.0625` ($\frac{1}{16}$)
  - Chessboard rules:
    - An $n \times n$ grid ($3 \times 3$, 0-indexed).
    - The knight begins at corner cell $(0, 0)$.
    - The knight attempts to execute exactly $k = 2$ moves.
    - At every move, the knight selects one of 8 standard L-shaped moves uniformly at random:
      $$
      P(\text{move}) = \frac{1}{8} = 0.125
      $$
    - If a move carries the knight outside the $3 \times 3$ grid boundaries, the knight falls off and can never return.
    - Objective: Calculate the exact probability that the knight remains on the board after completing $k = 2$ moves.
- **Markov Transition DP & Boundary Absorption Invariant:**
  - **The Recurrence Formulation ($f[h][i][j]$):**
    - Let $f[h][i][j]$ denote the probability that a knight positioned at cell $(i, j)$ **remains on the board** after executing $h$ subsequent moves.
  - **Base State ($h = 0$):**
    - With 0 moves remaining, any knight currently on the board has already survived:
      $$
      f[0][i][j] = 1.0 \quad \text{for all } 0 \le i, j < n
      $$
  - **Transition for Step $h$ ($1 \le h \le k$):**
    - From cell $(i, j)$, there are 8 mutually exclusive moves $(a, b)$.
    - If destination $(x, y) = (i + a, j + b)$ lies on the board ($0 \le x < n \land 0 \le y < n$), it contributes $\frac{1}{8} f[h - 1][x][y]$ to survival.
    - If $(x, y)$ is out of bounds, the survival probability from that branch is $0$:
      $$
      f[h][i][j] = \sum_{\substack{(a, b) \in \text{Moves} \\ 0 \le i+a < n \\ 0 \le j+b < n}} \frac{1}{8} f[h - 1][i + a][j + b]
      $$
  - **Final Target:**
    $$
    ans = f[k][row][column]
    $$
- **Step-by-Step Worked Execution Trace on $n = 3, k = 2$ starting at $(0, 0)$:**
  - Board dimensions: $3 \times 3$.
  - 8 Knight displacements:
    $$
    \{(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)\}
    $$
  - **Phase 0: Base Probabilities ($h = 0$):**
    - For all 9 cells $(i, j) \in [0, 2] \times [0, 2]$:
      $$
      f[0][i][j] = 1.0
      $$
  - **Phase 1: 1-Move Survival Probabilities ($h = 1$):**
    - Evaluate cells that are reachable from $(0, 0)$:
    - **From Cell $(0, 0)$:**
      - Test all 8 moves:
        1. $(-2, -1) \to (-2, -1)$: Off board (0)
        2. $(-2, 1) \to (-2, 1)$: Off board (0)
        3. $(-1, -2) \to (-1, -2)$: Off board (0)
        4. $(-1, 2) \to (-1, 2)$: Off board (0)
        5. $(1, -2) \to (1, -2)$: Off board (0)
        6. $(1, 2) \to (\mathbf{1}, \mathbf{2})$: On board!
        7. $(2, -1) \to (2, -1)$: Off board (0)
        8. $(2, 1) \to (\mathbf{2}, \mathbf{1})$: On board!
      - Exactly 2 of 8 moves stay on board:
        $$
        f[1][0][0] = \frac{1}{8}(1.0) + \frac{1}{8}(1.0) = \frac{2}{8} = \mathbf{0.25}
        $$
    - **From Cell $(1, 2)$:**
      - Out of 8 moves from $(1, 2)$, only two stay on board:
        - Move $(-1, -2) \to (\mathbf{0}, \mathbf{0})$: On board!
        - Move $(1, -2) \to (\mathbf{2}, \mathbf{0})$: On board!
      - All other 6 moves fall off the $3 \times 3$ grid.
      - Survival with 1 move left:
        $$
        f[1][1][2] = \frac{1}{8}(1.0) + \frac{1}{8}(1.0) = \frac{2}{8} = \mathbf{0.25}
        $$
    - **From Cell $(2, 1)$:**
      - By symmetry with $(1, 2)$, exactly 2 moves stay on board:
        - Move $(-2, -1) \to (\mathbf{0}, \mathbf{0})$: On board!
        - Move $(-2, 1) \to (\mathbf{0}, \mathbf{2})$: On board!
      - Survival with 1 move left:
        $$
        f[1][2][1] = \frac{2}{8} = \mathbf{0.25}
        $$
  - **Phase 2: 2-Move Survival from Start $(0, 0)$ ($h = 2$):**
    - From $(0, 0)$, the only legal on-board destinations are $(1, 2)$ and $(2, 1)$.
    - Each is chosen with probability $\frac{1}{8} = 0.125$.
    - Plug in their 1-move survival probabilities computed in Phase 1:
      $$
      f[2][0][0] = \frac{1}{8} f[1][1][2] + \frac{1}{8} f[1][2][1]
      $$
      $$
      f[2][0][0] = \frac{1}{8} \times 0.25 + \frac{1}{8} \times 0.25
      $$
      $$
      f[2][0][0] = \frac{0.25}{8} + \frac{0.25}{8} = \frac{0.50}{8} = \mathbf{0.0625}
      $$
    - In fractional form:
      $$
      \frac{1}{8} \times \frac{2}{8} + \frac{1}{8} \times \frac{2}{8} = \frac{2}{64} + \frac{2}{64} = \frac{4}{64} = \frac{1}{16} = \mathbf{0.0625}
      $$
  - **Step 4: Output:**
    $$
    ans = \mathbf{0.0625}
    $$
- **Zero Moves Boundary Case ($k = 0$):**
  - Knight makes 0 moves. Already on board $\implies$ survival probability is strictly **`1.0`**.
- **Center of Larger Board ($n = 8, row = 4, column = 4, k = 1$):**
  - All 8 moves stay on board $\implies 8 \times \frac{1}{8} = \mathbf{1.0}$.

This instance demonstrates finite Markov chain state probability propagation and grid boundary absorbing barrier modeling, mathematically proves why transition fractions decompose additively across recursive move horizons, and derives $O(K \cdot N^2)$ runtime and $O(K \cdot N^2)$ (or $O(N^2)$ space-optimized) space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ chessboard and starting position $(row, column)$:
At each step, a knight chooses one of 8 moves with probability $1/8$.
If it moves off the board, it dies.
Find the **probability the knight remains on the board after $k$ moves**.

```text
n = 3, k = 2, start at (0, 0)

Move 1 from (0, 0):
  Only 2 moves stay on board: (1, 2) and (2, 1).
  Probability of each = 1/8.

Move 2:
  From (1, 2): only 2 moves stay on board -> prob = 2/8.
  From (2, 1): only 2 moves stay on board -> prob = 2/8.

Total Probability:
  (1/8 * 2/8) + (1/8 * 2/8) = 2/64 + 2/64 = 4/64 = 1/16 = 0.0625
```

### The Invariant of the Markov Step
- The probability of surviving $h$ moves from $(i, j)$ equals the average of the probabilities of surviving $h - 1$ moves from all 8 destination cells.
- Any destination outside the board has survival probability 0.

---

## 2. Conceptual Foundation & Invariants

### 1. Markov Bellman Equation:
Base state:
$$
f[0][i][j] = 1.0 \quad \forall 0 \le i, j < n
$$
For $h = 1 \dots k$:
$$
f[h][i][j] = \sum_{\substack{(a, b) \in \text{Moves} \\ 0 \le i+a < n \\ 0 \le j+b < n}} \frac{f[h - 1][i + a][j + b]}{8}
$$

### 2. Conservation of Probability:
At any step, total probability mass either stays on the board or is absorbed into the off-board cemetery state.

> **Absorbing Markov Chain Invariant.** The random walk of the knight on grid $V$ with absorbing boundary $\partial V$ forms a time-homogeneous discrete Markov chain whose transient state probabilities at step $k$ satisfy $p^{(k)} = P^k p^{(0)}$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 3, k = 2, (0, 0)$:

---

### Step 1: Base State $h = 0$
- All on-board cells have $f[0] = 1.0$.

---

### Step 2: Step $h = 1$
- At $(1, 2)$: 2 legal moves $\implies f[1][1][2] = 2/8 = 0.25$.
- At $(2, 1)$: 2 legal moves $\implies f[1][2][1] = 2/8 = 0.25$.
- At $(0, 0)$: 2 legal moves $\implies f[1][0][0] = 2/8 = 0.25$.

---

### Step 3: Step $h = 2$ at $(0, 0)$
- Destinations are $(1, 2)$ and $(2, 1)$.
- $f[2][0][0] = \frac{1}{8}(0.25) + \frac{1}{8}(0.25) = \frac{0.5}{8} = \mathbf{0.0625}$.

---

### Step 4: Output
$$
\mathbf{0.0625}
$$

---

## 4. Complete Execution Trace

| Step $h$ | Evaluated Cell | Legal On-Board Moves | Destination Cells | Probabilities Used | Computed Survival Probability $f[h]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | All cells | — | — | Base state | $1.0$ |
| $1$ | $(1, 2)$ | $2$ / $8$ | $(0, 0), (2, 0)$ | $1.0, 1.0$ | $2/8 = 0.25$ |
| $1$ | $(2, 1)$ | $2$ / $8$ | $(0, 0), (0, 2)$ | $1.0, 1.0$ | $2/8 = 0.25$ |
| $1$ | $(0, 0)$ | $2$ / $8$ | $(1, 2), (2, 1)$ | $1.0, 1.0$ | $2/8 = 0.25$ |
| **$2$** | **$(0, 0)$** | **$2$ / $8$** | **$(1, 2), (2, 1)$** | **$0.25, 0.25$** | **$0.5 / 8 = \mathbf{0.0625}$** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$:** Always $1.0$ regardless of board size.
- **$1 \times 1$ Board ($n = 1, k \ge 1$):** Every knight move jumps off board $\implies 0.0$.
- **$2 \times 2$ Board ($n = 2, k \ge 1$):** Every knight move jumps off board $\implies 0.0$.
- **Large $k$ ($k = 100$):** Probability smoothly decays towards 0 without floating-point overflow.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Path Simulation ($8^k$):** For $k = 30$, $8^{30} \approx 1.2 \times 10^{27}$ paths, resulting in catastrophic Time Limit Exceeded. Dynamic programming reduces the state space to only $k \cdot n^2$.
- **Forgetting Division by 8 on Out-of-Bounds:** Each choice always has probability $1/8$, whether it stays on or leaves the board. Do not condition probability on "legal moves only".
- **Floating-Point Underflow:** Double precision floats easily handle probabilities down to $10^{-300}$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $k$ steps of dynamic programming.
  - In each step, iterate through all $n \times n$ cells.
  - At each cell, test 8 constant moves.
  - Total Time: $\mathcal{O}(k \cdot n^2)$ operations. For $n = 25, k = 100$, executes $\approx 5 \times 10^5$ operations in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(k \cdot n^2)$ for 3D table, or $\mathcal{O}(n^2)$ using two alternating 2D tables.
