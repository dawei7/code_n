# Guided Example: Domino and Tromino Tiling

We trace the step-by-step $2 \times n$ polyomino board tiling, tile geometry rotations ($2 \times 1$ domino and $L$-tromino), 4-state column profile frontiers (fully filled, top protruding, bottom protruding, both empty), profile transfer matrix transitions ($g = M \cdot f$), and linear recurrence relation ($dp[n] = 2 \cdot dp[n-1] + dp[n-3]$) on representative board widths:

- **Input:** $n = 3$
- **Required output:** `5`
  - Polyomino tiles & board specifications:
    - Board dimensions: $2 \times n$ grid.
    - Two types of shapes (rotations allowed):
      1. **Domino:** $2 \times 1$ rectangle (2 squares). Can be placed vertically ($2 \times 1$) or horizontally ($1 \times 2$).
      2. **Tromino:** $L$-shaped tromino (3 squares, formed by removing 1 corner square from a $2 \times 2$ block). Can be rotated in 4 orientations.
    - Objective: Count the number of distinct ways to tile the $2 \times n$ board completely with no overlaps and no empty cells, modulo $10^9 + 7$.
    - For $n = 3$ ($2 \times 3$ board):
      - Configuration 1: Three vertical dominos (`|||`).
      - Configuration 2: One vertical domino + two horizontal dominos (`| =`).
      - Configuration 3: Two horizontal dominos + one vertical domino (`= |`).
      - Configuration 4: Two complementary $L$-trominos interlocking (top-left orientation).
      - Configuration 5: Two complementary $L$-trominos interlocking (bottom-left orientation).
      - Total valid tilings: **5**.
- **Column Profile States & Transfer Invariant:**
  - **The 4 Frontier States at Column $i$:**
    - To place tiles column by column, classify the coverage of column $i$:
      - **State 0 (Full):** Both rows in column $i$ are covered.
      - **State 1 (Top Only):** Only the top square of column $i$ is covered (bottom is open).
      - **State 2 (Bottom Only):** Only the bottom square of column $i$ is covered (top is open).
      - **State 3 (Empty):** Neither square of column $i$ is covered.
  - **State Transition Matrix:**
    - Advancing from column $i - 1$ to column $i$:
      1. To reach **State 0** (both filled):
         - Vertical domino from State 0 ($f[0]$).
         - $L$-tromino from State 1 ($f[1]$).
         - $L$-tromino from State 2 ($f[2]$).
         - Two horizontal dominos from State 3 ($f[3]$).
         $$
         g[0] = (f[0] + f[1] + f[2] + f[3]) \pmod{10^9 + 7}
         $$
      2. To reach **State 1** (top filled, bottom empty):
         - Horizontal domino on top + empty bottom:
         $$
         g[1] = (f[2] + f[3]) \pmod{10^9 + 7}
         $$
      3. To reach **State 2** (bottom filled, top empty):
         - Horizontal domino on bottom + empty top:
         $$
         g[2] = (f[1] + f[3]) \pmod{10^9 + 7}
         $$
      4. To reach **State 3** (both empty, extending into next column):
         - Two horizontal dominos starting at $i$:
         $$
         g[3] = f[0] \pmod{10^9 + 7}
         $$
  - **The Unfolded Scalar Recurrence:**
    - Eliminating intermediate states reveals the elegant 3-term recurrence for full tilings $T(n)$:
      $$
      T(n) = 2 \cdot T(n - 1) + T(n - 3) \quad \forall n \ge 3
      $$
      with initial seeds $T(0) = 1, \; T(1) = 1, \; T(2) = 2$.
- **Step-by-Step Worked Execution Trace on $n = 3$:**
  - Initial state before column 1:
    $$
    f = [1, \; 0, \; 0, \; 0]
    $$
  - **Column 1 ($i = 1$):**
    - Compute new profile $g$:
      - $g[0] = f[0] + f[1] + f[2] + f[3] = 1 + 0 + 0 + 0 = \mathbf{1}$ *(1 vertical domino)*.
      - $g[1] = f[2] + f[3] = 0 + 0 = \mathbf{0}$.
      - $g[2] = f[1] + f[3] = 0 + 0 = \mathbf{0}$.
      - $g[3] = f[0] = \mathbf{1}$ *(Horizontal tiles starting here)*.
    - Update state:
      $$
      f = [1, \; 0, \; 0, \; 1]
      $$
  - **Column 2 ($i = 2$):**
    - Compute new profile $g$:
      - $g[0] = f[0] + f[1] + f[2] + f[3] = 1 + 0 + 0 + 1 = \mathbf{2}$ *(2 tilings: `||` or `==`)*.
      - $g[1] = f[2] + f[3] = 0 + 1 = \mathbf{1}$ *(Top protrusion tromino candidate)*.
      - $g[2] = f[1] + f[3] = 0 + 1 = \mathbf{1}$ *(Bottom protrusion tromino candidate)*.
      - $g[3] = f[0] = \mathbf{1}$.
    - Update state:
      $$
      f = [2, \; 1, \; 1, \; 1]
      $$
  - **Column 3 ($i = 3$, Final Column):**
    - Compute new profile $g$:
      - $g[0] = f[0] + f[1] + f[2] + f[3] = 2 + 1 + 1 + 1 = \mathbf{5}$.
      - $g[1] = f[2] + f[3] = 1 + 1 = \mathbf{2}$.
      - $g[2] = f[1] + f[3] = 1 + 1 = \mathbf{2}$.
      - $g[3] = f[0] = \mathbf{2}$.
    - Update state:
      $$
      f = [\mathbf{5}, \; 2, \; 2, \; 2]
      $$
  - **Output Result:**
    - The number of complete tilings of the $2 \times 3$ board is the fully filled state $f[0]$:
      $$
      ans = f[0] = \mathbf{5}
      $$
  - **Verification via Linear Recurrence:**
    $$
    T(3) = 2 \cdot T(2) + T(0) = 2 \times 2 + 1 = \mathbf{5}
    $$
    Perfect mathematical agreement!
- **Base Widths Trace ($n = 1$ and $n = 2$):**
  - $n = 1$: Only 1 way (single vertical domino) $\implies ans = \mathbf{1}$.
  - $n = 2$: Two vertical dominos or two horizontal dominos $\implies ans = \mathbf{2}$.
- **Next Term Expansion ($n = 4$):**
  - $T(4) = 2 \cdot T(3) + T(1) = 2 \times 5 + 1 = \mathbf{11}$.

This instance demonstrates transfer matrix dynamic programming on planar strip graphs and polyomino tiling counting, mathematically proves why elimination of boundary protrusion states generates the third-order linear difference equation $T(n) = 2T(n-1) + T(n-3)$, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a $2 \times n$ board, $2 \times 1$ dominos, and L-trominos:
Find the **number of ways to tile the board** modulo $10^9 + 7$.

```text
n = 3 (2 x 3 board)

5 distinct tilings:
  1. | | |  (3 vertical dominos)
  2. | =    (1 vertical, 2 horizontal)
  3. = |    (2 horizontal, 1 vertical)
  4. L-tromino pair (orientation 1)
  5. L-tromino pair (orientation 2)

Result: 5
```

### The Invariant of the 4-State Column Profile
- Classify the boundary of each column into 4 states:
  - State 0: both rows filled (complete tiling).
  - State 1: top filled, bottom empty.
  - State 2: bottom filled, top empty.
  - State 3: both rows empty.
- Transitioning between columns yields the exact count, equivalent to $T(n) = 2 \cdot T(n - 1) + T(n - 3)$.

---

## 2. Conceptual Foundation & Invariants

### 1. State Vector & Transition Matrix:
$$
\vec{f} = \begin{bmatrix} f_0 \\ f_1 \\ f_2 \\ f_3 \end{bmatrix} \implies \begin{bmatrix} g_0 \\ g_1 \\ g_2 \\ g_3 \end{bmatrix} = \begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
1 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix} f_0 \\ f_1 \\ f_2 \\ f_3 \end{bmatrix} \pmod{10^9 + 7}
$$

### 2. Collapsed 3-Term Recurrence:
$$
T(n) = (2 \cdot T(n - 1) + T(n - 3)) \pmod{10^9 + 7} \quad \forall n \ge 3
$$
$$
T(0) = 1, \quad T(1) = 1, \quad T(2) = 2
$$

> **Generating Function Tiling Invariant.** The ordinary generating function for $2 \times n$ domino-tromino tilings is $F(x) = \frac{1 - x}{1 - 2x - x^3} = \sum_{n=0}^\infty T(n) x^n$, whose denominator polynomial directly yields the recurrence relation $T(n) - 2T(n-1) - T(n-3) = 0$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 3$:

---

### Step 1: Column 1
- $g = [1, 0, 0, 1]$.

---

### Step 2: Column 2
- $g = [2, 1, 1, 1]$.

---

### Step 3: Column 3
- $g[0] = 2 + 1 + 1 + 1 = \mathbf{5}$.

---

### Step 4: Output
$$
\mathbf{5}
$$

---

## 4. Complete Execution Trace

| Column $i$ | State 0 (Full) | State 1 (Top Only) | State 2 (Bottom Only) | State 3 (Empty) | Active Recurrence $T(i)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial ($0$) | $1$ | $0$ | $0$ | $0$ | $1$ |
| $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $2$ | $2$ | $1$ | $1$ | $1$ | $2$ |
| **$3$** | **$5$** | **$2$** | **$2$** | **$2$** | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Single vertical domino $\implies 1$.
- **$n = 2$:** Two vertical or two horizontal $\implies 2$.
- **Large $N = 1000$:** Transition matrix modulo $10^9 + 7$ prevents integer overflow.
- **Matrix Exponentiation ($O(\log N)$):** For $N \le 10^9$, matrix exponentiation on the $4 \times 4$ transfer matrix evaluates $T(n)$ in logarithmic time.

---

## 6. Traps & Common Anti-Patterns

- **Missing Modulo Operations:** In intermediate additions $f[0] + f[1] + f[2] + f[3]$, ensure `% mod` is applied at each step to avoid arbitrary-precision integer slowdowns.
- **Forgetting Tromino Rotations:** An L-tromino has 4 orientations; interlocking pairs can bridge columns of length $\ge 3$. The recurrence $T(n) = 2T(n-1) + T(n-3)$ accounts for all interlocking combinations.
- **Off-By-One Base Seeds:** Ensure $T(0) = 1$, $T(1) = 1$, $T(2) = 2$. Using $T(0) = 0$ corrupts the $n = 3$ term ($2 \times 2 + 0 = 4 \ne 5$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Loop runs $N$ times.
  - At each step, 4 constant-time arithmetic additions: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 1000$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only the 4-element state array).
